#ifndef PLAYER_H
#define PLAYER_H

#include "Entity.h"
#include "WeaponStats.h"
#include "Projectile.h"
#include <SFML/Graphics.hpp>
#include <vector>

struct  KeyState{
    bool UpPressed;
    bool DownPressed;
    bool LeftPressed;
    bool RightPressed;
    bool LMBPressed;
};

class Player : public Entity
{
public:
    //Constructor and Destructor
    Player();
    Player(float pPosX, float pPosY, float pSpeed = 0, float pHealth = 0);
    Player(float pPosX, float pPosY, sf::Texture pTexture, float pSpeed = 0, float pHealth = 0);
    ~Player();

    //Getters
    float GetSpeed() { return mSpeed; }
    float GetHealth() {return mHealth; }
    sf::Sprite GetSprite() { return mSprite; }
    sf::Texture GetTexture() { return mTexture; }
    float GetDirection() { return mDirection; }
    WeaponStats GetWeapon() { return mWeapon; }
    std::vector<Projectile>& GetProjectiles() { return mProjectiles; }

    //Setters
    void SetSpeed(float val) { mSpeed = val; }
    void SetHealth(float val);
    void SetSprite(sf::Sprite val) { mSprite = val; }
    void SetTexture(sf::Texture val);
    void SetDiretion(float val) { mDirection = val; }
    void SetWeapon(WeaponStats pWeapon) { mWeapon = pWeapon; }
    void SetProjectiles(std::vector<Projectile>& pProjectiles) { mProjectiles = pProjectiles; }

    //Member Functions
    void Render(sf::RenderWindow* pTarget);     //Draw the player sprite and the projectiles
    void Update(float TimeStep, KeyState val, bool WillCollide);  //Update the projectiles positions and the players sprite
    void GenerateProjectile();

private:
    void UpdateProjectiles(float TimeStep);
    void RenderProjectiles(sf::RenderWindow* pTarget);
    void UpdateSprite();
    void Move(KeyState val, float TimeStep);    //Move the player in the pressed directions

    sf::Sprite mSprite;
    sf::Texture mTexture;
    float mSpeed;
    float mHealth;
    float mDirection;
    WeaponStats mWeapon;
    std::vector<Projectile> mProjectiles;
    sf::Clock mWeaponClock;
};

#endif // PLAYER_H
