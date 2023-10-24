#!/usr/bin/node
const fs = require("fs")
const req = require("request")

url = process.argv[2]
file_path = process.argv[3]

req.get(url, (err, res, body) => {
    if (!err && res.statusCode === 200){
        const fileStream = fs.createWriteStream(file_path);
        fileStream.write(body)
    }
    else{
        console.log(err)
    }
})