package main
import (
	"net/http"
	"appengine"
	"appengine/datastore"
	"appengine/memcache"
)
//Retrieves an item from the datastore.
func retrieveFromDatastore(id string, req *http.Request) (Object, error) {
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "User", id, 0, nil)
	var obj Object
	err := datastore.Get(ctx, key, &obj)
	if err != nil{ return Object{} , err }
	return obj , nil
} 


//Stores an item in the datastore.
func storeInDatastore(o Object, id string, req *http.Request) error{
	ctx := appengine.NewContext(req)
	key := datastore.NewKey(ctx, "User", id, 0, nil)
	_, err := datastore.Put(ctx, key, &o)
	if err != nil{ return err }
	return nil
}

//Retrieves an item from Memcache
func retrieveFromMemcache(id string, req *http.Request) (Object, error) {
	ctx    := appengine.NewContext(req)
	i, err := memcache.Get(ctx,id)
	if err != nil{ return Object{}, err }
	obj    := Object{string(i.Value)}
	return obj, nil
}

//Stores an item in Memcache
func storeInMemcache(o Object, id string, req *http.Request) error {
	ctx := appengine.NewContext(req)
	v   := &memcache.Item{Key:id,Value:[]byte(o.Data)}
	err := memcache.Add(ctx, v)
	if err != nil{return err}
	return nil
}