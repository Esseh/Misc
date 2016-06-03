/*
	This file is responsible for defining the user data that will be utilized in templates and cookies.
*/
package main

//Basic Struct that holds the username.
type User struct{
	Uuid,Name,Age,LoggedIn string
}