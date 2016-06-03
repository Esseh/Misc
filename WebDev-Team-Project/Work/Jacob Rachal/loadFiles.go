// by Jacob Rachal 4-22-16
// in the specifications, this is taking in the file name as the string and the variable that the file is tied to as the string address.
// Zero is the default parameter that is passed in FIRST due to
// 0, {{string, &string}} -> LoadFiles
package main//Jacob_Rachal
 // see the LoadFiles.png for a diagram

var i int = 0; // the counter for the # of times any file is run through the loader. If i = 3 tries, panic since something fishy is going on.