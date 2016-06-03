/*
    Enemy Peon appears at random then travels randomly shooting at intervals.
*/

int   PlayerHelperLife  = 20;
float PlayerHelperSize  = 1;
float PlayerHelperSpeed = 1;
int   PlayerHelperDamage= 2;
float PlayerHelperExplosionSize   = 1.0010;
int   PlayerHelperExplosionDamage = 5;
int   PlayerHelperFrequency       = 1000000;

struct PlayerHelper:GameObject{
    powerUpPair movementPattern;
	PlayerHelper(GamePlayer*);
	GamePlayer*master;
	vector<int>metaInt;
	vector<float>metaFloat;
	vector<bool>metaBool;
	~PlayerHelper();
	float anchor_x, anchor_y;
	void modVelocity();
    void simulate();
    void movement();
    void shoot();
    void collide();
    void apply();
};
