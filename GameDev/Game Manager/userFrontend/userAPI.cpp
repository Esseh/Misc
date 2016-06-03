All inline C++ is allowed except in class containers which uses (surprise) C++ class syntax!
In addition, everything in the SFML library can be explicitly called.

By default unordered_map, list, and vector are all available.

Additional Documentation to make your life easier..

///======================================================================================
///======================================================================================
///======================================================================================
//The module that controls the game flow.
GameManager::
    int currentScene;       //Changing this value will dispose of the current scene and load the new one.
    RenderWindow window;    //You can use this to capture window properties if needed. (Refer to SFML RenderWindow)
    Event event;            //You can use this to capture event properties if needed. (Refer to SFML Event)
///======================================================================================
///======================================================================================
///======================================================================================
//Graphics Module
G::
//Vector is used for spatial locality, this allows faster access for resources that are persistent.
    vector<pair<int,GameObject*> >highSpeedGraphics;
//List is used for objects that need to be added/removed quickly as the cost of doing so would be high in vector.
//Unfortunately this means a loss of speed due to a lack of spatial locality.
    list<pair<int,GameObject*> >lowSpeedGraphics;
///WARNING** Deletes all current graphics and textures. Automatically called in scene disposals.
    clear();
///updates all graphic objects in containers. Automatically called in scene updates.
    void updateAll();
///This checks against a filename in order to assign a sprite automatically to an object.
///It performs the checks to make sure textures are being used efficiently. Furthermore the sprite will be marked with a numerical id.
///Please use this instead of direct assignment.
	template<typename T>
    void addSpriteFast(int,string,Sprite,T);
	template<typename T>
    void addSpriteSlow(int,string,Sprite,T);
///Searches the containers to find an entry with the relevant id for when direct modification is ABSOLUTELY necessary and you don't have a better way.
    GameObject* getSprite(int);
///======================================================================================
///======================================================================================
///======================================================================================
Intializing and Disposing
///Declares the intialization of a scene giving the scene an id 'n'.
///Needs a matching event/update also with id 'n'
    makeInit(n)
    ///You can insert inline C++ here.
    makeDispose     //Automatically clears container graphics.
    ///You can insert inline c++ here.
    endID
Eventing and Updating
///Declares the event and update cycles for an scene of id 'n'
    makeEvent(n)            //Automatically Checks for Window Closure
    ///You can insert inline C++ here.
    makeUpdate              //Automatically updates container graphics.
    ///You can insert inline C++ here.
    end
///======================================================================================
///======================================================================================
///======================================================================================
///NEW FEATURES WILL BE ADDED UPON REQUEST
