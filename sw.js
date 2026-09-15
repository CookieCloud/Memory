/* Service worker de Memòria
   Puja el número de CACHE cada cop que canviïs index.html: així el navegador
   descarta la còpia antiga i es queda la nova. */
const CACHE = 'memoria-v2.17';

const FITXERS = [
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
      // addAll falla sencer si hi manca un fitxer; d'un en un, el que hi sigui es desa
      .then(c => Promise.all(FITXERS.map(f => c.add(f).catch(err => console.warn('Cache:', f, err)))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(claus => Promise.all(claus.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  // Les fonts de Google: primer la xarxa, i si no hi ha connexió, la còpia desada
  if (req.url.includes('fonts.googleapis.com') || req.url.includes('fonts.gstatic.com')){
    e.respondWith(
      fetch(req).then(resp => {
        const copia = resp.clone();
        caches.open(CACHE).then(c => c.put(req, copia));
        return resp;
      }).catch(() => caches.match(req))
    );
    return;
  }

  // Fitxers propis: primer la còpia desada, i si no hi és, la xarxa
  e.respondWith(
    caches.match(req).then(hit => hit || fetch(req).then(resp => {
      if (resp.ok && new URL(req.url).origin === location.origin){
        const copia = resp.clone();
        caches.open(CACHE).then(c => c.put(req, copia));
      }
      return resp;
    }).catch(() => caches.match('./index.html')))
  );
});
