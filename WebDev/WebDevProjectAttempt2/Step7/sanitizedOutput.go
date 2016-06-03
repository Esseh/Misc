/*
	This file is responsible for sanitizing cookie output values.
*/
package main
import(
		"encoding/base64"			 //base64
)

func sanitizedOutput(input []byte) string{
	left := base64.StdEncoding.EncodeToString(input)
	delimiter := ","
	right := base64.StdEncoding.EncodeToString([]byte(HmacEncode(base64.StdEncoding.EncodeToString(input))))
	return left+delimiter+right
}