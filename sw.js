/* ═══════════════════════════════════════════════════════
   MEMÒRIA — Service worker
   ═══════════════════════════════════════════════════════ */
const VERSIO = '3.41';
const CACHE  = 'memoria-v' + VERSIO;

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
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(claus => Promise.all(claus.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('message', e => {
  if (e.data && e.data.tipus === 'ACTIVA_JA') self.skipWaiting();
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const propi = url.origin === location.origin;

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
