package main

import( "net/http" )

func init(){
	// Load Files and attach them to templates.
	loadFiles()
	// Handle the main page
	http.HandleFunc("/", index)
	// Handle the public folder.
	http.Handle("/public/", http.StripPrefix("/public", http.FileServer(http.Dir("public"))))
	// Serve
	http.ListenAndServe(":8080", nil)
}

