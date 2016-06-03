/*
    This is the base GameObject
    It's really messy but basically contains common variables as well as useful helper functions.
*/


///Small Dependency Problem, for this approach to powerups to work PowerUp needs to be made before GameObject.
///This is an exception for our dependency tree.
template<typename T>
struct PowerUp{
    //typedef void (*powerUpPair)(GameObject*);                                  //Type definition of a subroutine pointer that takes in a GameObject.
    PowerUp(pair<string, pair<T, T> > inp){
        metaInt.clear(); metaFloat.clear(); metaBool.clear();
        name = inp.first; first = inp.second.first; second = inp.second.second;
    }
    vector<int>   metaInt;
    vector<float> metaFloat;
    vector<bool>  metaBool;
    string name;
    T first,second;
};



struct GameObject{
	Sprite s;                       // Sprite to display.
	string isPlayer;
	Texture t,compositeTexture;                      // Texture to map to sprite
	bool alive,appearing;           // First flag verifies if the object is living. The second is related to fadeIn()
    float vx,vy;                    // Velocity
    int elapsedTime, life, invuln, damage; //Respectively... total dt so far, current health, current invulnurability timer, damage inflicted through collision
    InvertableMap *generator;       //Random number generator.
    typedef void (*powerUpPair)(GameObject*,string, vector<int>&, vector<float>&, vector<bool>&);     //Type definition of a subroutine pointer that takes in a GameObject.
    list<PowerUp<powerUpPair> > effects; //Holds onto the power up pairs.
	GameObject();                   //Constructor
	virtual void draw();            //Draws the Sprite
	virtual void simulate();        //Simulates the Object
	virtual void events();          //Polls Events from the Object
	void fadeIn();                  //fades the sprite in. if in "if(appearing)"
	void dieIfOutOfBounds();        //What is says on the tin.
	void stayInBounds();            //Instead of dying keeps the object from leaving the screen.
	void invincibility();           //Handles the invincibility timer.
	void takeDamage(int);              //Object is damage and gains some short invincibility.
	//Handles the possibility of taking damage as well as death. In addition it will construct an explosion at pos, allied to c with a size mag and damage dmg.
    void damageHandling(Vector2f pos,list<GameObject*> &c,float mag, int dmg, int damageTaken);
    //Spawns on the edge of the screen.
	void spawnEdge();
	//Spawns at random
	void spawnRandom();
};
