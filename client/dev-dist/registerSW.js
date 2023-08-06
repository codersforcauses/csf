if ('serviceWorker' in navigator) {
  await navigator.serviceWorker.register('/dev-sw.js?dev-sw', { scope: '/', type: 'classic' }).then(() => {
    console.log("Service Worker Registered");
  }).catch((error) => {
    console.log(error);
  })
  await navigator.serviceWorker.ready;
}
