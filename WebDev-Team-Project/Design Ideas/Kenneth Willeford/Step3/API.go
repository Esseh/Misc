package main
import(
	"net/http"
	"fmt"
	"strings"
	"time"
	"appengine"
	"appengine/memcache"
	"github.com/nu7hatch/gouuid"
)

// =========================================================
// This function retrieves the user from datastore with the
// username 'key'
// ========================================================
func retrieveUser(key string ,req *http.Request)(User,error){
	// ===============================================
	// Grab our data from memcache
	// ===============================================
	data, err := retrieveFromMemcache(key, req)
	if err != nil{
		// =====================================
		// Failing that grab it from data store.
		// =====================================
		data, err = retrieveFromDatastore(key,req)
		if err == nil{
			// =================================================
			// If found then place in memcache before continuing.
			// =================================================
			err2 := storeInMemcache(data, key, req)
			if err2 != nil {}
		}
	}
	return data, err
}

// =======================================================================
// This is the handler for "/logout" however it is also a logout API call.
// By redirecting to "/logout" the current user can be logged out.
// Additionally this can be called directly during a request to log the user
// out as it redirects to the main page anyways.
// =======================================================================
func logout(res http.ResponseWriter, req *http.Request){
	cookie,_ := req.Cookie("session-info")
	// ===========================
	// The cookie is already dead.
	// The expiration is set to 
	// Epoch so it is erased.
	// ===========================
	t := time.Now()
	t.Sub(time.Now())
	cookie.Expires = t
	cookie.Path = "/"
	// =======================
	// We Apply the dead cookie.
	// Now their cookie will die
	// as well as their session.
	// ========================
	http.SetCookie(res,cookie)
	//============
	// Reload Page
	//============
	http.Redirect(res, req, "/", http.StatusFound)
}

// =======================================================================
// An API call that checks if a username exists. Meant to be used by AJAX
// through a GET at "/usernameexists"
// The query value of ?username=<CHECK>
// will verify if <CHECK> is being used or not.
// =======================================================================
func userNameExists(res http.ResponseWriter, req *http.Request){
	// ================================
	// No need to check an empty username field.
	// ================================
	if(req.FormValue("username") == ""){
		fmt.Fprint(res,"wut")
		return
	}
	// ===================
	// Get the user
	// ===================
	_, err := retrieveUser(req.FormValue("username") ,req)
	// ======================================
	// Make sure only plain text is sent.
	// ======================================
	res.Header().Set("Content-Type","text/plain")
	if(err != nil){
		// If the user wasn't retrieved say so.
		fmt.Fprint(res ,"doesn't exist")
	} else{ 
		// If the user was retrieved say so.
		fmt.Fprint(res ,"exists")
	}
}


// =======================================================
// This call authenticates if the current user is actually
// who they claim to be. It can be used during any request.
// =======================================================
func authenticatedUser(req *http.Request, res http.ResponseWriter) bool {
	// ================
	// Get the cookie.
	// ===============
	cookie,err := req.Cookie("session-info")
	if err != nil {
		// ====================================
		// If no cookie you don't belong here.
		// ====================================
		http.Redirect(res, req, "/", http.StatusFound)
		return false
	}
	// ======================
	// Parse cookie data
	// ======================
	values := strings.Split(cookie.Value,",")
	// ======================================
	// Get the user
	// ======================================
	data, err := retrieveUser(values[1] ,req)
	if err != nil {
		// If they couldn't be found then they're not legit.
		return false
	}
	// ==========================
	// Make sure they're legit.
	// ==========================
	return data.Uuid == values[0]
}

// =====================================================
//	This call will interrupt the request to change the 
//  user's password to 'input'.
// =====================================================
func changePassword(res http.ResponseWriter, req *http.Request, input string){
	// ============================
	// Get the user session
	// ============================
	cookie, err := req.Cookie("session-info")
	if err != nil{
		// ==================================================
		// This should never happen, but never too careful.
		// ==================================================
		return
	}
	// ======================
	// Parse the cookie value
	// ======================
	values := strings.Split(cookie.Value,",")
	// =============
	// Get the user.
	// =============
	data, err := retrieveUser(values[1] ,req)
	if err != nil { return }
	data.Password = input
	err = storeInDatastore(data, values[1], req) 
	if err != nil {
	
	}
	c := appengine.NewContext(req)
	memcache.Delete(c, values[1])
	err = storeInMemcache(data, values[1], req)
	if err != nil {}
}


func loginRequest(res http.ResponseWriter, req *http.Request){
	// ===================================================
	// Empty username or password? Ignore that nonsense.
	// ===================================================
	if(req.FormValue("username") == "" || req.FormValue("password") == ""){ return }
	// ==============
	// Grab the user.
	// ==============
	data, err := retrieveUser(req.FormValue("username") ,req)
	// ===================================
	// If they weren't found then return.
	// ===================================
	if err != nil { return }
	// =============================
	//HEY YOU ALREADY HAVE A COOKIE
	// =============================
	_, err = req.Cookie("session-id")
	if err == nil {
		fmt.Fprint(res,"stop reaching into the cookie jar!")
	} else {
		// ===================================================
		//Otherwise begin the session if everything is good..
		//Make sure the password is good.
		// ==================================================
		if(data.Password != req.FormValue("password")){
			http.Redirect(res, req, "/login", http.StatusFound)
			return
		} else {
			http.SetCookie(res,&http.Cookie{
				Name: "session-info",
				Value: data.Uuid+","+req.FormValue("username"),
				MaxAge: int((time.Hour).Seconds()),
				Path: "/",
			})			
		}
		http.Redirect(res, req, "/", http.StatusFound)
	}
}

func registerRequest(res http.ResponseWriter, req *http.Request){
	// ==========================================
	//If the username is empty don't even bother.
	// ==========================================
	if(req.FormValue("username") == "" || req.FormValue("password") == "" || req.FormValue("email") == ""){ 
		http.Redirect(res, req, "/register", http.StatusFound)
		return 
	}
	// Grab Emails
	emails, _ := retrieveEmails(req)
	// Iterate through to make sure it doesn't already exist. And if it does be sure to escape.
	for _, i := range emails.Values {
		if i == req.FormValue("email"){
			//Redirect back to register since
			//their information was wrong.
			http.Redirect(res, req, "/register", http.StatusFound)
			return
		}
	}
	// Otherwise Append new email to old emails.
	emails.Values = append(emails.Values,req.FormValue("email"))
	// Store Emails
	eerr := storeEmails(emails,req)
	if eerr != nil{
		// If the email wasn't stored properly quit early.
		return
	}
	// ==============
	// Grab the user.
	// ==============
	data, err := retrieveUser(req.FormValue("username"), req)
	if err != nil {
		// ======================================================
		//Because we didn't find a user we can construct the user.
		// Make a Unique User ID
		// ======================================================
		id,_ := uuid.NewV4()
		var newUser User
		// ==============
		// Place the UUID
		// ==============
		newUser.Uuid = id.String()
		// =========
		// PASSWORD
		// =========
		newUser.Password = req.FormValue("password")	
		// =========
		// EMAIL
		// ==========
		newUser.Email = req.FormValue("email")
		// ================================
		// Store the user in the datastore.
		// ================================
		err := storeInDatastore(newUser, req.FormValue("username"), req)
		if err != nil{
			fmt.Fprint(res,"Problem Making User Datastore",err)
		}
		// ====================
		// Also update memcache
		// =====================
		err2 := storeInMemcache(newUser, req.FormValue("username"), req)
		if err2 != nil{
			fmt.Fprint(res,"Problem Making User Memcache",err2)
		}
		loginRequest(res, req)
	} else {
		// Someone is trying to spoof a request, don't let them do anything.
		// Though we DID access datastore, put it in Memcache since it was found.
		storeInMemcache(data, req.FormValue("username"), req)
		fmt.Fprint(res,"Bad Idea Sir")
		return
	}
	// If it got here it was found in memcache, so someone was spoofing a request.
	return
}