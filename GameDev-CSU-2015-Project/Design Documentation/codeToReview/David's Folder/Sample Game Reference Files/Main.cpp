#include "Player.h"
#include "Function_Lib.h"
#include "Tile_Engine.h"
#include "Level_Entity_Manager.h"

#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

void PollEvent();
void Render();
void Update();
void GenerateTestLevel();

unsigned int const MapWidth = 20;
unsigned int const MapHeight = 20;

sf::ContextSettings settings;
sf::RenderWindow window;
LevelEntityManager TestLevel;
KeyState KeysPressed;

int main()
{
    srand (time(NULL));

    settings.antialiasingLevel = 8;
    window.create(sf::VideoMode(sf::VideoMode::getDesktopMode().width, sf::VideoMode::getDesktopMode().height), "Heist", sf::Style::Default, settings);

    GenerateTestLevel();

    PlayerCharacter MyPlayer(512, 512, 150, 100);
    TileEngine MyEngine;
    sf::Texture MyTexture;
    sf::Texture TileSet;

    MyTexture.loadFromFile("PlaceHolderPlayer.png");
    TileSet.loadFromFile("TileSet.png");

    MyPlayer.SetTexture(MyTexture);
    MyPlayer.SetWeapon(GetWeaponStat(SMGWeapon));

    std::vector<std::vector<int> > TileIDVec;
    std::vector<std::vector<bool> > SolidStateVec;

    for (unsigned int i = 0; i < MapHeight; i++)
    {
        std::vector<bool> boolRow;
        std::vector<int> intRow;

        for (unsigned int j = 0; j < MapWidth; j++)
        {
            intRow.push_back(rand() % 10);   //random between 0 and 0 (always 0) and then +1 to always be 1

            if (intRow[j] > 1)
                intRow[j] = 1;

            if (intRow[j] == 0)
                boolRow.push_back(true);       //random between 0 and 0
            else
                boolRow.push_back(false);
        }

        SolidStateVec.push_back(boolRow);
        TileIDVec.push_back(intRow);
    }

    MyEngine.LoadFromParam(32, 32, MapWidth, MapHeight, TileSet, TileIDVec, SolidStateVec, 64, 64);

    TestLevel.SetPlayer(MyPlayer);
    TestLevel.SetTileEngine(MyEngine);
    TestLevel.SetTarget(&window);

    while (window.isOpen())
    {
        PollEvent();
        Render();
    }
}

void GenerateTestLevel()
{

}

void PollEvent()
{
    sf::Event event;

    while (window.pollEvent(event))
    {
        if (event.type == sf::Event::Closed)
            window.close();
    }

    Update();
}

void Update()
{
    KeysPressed.LMBPressed = sf::Mouse::isButtonPressed(sf::Mouse::Left);
    KeysPressed.LeftPressed = sf::Keyboard::isKeyPressed(sf::Keyboard::A);
    KeysPressed.RightPressed = sf::Keyboard::isKeyPressed(sf::Keyboard::D);
    KeysPressed.UpPressed = sf::Keyboard::isKeyPressed(sf::Keyboard::W);
    KeysPressed.DownPressed = sf::Keyboard::isKeyPressed(sf::Keyboard::S);

    TestLevel.Update(KeysPressed);
}

void Render()
{
    window.clear();
    TestLevel.Render();
    window.display();
}
