if('serviceWorker' in navigator){
    navigator.serviceWorker.register('/dev-sw.js?dev-sw', { scope: '/', type: 'classic' });
    console.log("SW in navigator!")
}