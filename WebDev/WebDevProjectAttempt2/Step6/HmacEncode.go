/*
	This file is responsible for converting a string into the relevant HMAC encoded value.
*/

package main
import 	(
	"crypto/hmac"				 //HMAC
	"crypto/sha256"				 //sha256
)
func HmacEncode(data string) string {
	h := hmac.New(sha256.New, []byte(data+"superSecureKey"))
	return string(h.Sum(nil))
}