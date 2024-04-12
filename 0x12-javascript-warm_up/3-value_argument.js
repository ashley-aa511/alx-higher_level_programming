#!/usr/bin/node
// Prints the first argument passed to it

// Check if there is at least one argument
if (process.argv[2]) {
  console.log(process.argv[2]); // Print the first argument
} else {
  console.log('No argument'); // Print if no argument is passed
}
