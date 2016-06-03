#include<unordered_map>     //Unordered Map
#include<vector>            //Unordered Map Container
#include<list>              //Unordered Map Container
#include<SFML/Graphics.hpp> //SFML Graphics Library
#include<iostream>
using namespace sf;         //SFML Game Library
using namespace std;        //STD Standard Library
#include"backend/___nMdT___.gmbe"
#include"userFrontend/user.config"

typedef void (*func)(void);
#include"userDefinitions/userPrototypes.h"          //User Defined Prototypes Go Here
#include"userDefinitions/userClasses.h"             //User Defined Classes Go Here
#include"userDefinitions/userFunctions.h"           //User Defined Functions Go Here

#include"backend/__backendPrototypes__.gmbe"
#include"backend/__backendImplementations__.gmbe"

int main(){GameManager::run(FIRST_SCENE_ID);}
