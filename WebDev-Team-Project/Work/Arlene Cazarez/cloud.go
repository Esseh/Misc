package main

import (
	"strings"
	"fmt"
	"io"
	"net/http"
	"google.golang.org/appengine"
	"google.golang.org/cloud/storage"
	"mime/multipart"
	"crypto/sha256"
)
var bucket = "essys-bucket"


func createFileGCS(req *http.Request, file multipart.File,res http.ResponseWriter) error {
	// Get the cookie for datastore consistency.
	cookie, cookieerr := req.Cookie("session-info")
	// If something went wrong escape.
	if cookieerr != nil { return cookieerr }
	// Grab the username from the cookie.
	username := (strings.Split(cookie.Value,","))[1]
	// Get the blog data.
	data, dataerr := retrieveBlogData(req, username)
	if dataerr != nil {
		//If something went wrong escape.
		return dataerr
	}

	// Make Context
	ctx := appengine.NewContext(req)

	// Construct Client
	client, cerr := storage.NewClient(ctx)
	// If something went wrong escape.
	if cerr != nil { return cerr }
	// close the client when we're done.
	defer client.Close()


	// Sha the data in order to make a unique url.
	// Incidentally this will also ensure that there are no duplicates.
	// In fact someone else adding it would only add it to their local blog as the references are in their blog data.
	h := sha256.New()
	io.Copy(h,file)
	url := fmt.Sprintf("%x", h.Sum(nil))


	// Sha Move The Reader so we need to move it back.
	file.Seek(0,0)

	// Add image url to list of urls if not already present.
	check := true
	for _, v := range data.Images {
		if v == url + ".png" {
			check = false
			break
		}
	}
	if(check){
		data.Images = append(data.Images, url + ".png")
		// Make datastore consistent with cloud.
		storeerr := storeBlogData(data, username, req)
		if storeerr != nil {
			// If something went wrong then escape.
			return storeerr
		}
	}

	// Test the file's existance first...
	_, readerr := client.Bucket(bucket).Object(url + ".png").NewReader(ctx)
	if readerr == nil {
		fmt.Fprint(res,"The File has Already Been Uploaded. The File is Now Linked to your profiles.")
		return nil
	}

	// Make the Google Cloud Writer
	cloudWriter := client.Bucket(bucket).Object( url + ".png").NewWriter(ctx)
	// Set ACL Rules
	// Cloud Storage Writer - Permissions
	cloudWriter.ACL = []storage.ACLRule{
		{storage.AllUsers, storage.RoleReader},
	}
	// Set our data type.
	cloudWriter.ContentType = "image/jpeg"
	//Writing to the cloud writer.
	io.Copy(cloudWriter,file)
	return cloudWriter.Close()
}


func removeImageFromBlog(res http.ResponseWriter, req *http.Request,url string){
	if(authenticatedUser(req,res)){
		cookie,_ := req.Cookie("session-info")
		username := strings.Split(cookie.Value,",")[1]
		data, err := retrieveBlogData(req, username)
		if err != nil { return }
		memory := -1
		for i,val := range data.Images {
			if val == url{
				memory = i
				break
			}
		}
		if(memory > -1){
			data.Images = append(data.Images[:memory],data.Images[memory+1:]...)
			storeBlogData(data, username , req)
		}
	}
}

func API_removeImage(res http.ResponseWriter, req *http.Request){
	removeImageFromBlog(res, req, req.FormValue("key"))
}