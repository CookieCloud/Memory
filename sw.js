/* ═══════════════════════════════════════════════════════
   MEMÒRIA — Service worker
   ═══════════════════════════════════════════════════════

   COM FUNCIONEN LES ACTUALITZACIONS

   Cada cop que publiquis canvis, canvia el número de VERSIO d'aquí sota.
   Això fa que el navegador vegi un sw.js diferent, l'instal·li en segon pla
   i avisi la pàgina, que ensenya la barra "Hi ha una versió nova".

   Si no canvies VERSIO, el web continuarà servint la còpia desada i la gent
   no veurà els canvis. És l'únic que has de recordar de fer.

   LA MÚSICA
   Els fitxers de so (.mp3) es desen en una memòria a part, CACHE_SO, que
   NO s'esborra en canviar de versió: si no, cada actualització tornaria a
   baixar uns quants megues. Per canviar la música, puja-la amb un nom nou
   (com s'ha fet amb musica-record-piano.mp3) i canvia MUSICA_URL a l'index.html.
   ═══════════════════════════════════════════════════════ */
const VERSIO   = '4.80';
const CACHE    = 'memoria-v' + VERSIO;
const CACHE_SO = 'memoria-so';

/* Fitxers propis que es desen en instal·lar. Si en falta algun no passa res:
   es desen un a un perquè un error no faci caure tota la instal·lació. */
const NUCLI = [
  './',
  './index.html',
  './manifest.json',
  './memory32x32.png',
  './memory180x180.png',
  './memory192x192.png',
  './memory512x512.png',
  './memory-maskable512.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.all(NUCLI.map(f => c.add(f).catch(() => {}))))
    // Sense skipWaiting automàtic: qui decideix quan s'actualitza és la persona
    // que juga, des de la barra d'avís, i així no es talla cap partida.
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(claus => Promise.all(claus
        .filter(k => k !== CACHE && k !== CACHE_SO)     // la música es conserva
        .map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* La pàgina demana passar a la versió nova ara mateix */
self.addEventListener('message', e => {
  if (e.data && e.data.tipus === 'ACTIVA_JA') self.skipWaiting();
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  // Peticions parcials (les que fa un reproductor d'àudio o vídeo): les
  // deixem passar tal qual, perquè una resposta sencera de la memòria les
  // confondria i alguns navegadors deixarien de sonar
  if (req.headers.has('range')) return;

  const url = new URL(req.url);
  const propi = url.origin === location.origin;

  /* Música i sons: de la memòria de so, i si no hi són, de la xarxa */
  if (propi && url.pathname.endsWith('.mp3')){
    e.respondWith(
      caches.open(CACHE_SO).then(c => c.match(req).then(hit => hit ||
        fetch(req).then(resp => {
          if (resp.status === 200) c.put(req, resp.clone());
          return resp;
        })))
    );
    return;
  }

  /* L'HTML i la llista de fotos: primer la xarxa. Així els canvis arriben de
     seguida i, si no hi ha connexió, se serveix la còpia desada. */
  const esPagina = req.mode === 'navigate' ||
                   (propi && (url.pathname.endsWith('.html') || url.pathname.endsWith('fotos.json')));

  if (esPagina){
    e.respondWith(
      fetch(req)
        .then(resp => {
          const copia = resp.clone();
          caches.open(CACHE).then(c => c.put(req, copia));
          return resp;
        })
        .catch(() => caches.match(req).then(hit => hit || caches.match('./index.html')))
    );
    return;
  }

  /* Tipografies de Google: primer la xarxa, amb còpia de recanvi */
  if (url.hostname.includes('fonts.googleapis.com') || url.hostname.includes('fonts.gstatic.com')){
    e.respondWith(
      fetch(req).then(resp => {
        const copia = resp.clone();
        caches.open(CACHE).then(c => c.put(req, copia));
        return resp;
      }).catch(() => caches.match(req))
    );
    return;
  }

  /* La resta (fotos, icones): primer la còpia desada, que és molt més ràpid */
  e.respondWith(
    caches.match(req).then(hit => {
      if (hit) return hit;
      return fetch(req).then(resp => {
        if (resp.ok && propi){
          const copia = resp.clone();
          caches.open(CACHE).then(c => c.put(req, copia));
        }
        return resp;
      });
    })
  );
});
