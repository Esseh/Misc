#include<unordered_map>

float PowerUpSpeed = 1;

typedef void (*powerUpPair)(GameObject*,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool);                                  //Type definition of a subroutine pointer that takes in a GameObject.

//A powerup object.
struct GamePowerup:GameObject{
    GamePowerup(string);
	void simulate();
	pair<string,pair<powerUpPair,powerUpPair> > effects;
};



static unordered_map<string, pair<powerUpPair,powerUpPair> > powerUpMap;    //This holds our powerup functions.
