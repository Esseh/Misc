/*
    HeaderFile for GamePlayer
    Affects the controlled player.
*/

int   playerHealth = 9999;
int   playerDamage = 3;
float playerSpeed  = 1;
float playerSize   = 1;

struct GamePlayer:GameObject{
    bool moveUp,moveLeft,moveDown,moveRight, shooting;
    int damageBackup, numberOfPowerups;
    float speedBackup;
    GameObject*metaObject;
    Vector2f scaleBackup;
    GamePlayer();
    ~GamePlayer();
    void simulate();
    void events();
    void playerMovement();
    void playerInput();
    void shootInput();
    void shoot();
    void collide();
    void shootBullet();
    void powerUpCheck();
    void apply();
    void makeTexture();
};
