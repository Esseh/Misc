package main
import "net/http"

func lonelyPage(res http.ResponseWriter,req *http.Request){
	http.ServeFile(res, req, "html/index.html")
}

func main(){
	//Handle css directory.
	http.Handle("/css/",http.StripPrefix("/css",http.FileServer(http.Dir("css"))))
	//Handle pic directory.
	http.Handle("/pic/",http.StripPrefix("/pic",http.FileServer(http.Dir("pic"))))
	//Handle our index.html.
	http.HandleFunc("/",lonelyPage)
	http.ListenAndServe(":8080",nil)
}