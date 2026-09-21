#!/usr/bin/env python3
"""
Biblioteca de sons del web Memòria.

Tots els efectes són sintetitzats de zero (cap mostra de tercers) i es
munten en una sola tira, sons-memoria.mp3, amb silenci entre l'un i l'altre.
El web la baixa una vegada i després dispara cada tros pel seu compte.

Criteris: clars i evidents, com els d'una app de jocs, però sense cap
estridència. Res per sobre dels 5 kHz i atacs suaus de pocs mil·lisegons.
Els tons van en Fa pentatònic, el mateix to que la música de fons, perquè
els efectes no desafinin amb la música mentre sona.
"""
import json
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 44100
DIR = '/tmp/claude-0/-home-claude/46257fec-254f-5388-a15a-a7d89661eb07/scratchpad'
rng = np.random.default_rng(7)

def t_(dur): return np.arange(int(dur * SR)) / SR

def env(n, atac=0.004, decaiment=0.25, sosteniment=0.0):
    """Atac curt i caiguda exponencial: la forma d'un cop de mall"""
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(atac, 1e-5))
    e *= np.exp(-np.maximum(t - atac - sosteniment, 0) / decaiment)
    return e

def campana(f, dur, decaiment=None, parcials=(1, 2, 3.01), pesos=(1, .28, .09), atac=0.004):
    """Timbre de marimba/campana: fonamental i pocs parcials que s'apaguen"""
    t = t_(dur); n = len(t)
    d = decaiment if decaiment else dur * 0.38
    s = np.zeros(n)
    for p, w in zip(parcials, pesos):
        s += w * np.sin(2*np.pi*f*p*t) * np.exp(-t / (d / (1 + 0.8*(p - 1))))
    return s * env(n, atac, d)

def fusta(dur=0.03, lo=1200, hi=3600, decaiment=0.012):
    """Cop sec de fusta: soroll filtrat i molt curt"""
    n = int(dur * SR)
    x = rng.standard_normal(n)
    x = signal.sosfilt(signal.butter(2, [lo/(SR/2), hi/(SR/2)], 'band', output='sos'), x)
    return x * np.exp(-np.arange(n) / (decaiment * SR))

def escombrada(f0, f1, dur, tipus='soroll', ampla=0.5):
    """Fregada ascendent o descendent (per als efectes de moviment)"""
    t = t_(dur); n = len(t)
    if tipus == 'soroll':
        x = rng.standard_normal(n)
        sortida = np.zeros(n); bloc = 512
        for i in range(0, n, bloc):
            k = min(bloc, n - i)
            fc = f0 * (f1/f0) ** (i / max(n - 1, 1))
            fc = np.clip(fc, 60, SR/2 - 800)
            sos = signal.butter(2, [max(fc*(1-ampla), 40)/(SR/2), min(fc*(1+ampla), SR/2-600)/(SR/2)], 'band', output='sos')
            sortida[i:i+k] = signal.sosfilt(sos, x[i:i+k])
        return sortida * np.hanning(n)
    fase = 2*np.pi*np.cumsum(f0 * (f1/f0) ** (np.arange(n)/max(n-1, 1))) / SR
    return np.sin(fase) * env(n, 0.005, dur*0.4)

def posar(base, so, t0, guany=1.0):
    i = int(t0 * SR); n = min(len(so), len(base) - i)
    if n > 0: base[i:i+n] += so[:n] * guany
    return base

def buit(dur): return np.zeros(int(dur * SR))

# Fa pentatònic, com la música
FA, SOL, LA, DO, RE, FA2 = 349.2, 392.0, 440.0, 523.3, 587.3, 698.5
LA2, DO2, RE2, FA3 = 880.0, 1046.5, 1174.7, 1396.9

SONS = {}

# ── Interacció bàsica ──────────────────────────────────────────
s = buit(0.22)
posar(s, fusta(0.04, 1400, 3800, 0.010), 0, 0.55)
posar(s, campana(DO2, 0.18, 0.055, (1, 2.4), (1, .3)), 0.002, 0.6)
SONS['carta'] = s                      # tocar una carta

s = buit(0.26)
posar(s, fusta(0.05, 700, 2200, 0.016), 0, 0.6)
posar(s, campana(FA2, 0.22, 0.075, (1, 2), (1, .25)), 0.004, 0.5)
SONS['safata'] = s                     # la carta cau a la safata

s = buit(0.16)
posar(s, campana(LA2, 0.14, 0.05), 0, 0.75)
SONS['triar'] = s                      # marcar una opció

s = buit(0.16)
posar(s, campana(RE, 0.14, 0.05), 0, 0.7)
SONS['destriar'] = s                   # desmarcar-la

s = buit(0.13)
posar(s, fusta(0.02, 2000, 4200, 0.006), 0, 0.35)
posar(s, campana(DO2, 0.1, 0.03), 0.002, 0.4)
SONS['boto'] = s                       # botons i finestres

s = buit(0.3)
posar(s, campana(147, 0.26, 0.09, (1, 2), (1, .4)), 0, 0.9)
posar(s, fusta(0.03, 300, 900, 0.012), 0, 0.5)
SONS['bloquejada'] = s                 # tocar on no es pot

# ── Encerts ────────────────────────────────────────────────────
s = buit(0.7)
posar(s, campana(DO2, 0.4, 0.14), 0.00, 0.85)
posar(s, campana(SOL*2, 0.5, 0.20), 0.09, 0.95)
posar(s, campana(FA3, 0.4, 0.10, (1,), (1,)), 0.10, 0.25)
SONS['parella'] = s                    # parella trobada / encert

s = buit(0.55)
posar(s, campana(LA2, 0.3, 0.10), 0.00, 0.7)
posar(s, campana(DO2, 0.35, 0.13), 0.07, 0.8)
SONS['ronda'] = s                      # ronda superada, pas endavant

s = buit(0.95)
for k, f in enumerate([FA2, LA2, DO2, FA3]):
    posar(s, campana(f, 0.6, 0.18), 0.07*k, 0.75)
posar(s, escombrada(1200, 4000, 0.5) * np.exp(-t_(0.5)/0.18), 0.05, 0.16)
SONS['estrella'] = s                   # carta especial: buida la safata

s = buit(1.1)
for k, f in enumerate([DO, FA2, LA2, DO2, FA3]):
    posar(s, campana(f, 0.7, 0.22), 0.055*k, 0.6)
posar(s, escombrada(800, 4500, 0.7) * np.exp(-t_(0.7)/0.25), 0.02, 0.18)
SONS['buidar'] = s                     # la safata queda neta

# ── Errades ────────────────────────────────────────────────────
s = buit(0.55)
for k, f in enumerate([392.0, 311.1]):
    x = campana(f, 0.35, 0.16, (1, 2, 3), (1, .35, .12), atac=0.008)
    posar(s, x, 0.13*k, 0.85)
SONS['error'] = s                      # fallada

s = buit(0.95)
for k, f in enumerate([LA, FA, 293.7]):
    posar(s, campana(f, 0.55, 0.22, (1, 2), (1, .3), atac=0.01), 0.16*k, 0.7)
SONS['fi'] = s                         # partida acabada sense guanyar

s = buit(0.85)
for k in range(3):
    x = campana(LA2 if k < 2 else FA2, 0.22, 0.07, (1, 2), (1, .3))
    posar(s, x, 0.2*k, 0.8 - 0.1*k)
SONS['temps'] = s                      # s'acaba el temps

s = buit(0.06)
posar(s, fusta(0.02, 1800, 3500, 0.005), 0, 0.3)
SONS['tic'] = s                        # últims segons del rellotge

# ── Final de partida ───────────────────────────────────────────
s = buit(2.0)
for k, f in enumerate([FA2, LA2, DO2, FA3]):          # arpegi que puja
    posar(s, campana(f, 1.2, 0.35), 0.10*k, 0.7)
for k, f in enumerate([FA, LA, DO, FA2]):             # acord que queda sonant
    posar(s, campana(f, 1.6, 0.6, (1, 2), (1, .2), atac=0.02), 0.42 + 0.02*k, 0.45)
posar(s, escombrada(900, 4500, 0.9) * np.exp(-t_(0.9)/0.3), 0.06, 0.2)
for k in range(9):                                     # espurnes
    posar(s, campana(rng.choice([DO2, RE2, FA3, LA2*2]), 0.35, 0.09, (1,), (1,)),
          0.5 + 0.11*k + rng.uniform(0, .04), 0.16)
SONS['victoria'] = s                   # ho has aconseguit

s = buit(1.3)
for k, f in enumerate([FA2, DO2, FA3]):
    posar(s, campana(f, 0.9, 0.3), 0.09*k, 0.62)
posar(s, escombrada(700, 3500, 0.5) * np.exp(-t_(0.5)/0.2), 0.03, 0.14)
SONS['nivell'] = s                     # comença una partida nova

# ── Moviment de cartes ─────────────────────────────────────────
s = buit(0.95)
posar(s, escombrada(3200, 500, 0.55, ampla=0.7) * 0.5, 0, 0.5)
for k, dt in enumerate([0.22, 0.36, 0.47, 0.6]):       # les cartes que toquen a terra
    f = rng.uniform(120, 190)
    posar(s, campana(f, 0.3, 0.09, (1, 2.2), (1, .35)), dt, 0.55)
    posar(s, fusta(0.03, 500, 1800, 0.012), dt, 0.45)
SONS['caiguda'] = s                    # cauen cartes de càstig

s = buit(0.45)
posar(s, escombrada(400, 2600, 0.3, ampla=0.6) * 0.5, 0, 0.35)
posar(s, campana(FA2, 0.25, 0.08, (1, 2), (1, .2)), 0.16, 0.3)
SONS['apareix'] = s                    # es reparteixen les cartes

s = buit(0.4)
posar(s, escombrada(2600, 900, 0.22, ampla=0.6) * 0.5, 0, 0.3)
posar(s, campana(SOL, 0.2, 0.06, (1, 2), (1, .2)), 0.1, 0.35)
SONS['pista'] = s                      # es mostra la solució

# ── Els sis tons del joc de la seqüència (Fa pentatònic) ───────
for i, f in enumerate([FA, SOL, LA, DO, RE, FA2]):
    s = buit(0.55)
    posar(s, campana(f, 0.45, 0.17, (1, 2, 3), (1, .3, .08), atac=0.006), 0, 0.8)
    SONS[f'seq{i}'] = s

# ───────────────────────────────────────────────────────────────
# NIVELLS: cada so al seu punt, perquè cap destaqui sobre els altres
# ───────────────────────────────────────────────────────────────
PIC = {                                # pic desitjat, en dBFS
    # La música de fons té un RMS de -22 dBFS: els efectes han de quedar-hi
    # clarament per sobre, que és el que va demanar la Gerard.
    'carta': -6, 'safata': -7, 'triar': -8, 'destriar': -8, 'boto': -9,
    'bloquejada': -7, 'parella': -3, 'ronda': -5, 'estrella': -2, 'buidar': -3,
    'error': -5, 'fi': -6, 'temps': -4, 'tic': -14, 'victoria': -1,
    'nivell': -4, 'caiguda': -4, 'apareix': -9, 'pista': -8,
    **{f'seq{i}': -4 for i in range(6)},
}

tira, mapa, cursor = [], {}, 0.0
SILENCI = 0.25
for nom, x in SONS.items():
    x = signal.sosfiltfilt(signal.butter(2, 60/(SR/2), 'high', output='sos'), x)
    x = signal.sosfiltfilt(signal.butter(2, 5200/(SR/2), 'low', output='sos'), x)
    x[-int(0.01*SR):] *= np.linspace(1, 0, int(0.01*SR))       # sense talls secs
    x *= 10 ** (PIC[nom] / 20) / (np.max(np.abs(x)) + 1e-9)
    tira.append(buit(SILENCI)); cursor += SILENCI
    mapa[nom] = [round(cursor, 3), round(len(x)/SR + 0.06, 3)]
    tira.append(x); cursor += len(x) / SR
tira.append(buit(SILENCI))

audio = np.concatenate(tira)
wavfile.write(f'{DIR}/sons.wav', SR, (audio * 32767).astype(np.int16))
json.dump(mapa, open(f'{DIR}/sons.json', 'w'), ensure_ascii=False)

print(f'{len(SONS)} sons · tira de {len(audio)/SR:.1f} s · pic {20*np.log10(np.max(np.abs(audio))):.1f} dBFS')
for nom, (o, d) in mapa.items(): print(f'  {nom:<10} {o:6.3f} s  ({d:.2f} s)')
