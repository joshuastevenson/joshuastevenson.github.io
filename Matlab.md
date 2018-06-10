---
title: I hate Matlab
lastEdited: 2018-06-10
---

# I hate Matlab
A lot of my work is replacing Matlab code with mex functions written in c++. Matlab is problematic. Disclaimer: this is not going to be well organized.

## Matlab is slower than you'd expect
Matlab uses MKL. So why did I need to write a mex function that calls MKL to do a matrix transpose? Why is Matlab's `fread` 3x slower than C? 

## Object oriented matlab was a mistake
A single function per file is bad enough. Add oop ideas and navigating code becomes an even bigger hassle.

## Bleh
Indexes start at 1. Can't index the return value of a function.

## Language design inhibits performance aware programming
Matlab stores matrices in a Column Major format. Fine enough by itself. But the default array is a row. Want to have multiple arrays? Now you need to swap the dimensions. 

