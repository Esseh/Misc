package main

import( 
	"net/http" 
	"html/template"
	"strings"
	"fmt"
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
	// Handle the User File Manager
	http.HandleFunc("/edituser/file/", fileHandler)
	// Handle the login page
	http.HandleFunc("/register/", register)
	// Handle the Email in use API call
	http.HandleFunc("/emailinuse/", emailInUse)
	// Handle the Remove Image API call
	http.HandleFunc("/edituser/file/removeimage/", API_removeImage)
	// Handle the Username Exists API call
	http.HandleFunc("/usernameexists/", userNameExists)
	// Handle the Password Is Good API call
	http.HandleFunc("/passwordisgood/", passwordIsGood)
	// Handle API call to post comment
	http.HandleFunc("/postcomment/", postComment)
	// Handle the public folder.
	http.Handle("/public/", http.StripPrefix("/public", http.FileServer(http.Dir("public"))))
	// Handle Blog Posts
	http.HandleFunc("/blog/", blog)
}

var indexT *template.Template
var loginT *template.Template
var registerT *template.Template
var edituserT *template.Template
var managefileT *template.Template
var blogT *template.Template

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
	managefileT, err =template.ParseFiles("templates/managefile.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
	blogT, err =template.ParseFiles("templates/blog.html")
	// If something went wrong panic.
	if err != nil{ panic("Couldn't load file.") }
}

type LoginCheck struct{
	Url string
	UrlText string
	Edit string
	BlogList []string
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
	data, perr := retrievePages(req)
	if perr != nil {}
	Status.BlogList = data.Data 
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
	cookie,err := req.Cookie("session-info")
	if err != nil{ 
		fmt.Fprint(res,"cookie not found") 
		return 
	}
	values := strings.Split(cookie.Value,",")
	username := values[1]
	if(authenticatedUser(req,res)){
		if(req.Method == "POST"){
			// If the user wasn't grabbed exit.
			data, err := retrieveUser(username ,req)
			if err != nil {
				fmt.Fprint(res,err)
				return	
			}
			// Make sure the confirmation password is good. If it is change the password.
			if data.Password == req.FormValue("oldPasswordInput"){ changePassword(res,req,req.FormValue("userPasswordInput")) }			
			obj, err := retrieveBlogData(req,username)
			if err != nil {}
			obj.BlogTitle = req.FormValue("blogTitleInput")
			obj.BlogTitleBody = req.FormValue("blogTitleBodyInput")
			obj.LeftTitle = req.FormValue("leftTitleInput")
			obj.LeftBody = req.FormValue("leftBodyInput")
			obj.BlogBody = req.FormValue("blogBodyInput")
			obj.RightTitle = req.FormValue("rightTitleInput")
			obj.RightBody = req.FormValue("rightBodyInput")
			obj.FooterRight = req.FormValue("leftFooterInput")
			obj.FooterLeft = req.FormValue("rightFooterInput")
			obj.BlogCSS = req.FormValue("cssStyle")
			storeBlogData(obj, username, req)
			http.Redirect(res, req, "/", http.StatusFound)
		} else {			
			
			obj, err := retrieveBlogData(req,username)
			if err != nil {}
			res.Header().Set("Content-Type","text/html")
			edituserT.Execute(res, obj)
		}
	}
}

// Where the user can upload and manage their files.
func fileHandler(res http.ResponseWriter, req *http.Request){
	cookie,err := req.Cookie("session-info")
	if err != nil{ 
		fmt.Fprint(res,"cookie not found") 
		return 
	}
	values := strings.Split(cookie.Value,",")
	username := values[1]
	if(authenticatedUser(req,res)){
		if(req.Method == "POST"){
			file, _, ferr := req.FormFile("fileUpload")
			if ferr == nil { 
				createFileGCS(req, file,res) 
			}
 			http.Redirect(res, req, "/edituser/file/", http.StatusFound)
		} else {
			obj, err := retrieveBlogData(req,username)
			if err != nil {}				
			res.Header().Set("Content-Type","text/html")
			managefileT.Execute(res, obj)		
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

type BlogPost struct{
	Url string
	UrlText string
	Edit string
	BlogTitle string
	BlogTitleBody string
	LeftTitle string
	LeftBody string
	BlogBody string
	RightTitle string
	RightBody string
	FooterRight string
	FooterLeft string
	BlogCSS string
	Images []string
	Comments []string
	URL string
}


func blog(res http.ResponseWriter, req *http.Request){
	obj := BlogPost{}
	/* Check if the user is logged in. */
	_, err := req.Cookie("session-info")
	var Status LoginCheck
	if(err != nil){ 
		Status = LoginCheck{Url:`/login/` , UrlText:`Log In`}
	} else {
		Status = LoginCheck{Url:`/logout/` , UrlText:`Log Out`}
		Status.Edit = "true"
	}
	
	// Get the blog based on the URL
	path := req.URL.Path
	path = strings.Split(path,"/")[2]
	data, err := retrieveBlogData(req, path)
	if err != nil{
		return
	}

	obj.Url				= Status.Url 
	obj.UrlText			= Status.UrlText
	obj.Edit			= Status.Edit
	obj.BlogTitle		= data.BlogTitle
	obj.BlogTitleBody	= data.BlogTitleBody
	obj.LeftTitle		= data.LeftTitle
	obj.LeftBody		= data.LeftBody
	obj.BlogBody 		= data.BlogBody
	obj.RightTitle 		= data.RightTitle
	obj.RightBody 		= data.RightBody
	obj.FooterRight 	= data.FooterRight
	obj.FooterLeft		= data.FooterLeft
	obj.BlogCSS 		= data.BlogCSS
	obj.Images			= data.Images
	obj.Comments		= data.Comments
	obj.URL				= path
	
	res.Header().Set("Content-Type","text/html")
	blogT.Execute(res,obj)
}

func postComment(res http.ResponseWriter, req *http.Request){
	obj, _ := retrieveBlogData(req,req.FormValue("user"))
	obj.Comments = append(obj.Comments,req.FormValue("comment"))
	storeBlogData(obj,req.FormValue("user"),req)
}