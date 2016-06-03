#include "Level_Entity_Manager.h"

LevelEntityManager::LevelEntityManager()
{

}

LevelEntityManager::~LevelEntityManager()
{

}

void LevelEntityManager::Update(KeyState pKeyState)
{
    mFrameTime = mFrameClock.restart().asSeconds();

    sf::Vector2f NewPlayerPos = GetPlayerNewPosition(mPlayer, pKeyState);
    sf::Vector2f NewPlayerSpritePos = sf::Vector2f(NewPlayerPos.x - mPlayer.GetSprite().getOrigin().x, NewPlayerPos.y - mPlayer.GetSprite().getOrigin().y);

    mPlayer.SetDiretion(ToDegrees(DirectionToPoint(mPlayer.GetPosX(), mPlayer.GetPosY(), sf::Mouse::getPosition(*mpTarget).x, sf::Mouse::getPosition(*mpTarget).y)));
    mPlayer.Update(mFrameTime, pKeyState, CheckTileSolidColision(GenerateBoxFromDimentions(NewPlayerSpritePos.x, NewPlayerSpritePos.y, mPlayer.GetTexture().getSize().x, mPlayer.GetTexture().getSize().y)));
}

sf::Vector2f LevelEntityManager::GetPlayerNewPosition(PlayerCharacter pPlayer, KeyState pKeyState)
{
    float NewPlayerX = pPlayer.GetPosX();
    float NewPlayerY = pPlayer.GetPosY();

    if (pKeyState.UpPressed)
        NewPlayerY -= pPlayer.GetSpeed() * mFrameTime;
    if (pKeyState.DownPressed)
        NewPlayerY += pPlayer.GetSpeed() * mFrameTime;
    if (pKeyState.LeftPressed)
        NewPlayerX -= pPlayer.GetSpeed() * mFrameTime;
    if (pKeyState.RightPressed)
        NewPlayerX += pPlayer.GetSpeed() * mFrameTime;

    sf::Vector2f NewPlayerPos(NewPlayerX, NewPlayerY);

    return NewPlayerPos;
}

void LevelEntityManager::Render()
{
    mTileEngine.Render(mpTarget);   //Order of rendering here is important!
    mPlayer.Render(mpTarget);
}

bool LevelEntityManager::CheckTileSolidColision(std::vector<sf::Vector2f> CornerPoints)
{
    for (int i = 0; i < CornerPoints.size(); i++)
    {
        if (mTileEngine.CheckSolid(CornerPoints[i].x, CornerPoints[i].y))
            return true;
    }

    return false;
}
