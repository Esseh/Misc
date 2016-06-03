#include "Function_Lib.h"

float DistanceBetween(float px1, float py1, float px2, float py2)
{
    float DiffX = px1 - px2;
    float DiffY = py1 - py2;

    float DistSqr = DiffX * DiffX + DiffY * DiffY;

    return sqrt(DistSqr);
}

float DistanceBetween(Entity* pEntity1, Entity* pEntity2)
{
    float DiffX = pEntity1->GetPosX() - pEntity2->GetPosX();
    float DiffY = pEntity1->GetPosY() - pEntity2->GetPosY();

    float DistSqr = DiffX * DiffX + DiffY * DiffY;

    return sqrt(DistSqr);
}

float ToDegrees(float radians)
{
    return radians * (180 / _PI);
}

float ToRadians(float degrees)
{
    return degrees * (_PI / 180.0f);
}

float DirectionToPoint(float ax, float ay, float bx, float by)
{
    float DiffX = bx - ax;
    float DiffY = by - ay;

    return atan2(DiffY, DiffX);
}

float DirectionToPoint(Entity* a, Entity* b)
{
    float DiffX = b->GetPosX() - a->GetPosX();
    float DiffY = b->GetPosY() - a->GetPosY();

    return atan2(DiffY, DiffX);
}

std::vector<sf::Vector2f> GenerateBoxFromSprite(sf::Sprite pSprite)
{
    sf::Vector2f P1((pSprite.getPosition().x - pSprite.getOrigin().x), (pSprite.getPosition().y - pSprite.getOrigin().y)); //Top right corner
    sf::Vector2f P2((pSprite.getPosition().x + pSprite.getOrigin().x), (pSprite.getPosition().y - pSprite.getOrigin().y)); //Top left
    sf::Vector2f P3((pSprite.getPosition().x - pSprite.getOrigin().x), (pSprite.getPosition().y + pSprite.getOrigin().y)); //Bottom Right
    sf::Vector2f P4((pSprite.getPosition().x + pSprite.getOrigin().x), (pSprite.getPosition().y + pSprite.getOrigin().y)); //Bottom left

    std::vector<sf::Vector2f> CornerPoints;

    CornerPoints.push_back(P1);
    CornerPoints.push_back(P2);
    CornerPoints.push_back(P3);
    CornerPoints.push_back(P4);

    return CornerPoints;
}

std::vector<sf::Vector2f> GenerateBoxFromDimentions(float px, float py, float width, float height)
{
    sf::Vector2f P1(px, py); //Top right corner
    sf::Vector2f P2(px + width, py); //Top left
    sf::Vector2f P3(px, py + height); //Bottom Right
    sf::Vector2f P4(px + width, py + height); //Bottom left

    std::vector<sf::Vector2f> CornerPoints;

    CornerPoints.push_back(P1);
    CornerPoints.push_back(P2);
    CornerPoints.push_back(P3);
    CornerPoints.push_back(P4);

    return CornerPoints;
}
