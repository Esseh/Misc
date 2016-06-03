#include "Projectile.h"

struct GamePlayer:GameObject{
    int health;
    bool moveUp,moveLeft,moveDown,moveRight;
    float vx,vy;
    #define P_HEALTH 5
    GamePlayer(){health = P_HEALTH; moveUp = moveLeft = moveDown = moveRight = false; vx = vy = 0; s.setOrigin(0,0); s.setPosition(0,0);}
    void simulate(){playerMovement(); collision(); shoot(); if(health <= 0){selfTerminate();}}
    void events(){playerInput(); shootInput();}
    void playerMovement(){
        vx = vy = 0;
        #define P_VELOCITY 0.0005
        vx = dt*P_VELOCITY*(moveRight - moveLeft);
        vy = dt*P_VELOCITY*(moveDown - moveUp);
        //Collision
        if(s.getPosition().x < 0){vx=abs(vx);}
        if(s.getPosition().y > window.getSize().y - s.getGlobalBounds().height){vy = -abs(vy);}
        if(s.getPosition().y < 0){vy=abs(vy);}
        if(s.getPosition().x > window.getSize().x - s.getGlobalBounds().width){vx = -abs(vx);}
        s.move(vx,vy);
    }
    void playerInput(){
        if(PressKey("Up")     || PressKey("W"))
			moveUp    = true;
		if(PressKey("Right")  || PressKey("D"))
			moveRight = true;
		if(PressKey("Left")   || PressKey("A"))
			moveLeft  = true;
		if(PressKey("Down")   || PressKey("S"))
			moveDown  = true;
		if(ReleaseKey("Up")   || ReleaseKey("W"))
			moveUp    = false;
		if(ReleaseKey("Right")|| ReleaseKey("D"))
			moveRight = false;
		if(ReleaseKey("Left") || ReleaseKey("A"))
			moveLeft  = false;
		if(ReleaseKey("Down") || ReleaseKey("S"))
			moveDown  = false;
    }
    void shootInput(){}                     ///INCOMPLETE - BRIAN
    void shoot(){}                          ///INCOMPLETE - BRIAN
    void collision(){}                      ///INCOMPLETE - BRIAN
};

struct GameStage:GameObject{
    void simulate(){spawnRandomEnemy();}
    void draw(){return;}
    void spawnRandomEnemy(){}               ///INCOMPLETE - KENNETH
};

struct FriendlyBullet:Projectile{
    FriendlyBullet()                        ///IN-PROGRESS - DAVIS
    {

    }

    void movement()                        ///IN-PROGRESS - DAVIS
    {
        sf::Vector2f movement(0.f, 0.f);
        movement.y -= _velocity;
        GetSprite().move(movement * elapsedTime);
    }

    void collide(){                         ///IN-PROGRESS - DAVIS
    //check for collision with enemies.
	for each (auto item in Game::GetGameObjectManager().GetAll())
	{
		BasicEnemy* enemy = dynamic_cast<BasicEnemy*>(item.second);
		if (enemy != NULL)
		{
			if (enemy->GetBoundingRect().contains(GetSprite().getPosition()))
			{
				Game::GetGameObjectManager().Remove(item.first);
				shouldDestroy = true;
			}
		}
	}

    bool Projectile::Destroy()
    {
        return shouldDestroy;
    }
    }

    void simulate(){movement(); collide();}
};

struct EnemyBullet:Projectile{
    EnemyBullet()                           ///IN-PROGRESS - DAVIS
    {

    }

    void movement()                         ///IN-PROGRESS - DAVIS
    {
        sf::Vector2f movement(0.f, 0.f);
        movement.y += _velocity;
        GetSprite().move(movement * elapsedTime);
    }

    void collide()                          ///IN-PROGRESS - DAVIS
    {
    //check for collision with player.
	Player *player = dynamic_cast<Player*>(Game::GetGameObjectManager().Get("player"));
	if (player != NULL)
	{
		if (!player->IsPlayerHit() && player->GetBoundingRect().contains(GetSprite().getPosition()))
		{
			std::cout << "You got hit!" << std::endl;

			player->HitPlayer();
		}
	}
    }

    void simulate(){movement(); collide();}
};

struct GameEnemy:GameObject{
    GameEnemy(){}                                   ///INCOMPLETE - KENNETH
    void simulate(){movement(); shoot(); collide();}
    void movement(){}                               ///INCOMPLETE - KENNETH
    void shoot(){}                                  ///INCOMPLETE - KENNETH
    void collide(){}                                ///INCOMPLETE - KENNETH
};

