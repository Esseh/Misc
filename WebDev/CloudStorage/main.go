/*
	Utilized the Google Cloud Storage Example/Todd's Example and found the important parts.
	I left out the error handling to make the purpose of the calls easier to realize. 
	Mine is an awful example of how to use it but I think a clear example of how it is used.
*/
package main

import (
		"net/http" 
		"google.golang.org/appengine"
		"google.golang.org/cloud/storage"		
)

func store(res http.ResponseWriter, req *http.Request) {
	//Make Context
	ctx := appengine.NewContext(req)
	//Make Client
	client, _ := storage.NewClient(ctx)
	//Construct Our object to interface with the cloud storage.
	d := &demo{
		w:      res,		//The response writer so it knows what to write to later if retrieving.
		ctx:    ctx,		//Current Context
		client: client,					//Current Client
		bucket: client.Bucket(bucket),	//Relevant Bucket, bucket is a global string that contains the default bucket location.
	}
	//The name of the file we will be creating.
	n := "demo-testfile-go"
	//Create the File and store in google cloud.
	d.createFile(n)
}

func retrieve(res http.ResponseWriter, req *http.Request) {
	ctx := appengine.NewContext(req)
	client, _ := storage.NewClient(ctx)
	d := &demo{
		w:      res,
		ctx:    ctx,
		client: client,
		bucket: client.Bucket(bucket),
	}
	//The name of the file we will be grabbing and reading from.
	n := "demo-testfile-go"
	//Read the file from google cloud.
	d.readFile(n)
}


//Empty base webpage. 
func index(res http.ResponseWriter, req *http.Request) {}

func init(){
	http.HandleFunc("/", index)
	http.HandleFunc("/store", store)
	http.HandleFunc("/retrieve", retrieve)
}