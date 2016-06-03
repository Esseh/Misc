/*
    EnemyBullet Header File
    This controls the behaviors of the normal bullets shot by the enemy.
*/

int   BulletDamage = 2;
float BulletSpeed  = 1;
float BulletSize   = 1;
float BulletExplosionSize  =1.0010;
int   BulletExplosionDamage=2;

struct Bullet:GameObject{
    string ally;
    Bullet(float curr_x, float curr_y, string alliance, list<PowerUp<powerUpPair> > pwp, string bounce);
    string riccochet;
    Vector2f originalScale;
    float originalvx, originalvy;
    void simulate();
    void movement();
    void collide();
    void apply();
};
