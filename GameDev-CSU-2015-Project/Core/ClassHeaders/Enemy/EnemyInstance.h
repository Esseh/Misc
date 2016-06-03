/*
    Enemy Peon appears at random then travels randomly shooting at intervals.
*/

int   EnemyInstanceLife  = 3;
float EnemyInstanceSize  = 1;
float EnemyInstanceSpeed = 1;
int   EnemyInstanceDamage= 2;
float EnemyInstanceExplosionSize   = 1.0010;
int   EnemyInstanceExplosionDamage = 1;
int   EnemyInstanceFrequency       = 1000000;

unordered_map<string,powerUpPair>enemyMap;

struct EnemyInstance:GameObject{
    powerUpPair movementPattern;
	EnemyInstance(string,list<PowerUp<powerUpPair> >,string,string);
	string sizeClass;
	vector<int>metaInt;
	vector<float>metaFloat;
	vector<bool>metaBool;
	~EnemyInstance();
	void modVelocity();
    void simulate();
    void movement();
    void shoot();
    void collide();
    void apply();
};
