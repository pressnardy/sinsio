const CACHE_NAME = 'my-pwa-cache-v1';
const urlsToCache = [

    '/static/eccentric/svg/notify.svg',
    '/static/eccentric/svg/search.svg',
    '/static/eccentric/svg/whatsapp-chat.svg',
    '/static/s.svg',
    '/static/iconfavicon.png',
    '/static/sicon.svg',
    '/eccentric/home.html',
    '/eccentric/login.html',
    '/eccentric/register.html',
    '/clients/index.html',
    '/clients/register.html',
    '/clients/search.html',
    '/clients/edit.html',

];


self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});


self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
  );
});
