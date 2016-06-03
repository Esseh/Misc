/*
	This file is responsible for processing the user object to parse.
*/
package main
import(
		"encoding/json"				 //JSON
		"encoding/base64"			 // base64
)


func outputUser(Value string) User{
	var output User
	decoded, _ := base64.StdEncoding.DecodeString(Value)		//Decode data from base 64
	json.Unmarshal(decoded,&output)								//Unpack it into a User object.
	return output												//Return the object.
}