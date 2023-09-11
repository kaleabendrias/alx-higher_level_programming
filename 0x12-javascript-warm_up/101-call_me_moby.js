#!/usr/bin/node
// func that executes x times a func.

function callMeMoby (x, y) {
  for (let i = 0; i < x; i++) {
    y();
  }
}

module.exports = {
  callMeMoby
};
