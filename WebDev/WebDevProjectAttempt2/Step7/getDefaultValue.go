/*
	This file is responsible for getting the default cookie value for session-info
*/
package main
import(
		"encoding/json"				 //JSON
		"github.com/nu7hatch/gouuid" //UUID
)

func getDefaultValue() string {
	id,_ := uuid.NewV4()				//Get the cookie a unique universal id.
	name := "NULL"					    //Default the name to NULL
	age  := "NULL"						//Default the age to NULL
	loggedin := "loggedOff"				//Default log in status is "loggedOff"
	r, _ := json.Marshal(User{id.String(),name,age,loggedin})	//Result to store
	//Return the string encoded in base64 and it's HMAC encoding delimited by a ';'
	return sanitizedOutput(r)
}