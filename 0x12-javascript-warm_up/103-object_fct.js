#!/usr/bin/node
// script by adding a new function incr

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function incr () {
  this.value++;
}
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
