/*
	This file is responsible for processing the user object to parse.
*/
package main
import(
		"encoding/json"				 //JSON
		"encoding/base64"			 //base64
		"strings"					 //String Parsing
)


func outputUser(Value string) User{
	//Value is of the form base64.StdEncoding.EncodeToString(r)+","+HmacEncode(base64.StdEncoding.EncodeToString(r))
	var output User
	tempString := Value											// Ready string for parsing
	tempString = strings.Split(tempString,",")[0]				// Get left side of data pair.
	decoded, _ := base64.StdEncoding.DecodeString(tempString)	//Decode data from base 64
	json.Unmarshal(decoded,&output)								//Unpack it into a User object.
	return output												//Return the object.
}