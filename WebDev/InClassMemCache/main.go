package main
import (
	"net/http"
	"fmt"
)


type Object struct{Data string}

// Run the Handler
func init() { 
	http.HandleFunc("/", handlerHome) 
	http.HandleFunc("/store/", handlerStore)
	http.HandleFunc("/retrieve/", handlerRetrieve)
}

func handlerStore(res http.ResponseWriter, req *http.Request) {}
func handlerHome(res http.ResponseWriter, req *http.Request) {}
func handlerRetrieve(res http.ResponseWriter, req *http.Request) {}