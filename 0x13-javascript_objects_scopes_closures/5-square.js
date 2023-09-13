#!/usr/bin/node
// Square that defines a square and inherits from Rectangle

module.exports = class square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size); // call the super class's constructor with the arguments passed in.
  }
};
