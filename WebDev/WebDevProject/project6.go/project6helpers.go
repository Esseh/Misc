/*==============================================================
	Kenneth Willeford
	Project Part 5 Helper Functions

==============================================================*/
package main
import (
		"net/http"						// web server
		"github.com/nu7hatch/gouuid"	// UUID
		"encoding/json"					// JSON
		"encoding/base64"				// base64
		"crypto/hmac"
		"crypto/sha256"
		"fmt"
)


func getCode(data string) string {
	h := hmac.New(sha256.New, []byte(data+"superSecureKey"))
	return string(h.Sum(nil))
}


func updateCookie(cookie *http.Cookie, req *http.Request) string {
	//Unpack the JSON into a User
	jsonValues := unpackJSON(cookie)
	fmt.Println(jsonValues)
	//New Entries for the User
	jsonValues.Name = req.FormValue("name")
	jsonValues.Age = req.FormValue("age")
	jsonValues.Hmac = getCode(jsonValues.Uuid + jsonValues.Name + jsonValues.Age)
	return repackJSON(jsonValues)
}

func repackJSON(jsonValues User) string{
	//Convert back to JSON
	b, _ := json.Marshal(jsonValues)
	
	//Encode the JSON in base64
	return base64.StdEncoding.EncodeToString(b)
}

func unpackJSON(cookie *http.Cookie) User{
		//Recover the JSON
		//decode, _ := base64.StdEncoding.DecodeString(cookie.Value)
		decode := []byte(cookie.Value)
		//Value to hold the unmarshalled JSON
		var jsonValues User

		//Unmarshal the JSON
		json.Unmarshal(decode,&jsonValues)
		
	return jsonValues
}

func defaultCookie() *http.Cookie{
	//Get UUID
	id,_ := uuid.NewV4()
	//Construct instance of User
	temp := User{id.String(),"empty","empty","empty"}
	temp.Hmac = getCode(temp.Uuid + temp.Name + temp.Age)
	//Marshal this into JSON.
	b, _ := json.Marshal(temp)
	//Encode the JSON in base64
	//encode := base64.StdEncoding.EncodeToString(b)
	encode := b
	fmt.Println(b)
	return &http.Cookie{
		Name:  "session-fino",
		Value: string(encode),
		// Secure: true,
		HttpOnly: true,
	}
}