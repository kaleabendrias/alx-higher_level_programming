#!/usr/bin/node
// function that executes x times a function.

function callMeMoby(x, y){
    for (let i = 0; i < x; i++) {
        y();
    }
}

module.exports = {
    callMeMoby: callMeMoby
};