package main
import (
	"net/http"
	"appengine"
	"appengine/datastore"
	"appengine/memcache"
	"encoding/json"
)

type User struct{
	Uuid string
	Password string
	Email string
}


type Emails struct{
	Values []string
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