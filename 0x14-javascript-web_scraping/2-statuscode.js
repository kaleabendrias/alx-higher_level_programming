#!/usr/bin/node

const url = process.argv[2];

fetch(url)
  .then((response) => console.log(response.status));
