var http = require('http');
var dandt = require('./date')

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.write('Hello World! ');
  res.end("The date and time is currently: " + dandt.date_time());
}).listen(8080);