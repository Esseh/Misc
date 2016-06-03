#ifndef WEAPONS_H_INCLUDED
#define WEAPONS_H_INCLUDED

#include <SFML/Graphics.hpp>

struct Weapons
{
    float mDamage;
    float mBulletSpeed;
    float mFireRate;
    float mBulletSpred;
    sf::Texture mBulletTexture;
};

enum WeaponTypes
{
    Weapon1,
    Weapon2,
    Weapon3,
};

Weapons GetWeapons(WeaponTypes WeaponID);


#endif // WEAPONS_H_INCLUDED
