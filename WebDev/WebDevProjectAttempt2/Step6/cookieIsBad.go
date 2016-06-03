package main
import (
	"net/http"
	"crypto/hmac"
	"encoding/base64"
	"strings"
)
func cookieIsBad(cookie *http.Cookie) bool {
	//Data is of the form base64.StdEncoding.EncodeToString(input),base64.StdEncoding.EncodeToString([]byte(HmacEncode(base64.StdEncoding.EncodeToString(input))))
	stringsToParse := strings.Split(cookie.Value,",")	//Get Data Pairs
	t, _ := base64.StdEncoding.DecodeString(stringsToParse[1])
	return !(hmac.Equal([]byte(HmacEncode(stringsToParse[0])),[]byte(t)))
}