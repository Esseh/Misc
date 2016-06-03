package main
import (
	"net/http"
	"google.golang.org/appengine"
	"google.golang.org/appengine/datastore"
	"google.golang.org/appengine/memcache"
	"encoding/json"

)

type User struct{
	Uuid string
	Password string
	Email string
}

type BlogData struct{
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
}

type Emails struct{
	Values []string
}

type Pages struct{
	Data []string
}

func retrieveEmails(req *http.Request) (Emails, error) {
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "Email", "Emails", 0, nil)
	var obj Emails
	err := datastore.Get(ctx, key, &obj)
	if err != nil{ return Emails{} , err }
	return obj, nil
}


func storeEmails(o Emails, req *http.Request) error{
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "Email", "Emails", 0, nil)
	_, err := datastore.Put(ctx, key, &o)
	return err
}

func retrievePages(req *http.Request) (Pages, error) {
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "Pages", "Pages", 0, nil)
	var obj Pages
	err := datastore.Get(ctx, key, &obj)
	if err != nil{ return Pages{} , err }
	return obj, nil
}


func storePages(o Pages, req *http.Request) error{
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "Pages", "Pages", 0, nil)
	_, err := datastore.Put(ctx, key, &o)
	return err
}


func retrieveBlogData(req *http.Request, username string) (BlogData, error) {
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "BlogData", username, 0, nil)
	var obj BlogData
	err := datastore.Get(ctx, key, &obj)
	if err != nil{ return BlogData{} , err }
	return obj, nil
}


func storeBlogData(o BlogData, username string , req *http.Request) error{
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "BlogData", username, 0, nil)
	_, err := datastore.Put(ctx, key, &o)
	return err
}


//Retrieves an item from the datastore.
func retrieveFromDatastore(username string, req *http.Request) (User, error) {
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "User", username, 0, nil)
	var obj User
	err := datastore.Get(ctx, key, &obj)
	if err != nil{ return User{} , err }
	return obj, nil
}


//Stores an item in the datastore.
func storeInDatastore(o User, username string, req *http.Request) error{
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "User", username, 0, nil)
	_, err := datastore.Put(ctx, key, &o)
	return err
}

//Retrieves an item from Memcache
func retrieveFromMemcache(username string, req *http.Request) (User, error) {
	ctx    := appengine.NewContext(req)
	i, err := memcache.Get(ctx,username)
	if err != nil{ return User{}, err }
	var obj User
	err = json.Unmarshal(i.Value,&obj)
	return obj, err
}

//Stores an item in Memcache
func storeInMemcache(o User, username string, req *http.Request) error {
	ctx := appengine.NewContext(req)
	b, err := json.Marshal(o)
	if err != nil{ return err }
	v   := &memcache.Item{Key:username,Value:b}
	err = memcache.Add(ctx, v)
	if err != nil{return err}
	return nil
}