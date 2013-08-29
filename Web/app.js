var osc = require('node-osc');
var util = require('util');
var ip = "127.0.0.1"


var oscServer = new osc.Server(3333, ip); //server que vai escutar do puredata


var http = require('http'),
    fs = require('fs'),
    // NEVER use a Sync function except at start-up!
    index = fs.readFileSync(__dirname + '/index.html');

// formata cabecalho html
var app = http.createServer(function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(index);
});

// Socket.io server listens to our app
var io = require('socket.io').listen(app);


//injeta a mensagem puredata no html
oscServer.on("message", function (msg, rinfo) {
      io.sockets.emit('time', {time: msg })
      //console.log(msg);//debug2
      //console.log(JSON.stringify(msg);//debug2
      });


app.listen(3000); //repassa o app para html na porta 3000
