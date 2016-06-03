package main

import( "html/template" )

var indexT *template.Template

func loadFiles(){
	// Load and Parse File
	var err error
	indexT, err =template.ParseFiles("templates/index.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
}