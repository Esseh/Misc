package main
import(
	"fmt"
	"math/rand"
)
/* =======================================================
	Existing Character Sets
*/ =======================================================
func Lower()   string{ return "abcdefghijklmnopqrstuvwxyz" }
func Upper()   string{ return "ABCDEFGHIJKLMNOPQRSTUVWXYZ" }
func Integers()string{ return "1234567890" }
func Symbols() string{ return "~!@#$%^&*()_+-=,./;'[]\\<>?:\"{}|" }
func Letters() string{ return Lower()+Upper()}
func All()     string{ return Letters()+Integers()+Symbols()}
func Simple()  string{ return Letters()+Integers()}
/* ========================================================
// Makes a unique password based off of a string handed in.
// For example, utilizing a URL ie: "http://www.site.com/login"
// Will always generate the same password given the same
// key.
// ========================================================*/
func Password(url, charset string,length,key int64)(string){
	seed := int64(1)									// Initialize Seed
	for _,val := range []byte(url){ seed*=int64(val) }  // Fold across the input string
	rand.Seed(seed*key)									// Seed the generator with specific key
	// ====================================================
	// Generate Password of appropriate length
	// ====================================================
	var output string
	for output = ""; int64(len(output)) < length; { output += string(charset[rand.Int() % len(charset)]) }
	return output										// Send out the generated password.
}


func main(){
	fmt.Println(Password("this/url.coms",Simple(),20,99))
	fmt.Println(Password("this/url.com",Simple(),20,107))
	fmt.Println(Password("this/url.com",Simple(),100,107))
	fmt.Println(Password("this/url.com",Simple(),100,107))
}