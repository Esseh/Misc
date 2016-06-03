package main

import( 
	"net/http" 
	"html/template"
)

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

type LoginCheck struct{
	Url string
	UrlText string
	Edit string
}


// The main page. The front of our Lorem Ipsum website.
func index(res http.ResponseWriter, req *http.Request){
	
	/* Check if the user is logged in. */
	_, err := req.Cookie("session-info")
	var Status LoginCheck
	if(err != nil){ 
		Status = LoginCheck{Url:`login` , UrlText:`Log In`}
	} else {
		Status = LoginCheck{Url:`/logout` , UrlText:`Log Out`}
		Status.Edit = "true"
	}

	// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
	res.Header().Set("Content-Type","text/html")
	// Execute our template
	indexT.Execute(res, Status)
}


// The login page. Handles Login requests.
func login(res http.ResponseWriter, req *http.Request){
	// Check if they're already logged in.
	_ ,err := req.Cookie("session-info")
	// If they aren't then let them through.
	if err!=nil{
		if(req.Method == "POST"){
			// From AJAX if everything is fine push the login request forward.(second authentication handled within.)
			loginRequest(res,req)
		} else { 
			// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
			res.Header().Set("Content-Type","text/html")
			// Execute our template
			loginT.Execute(res, nil)
		}	
	} else{
		//If they're already logged in redirect them to the main page.
		http.Redirect(res, req, "/", http.StatusFound)
	}
}


// The edituser page. Handles the editing of the user information. For now just the password. In the future blog info.
func edituser(res http.ResponseWriter, req *http.Request){
	if(authenticatedUser(req,res)){
		if(req.Method == "POST"){
			changePassword(res,req,req.FormValue("userPasswordInput"))
			http.Redirect(res, req, "/", http.StatusFound)
		} else {
			res.Header().Set("Content-Type","text/html")
			edituserT.Execute(res, nil)
		}
	}
}


// The main page. The front of our Lorem Ipsum website.
func register(res http.ResponseWriter, req *http.Request){
	// Check if they're already logged in.
	_,err := req.Cookie("session-info")
	// If they aren't then let them through.
	if err!=nil{
		if(req.Method == "POST"){
			// From AJAX if everything is fine push the register request forward. (Second authentication handled within)
			registerRequest(res,req)
			// Redirect them once the registerRequest completes
			//http.Redirect(res, req, "/", http.StatusFound)
		} else { 
			// Set the content type to html , this was to fix a bug where the content header defaulted to text/plain
			res.Header().Set("Content-Type","text/html")
			// Execute our template
			registerT.Execute(res, nil)
		}
	} else {
		//If they're already logged in redirect them to the main page.
		http.Redirect(res, req, "/", http.StatusFound)
	}
}



