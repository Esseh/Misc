/*
    Game Explosion controls the explosion effects that occur throughout the game.
    It's only variable is passed in which will determine the size of an explosion.
*/

//Change this to change the default explosion damage.
#define explosionBaseDamage 3
//Change this to change how quick an explosion occurs.
//A smaller number results in a quicker explosion.
#define explosionSpeed 125000

struct GameExplosion:GameObject{
    float explosionFactor;          //The intensity of the explosion.
    GameExplosion(float,int);
    void simulate();
};
