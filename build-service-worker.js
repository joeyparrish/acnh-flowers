#!/usr/bin/env node

(async () => {
  const {generateSW} = require('workbox-build');
  const {count, size, warnings} = await generateSW({
    maximumFileSizeToCacheInBytes: 3e6,
    globDirectory: '.',
    globPatterns: [
      '*.otf',
      'index.html',
      'icons/**/*.png',
    ],
    skipWaiting: true,
    swDest: 'service-worker.js',
  });

  if (warnings.length > 0) {
    console.warn(`Warnings encountered while generating a service worker: ${warnings.join('\n')}`);
  }
  console.log(`Generated a service worker to precache ${count} files, totaling ${size} bytes.`);
})();
