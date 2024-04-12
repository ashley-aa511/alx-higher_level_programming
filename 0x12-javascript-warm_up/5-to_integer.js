#!/usr/bin/node
// Prints argument if its an integer

const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
