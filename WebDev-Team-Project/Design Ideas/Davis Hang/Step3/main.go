package main

import( "net/http" )

func init(){
	// Load Files and attach them to templates.
	loadFiles()
	// Handle the main page
	http.HandleFunc("/", index)
	// Handle the login page
	http.HandleFunc("/login/", login)
	// Handle the logging out
	http.HandleFunc("/logout/", logout)
	// Handle the Edit User Page
	http.HandleFunc("/edituser/", edituser)
	// Handle the login page
	http.HandleFunc("/register/", register)
	// Handle the Username Exists API call
	http.HandleFunc("/usernameexists/", userNameExists)
	// Handle the public folder.
	http.Handle("/public/", http.StripPrefix("/public", http.FileServer(http.Dir("public"))))
}

