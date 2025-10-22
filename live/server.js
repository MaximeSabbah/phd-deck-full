// live/server.js
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 3001 });
const peers = new Map(); // id -> ws

wss.on('connection', (ws) => {
  let id = null;
  ws.on('message', raw => {
    const msg = JSON.parse(raw);
    if (msg.type === 'hello') { id = msg.id; peers.set(id, ws); return; }
    const dest = peers.get(msg.to);
    if (dest && dest.readyState === 1) dest.send(JSON.stringify({ from:id, ...msg }));
  });
  ws.on('close', () => { if (id) peers.delete(id); });
});
console.log('Signaling: ws://0.0.0.0:3001');
