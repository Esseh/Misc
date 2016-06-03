#include "Weapons.h"

Weapons GetWeapons(WeaponTypes WeaponID)
{
    Weapons WeaponIDStats;
    sf::Texture WeaponIDTexture;

    switch (WeaponID)
    {
        case Weapon1:
            WeaponIDTexture.loadFromFile("Bullet.png");
            WeaponIDStats.mBulletSpeed = 25;
            WeaponIDStats.mDamage = 10;
            WeaponIDStats.mFireRate = 0.1;
            WeaponIDStats.mBulletSpred = 2;
            break;
        case Weapon2:
            WeaponIDTexture.loadFromFile("Bullet.png");
            WeaponIDStats.mBulletSpeed = 20;
            WeaponIDStats.mDamage = 7;
            WeaponIDStats.mFireRate = 0.05;
            WeaponIDStats.mBulletSpred = 1;
            break;
        case Weapon3:
            WeaponIDTexture.loadFromFile("Bullet.png");
            WeaponIDStats.mBulletSpeed = 20;
            WeaponIDStats.mDamage = 20;
            WeaponIDStats.mFireRate = 2;
            WeaponIDStats.mBulletSpred = 5;
            break;
        default:
            break;
    }

    WeaponIDStats.mBulletTexture = WeaponIDTexture;

    return WeaponIDStats;
}
