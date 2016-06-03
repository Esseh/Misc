#ifndef FUNCTION_LIB_H
#define FUNCTION_LIB_H

//required headers
#include "Entity.h"
#include "SFML/Graphics.hpp"

//prefer a const variable over a preprocessor define.
//#define float _PI = 3.14159265;
const float _PI = 3.14159265.f;

//member functions
float DistanceBetween(float px1, float py1, float px2, float py2);
float DistanceBetween(Entity* pEntity1, Entity* pEntity2);
float ToDegrees(float radians);
float ToRadians(float degrees);
float DirectionToPoint(float ax, float ay, float bx, float by); //returns in radians the angle from a(x, y) to b(x, y)
float DirectionToPoint(Entity* a, Entity* b);                   //returns in radians the angle from a to b

std::vector<sf::Vector2f> GenerateBoxFromSprite(sf::Sprite pSprite);
std::vector<sf::Vector2f> GenerateBoxFromDimentions(float px, float py, float width, float height);

#endif // FUNCTION_LIB_H
