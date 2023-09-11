#!/usr/bin/node
const firstArgument = process.argv[2];

console.log(firstArgument !== undefined ? firstArgument : 'No argument');
