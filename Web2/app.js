// importa node-osc e socket.io (lib para facilitar uso de websockets)
var osc = require('node-osc'),
    io = require('socket.io').listen(8081); // servidor websocket

// quando um cliente conectar no servidor websocket...
io.sockets.on('connection', function (socket) {
  // cria um servidor OSC escutando na porta 3333
  var oscServer = new osc.Server(3333, '127.0.0.1');

  // quando o servidor OSC receber (do Pd ou outra app) uma mensagem...
  oscServer.on("message", function (msg, rinfo) {
    // usa o websocket e manda a mensagem para o cliente conectado na 8081
    socket.emit("coords", {lat: msg[1], lng: msg[2]});
    // mostra no terminal a mensagem recebida por OSC e enviada por websocket
    console.log("mensagem OSC do Pd: ", msg, " enviada por: ", rinfo);
  });
});