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
)

func getCode(data string) string {
	h := hmac.New(sha256.New, []byte(data+"superSecureKey"))
	return string(h.Sum(nil))
}


func updateCookie(cookie *http.Cookie, req *http.Request) string {
	//Unpack the JSON into a User
	jsonValues, _ := unpackJSON(cookie)
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

//Also returns the validity of the HMAC data.
func unpackJSON(cookie *http.Cookie) (User, bool){
		//Recover the JSON
		decode, _ := base64.StdEncoding.DecodeString(cookie.Value)
		
		//Value to hold the unmarshalled JSON
		var jsonValues User

		//Unmarshal the JSON
		json.Unmarshal(decode,&jsonValues)
		
		if hmac.Equal([]byte(jsonValues.Hmac),[]byte(getCode(jsonValues.Uuid + jsonValues.Name + jsonValues.Age))){
			return jsonValues, true
		}
	return jsonValues, false
}

func defaultCookie() *http.Cookie{
	//Get UUID
	id,_ := uuid.NewV4()
	//Construct instance of User
	temp := User{Uuid:id.String(),Hmac:getCode(id.String())}
	//Marshal this into JSON.
	b, _ := json.Marshal(temp)
	//Encode the JSON in base64
	encode := base64.StdEncoding.EncodeToString(b)
	return &http.Cookie{
		Name:  "session-fino",
		Value: encode,
		// Secure: true,
		HttpOnly: true,
	}
}