Clock deltaClock;       //Used for dt, don't touch.
float dt;               //The time that has passed between loops.
bool dead_flag = false; //Do not touch this please.
bool inControl = true;
Clock timeKeeper;
int elapsedtkTime = 0;

Event event;            //event for polling.
RenderWindow window;    //window for WINDOW!
GameObject*playerSprite;
GameObject*player;              //The player object, also belongs to allies.
list<GameObject*>backgrounds;   //Background objects are draw first.
list<GameObject*>allies;        //Player Aligned Objects
list<GameObject*>enemies;       //Enemy Aligned Objects
list<GameObject*>objects;       //Neutral Objects
GameObject* pause;

//Random Number Generators. Their seeds are handled by the configuration file.
InvertableMap screenSeeds(BackgroundSeed);
InvertableMap enemySeeds(EnemySeed);
InvertableMap enemyGeneratorA(EnemyProbA);
InvertableMap enemyGeneratorB(EnemyProbB);
InvertableMap projectiles(3);
