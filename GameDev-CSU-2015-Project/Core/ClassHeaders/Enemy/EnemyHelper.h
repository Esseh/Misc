/*
    Enemy Peon appears at random then travels randomly shooting at intervals.
*/

int   EnemyHelperLife  = 2;
float EnemyHelperSize  = 1;
float EnemyHelperSpeed = 1;
int   EnemyHelperDamage= 2;
float EnemyHelperExplosionSize   = 1.0010;
int   EnemyHelperExplosionDamage = 5;
int   EnemyHelperFrequency       = 1000000;

struct EnemyHelper:GameObject{
    powerUpPair movementPattern;
	EnemyHelper(EnemyInstance*);
	EnemyInstance*master;
	vector<int>metaInt;
	vector<float>metaFloat;
	vector<bool>metaBool;
	~EnemyHelper();
	float anchor_x, anchor_y;
	void modVelocity();
    void simulate();
    void movement();
    void shoot();
    void collide();
    void apply();
};
