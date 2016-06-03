package main
import(
		"encoding/json"				 //JSON
		"github.com/nu7hatch/gouuid" //UUID
		"encoding/base64"			 // base64
)

func getDefaultValue() string {
	id,_ := uuid.NewV4()				//Get the cookie a unique universal id.
	name := "NULL"					    //Default the name to NULL
	age  := "NULL"						//Default the age to NULL
	r, _ := json.Marshal(User{id.String(),name,age})	//Result to store
	return base64.StdEncoding.EncodeToString(r)			//Return the string encoded in base64. 
}