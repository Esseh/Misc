package main

import( "html/template" )

var indexT *template.Template
var loginT *template.Template
var registerT *template.Template
var edituserT *template.Template

func loadFiles(){
	// Load and Parse File
	var err error
	indexT, err =template.ParseFiles("templates/index.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
	loginT, err =template.ParseFiles("templates/login.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
	registerT, err =template.ParseFiles("templates/register.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
	edituserT, err =template.ParseFiles("templates/edituser.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
}