package main
import (
	"net/http"
	"io/ioutil"
	"fmt"
	"strconv"
)



var page string
var uniqueID int

// Simply Serves the Index.html page. The rest is handled by the page's AJAX. 
func index(res http.ResponseWriter, req *http.Request){
	fmt.Fprintf(res,page)
}

//receives raw string query , outputs formatted string with unique id.
func ajax(res http.ResponseWriter, req *http.Request){
	//Make sure only plain text is printed.
	res.Header().Set("Content-Type","text/plain")
	//Print the formatted string with unique id.
	fmt.Fprintf(res,`<div class="readable" onclick="killMe('`+strconv.Itoa(uniqueID)+`')" id="`+ strconv.Itoa(uniqueID) +`">` + req.FormValue("key") + `</div>`)
	// Advance unique id by 1. 
	uniqueID++
}

func init(){
	// Initialize the file.
	temp, _ := ioutil.ReadFile("index.html")	
	page = string(temp)
	uniqueID = 0
}

func main(){	
	// Handle the image files.
	http.Handle("/files/",http.StripPrefix("/files",http.FileServer(http.Dir("files"))))
	// Serve the index.html page.
	http.HandleFunc("/", index)
	// Serve the ajax page to be polled.
	http.HandleFunc("/ajax/", ajax)
	// Serve Server
	http.ListenAndServe(":8080",nil)
}