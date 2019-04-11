const express = require('express');
const crypto  = require('crypto');
const assert  = require('assert');
const fs      = require('fs');

const app = express();
const port = 3000;

const net = require('net');

const key = 'AAAAAAAAAAAAAAAA';
const iv  = 'BBBBBBBBBBBBBBBB';

function decrypt_data(data) {
    let decipher = crypto.createDecipheriv('aes-128-cbc', key, iv);
    //decipher.update(data, 'base64', 'binary');
    return decipher.final('binary');
}

// Generate keys (DH)
/*const serverEntity = crypto.createDiffieHellman(3072);
const serverKey = serverEntity.generateKeys();

// Generate p prime  and g generator
const p = serverEntity.getPrime();
const g = serverEntity.getGenerator();*/

// Send parameters to the client
// TODO:
// send 'serverKey', 'p', 'g'

// Receive key from client
/*let clientKey = "";
app.get('/dh_init', (req, res) => {
    if (false) {

    }
    else {
        
    }
})*/


// Generate server secret based on client parameters
//const serverSecret = serverEntity.computeSecret(clientKey);




/*app.get('/', (req, res) => {
    res.send('yoyoyyo');
    console.log("j'ai recu");
});

app.listen(port, () => {
    console.log(`listening on port ${port}.`);
});*/


// Create and return a net.Server object, the function will be invoked when client connect to this server.
let total_data = '';
var server = net.createServer(function(client) {

    console.log('Client connect. Client local address : ' + client.localAddress + ':' + client.localPort + '. client remote address : ' + client.remoteAddress + ':' + client.remotePort);

    client.setEncoding('utf-8');

    client.setTimeout(1000);

    // When receive client data.
    client.on('data', function (data) {

        // Print received client data and length.
        //console.log('Receive client send data : ' + data + ', data size : ' + client.bytesRead);
        total_data += data;
        console.log('data size : ' + client.bytesRead);
        // Server send data back to client use client net.Socket object.
        //client.end('Server received data : ' + data + ', send back to client data size : ' + client.bytesWritten);
    });

    // When client send data complete.
    client.on('end', function () {
        console.log('Client disconnect.');

        plain_data = decrypt_data(total_data);

        fs.writeFile("test.jpg", plain_data, function(err) {
            if(err) {
                return console.log(err);
            }
        
            console.log("The file was saved!");
        }); 

        // Get current connections count.
        server.getConnections(function (err, count) {
            if(!err)
            {
                // Print current connection count in server console.
                console.log("There are %d connections now. ", count);
            }else
            {
                console.error(JSON.stringify(err));
            }

        });
    });

    // When client timeout.
    client.on('timeout', function () {
        console.log('Client request time out. ');
    })
});

// Make the server a TCP server listening on port 9999.
server.listen(3000, function () {

    // Get server address info.
    var serverInfo = server.address();

    var serverInfoJson = JSON.stringify(serverInfo);

    console.log('TCP server listen on address : ' + serverInfoJson);

    server.on('close', function () {
        console.log('TCP server socket is closed.');
    });

    server.on('error', function (error) {
        console.error(JSON.stringify(error));
    });

});