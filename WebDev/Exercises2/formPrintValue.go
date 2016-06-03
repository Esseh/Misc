/*==============================================================
 "Create a webpage that displays the text in an uploaded file
 Kenneth Willeford
	prints to stdout with res as the writer. 
==============================================================*/
package main
import (
		"net/http"
		"io"
		"fmt"
)

func lonelyPage(res http.ResponseWriter,req *http.Request){
	fmt.Fprint(res,`<!DOCTYPE html>
				<html>
				<head>
					<title></title>
				</head>
					<body>
					<form method = "POST"  enctype="multipart/form-data">
						<input type="file" name="name"><br>
						<input type="submit">
					</form>
				</body>
				</html>`)
	if req.Method == "POST"{
		key := "name"
		_, hdr, err2 := req.FormFile(key)
		if err2 != nil{
			fmt.Println(err2)
		}
		
		rdr, err := hdr.Open()
		if err != nil{
			fmt.Println(err)
		}
		io.Copy(res,rdr)		
	}
}

func main(){
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}