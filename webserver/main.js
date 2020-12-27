var fs = require('fs'),
    http = require('http');
var count=0; // count on request
function get_ip(req)
{
  let ip="0.0.0.0"
  if (req.headers['x-forwarded-for']) {
    ip = "XF"+req.headers['x-forwarded-for'].split(",")[0];
  } else if (req.connection && req.connection.remoteAddress) {    
    ip = "RA"+req.connection.remoteAddress;
  } else {
    ip = "IP"+req.ip;
  }  
  return ip
}

function handler(req,res)
{
    count++;
    let ip =get_ip(req);
//    console.log(req.headers)
    console.log("Handler:"
    +count.toString() +":["
    +ip+"]:"
    +req.method+":"
    +req.url )

    fs.readFile(__dirname + req.url, function (err,data) {
        if (err) {
          res.writeHead(404);
          res.end(JSON.stringify(err));
          return;
        }
        res.writeHead(200);
        res.end(data);
      })
}
console.log("Web Server to render static files ")
console.log("starting at "+process.cwd())
http.createServer(handler).listen(8080);