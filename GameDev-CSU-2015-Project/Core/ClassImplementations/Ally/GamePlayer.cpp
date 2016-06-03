/*
    Implementation File for GamePlayer
*/

GamePlayer::GamePlayer(){
    damage = playerDamage; life = playerHealth;
    t.loadFromFile("Resources/Graphics/Player.png");
    s.setTexture(t);
    playerSprite = new GameObject();
    objects.push_front(playerSprite);
    metaObject = playerSprite;
    playerSprite->t.loadFromFile("Resources/Graphics/PlayerShip.png");
    playerSprite->s.setTexture(playerSprite->t);
    moveUp = moveLeft = moveDown = moveRight = false;
    vx = vy = 0; s.setPosition(0,0);
    s.scale(playerSize,playerSize); shooting = false;
    damageBackup = damage; scaleBackup = s.getScale(); speedBackup = playerSpeed;
    numberOfPowerups = 0;
    isPlayer = "true";
}
GamePlayer::~GamePlayer(){
    metaObject->alive = false;
    objects.remove_if([](GameObject*i){if(!i->alive){delete i; return true;} return false;});
}
void GamePlayer::simulate(){
    if(life > playerHealth){ life = playerHealth; }
    elapsedTime+=dt;
    if(invuln <= 0) playerSprite->s.setColor(Color(255,255,255,255));
    else playerSprite->s.setColor(Color(255,255,255,invuln % 255));
    playerMovement(); collide(); shoot(); powerUpCheck(); invincibility();
    playerSprite->s.setOrigin(playerSprite->s.getLocalBounds().width/2,playerSprite->s.getLocalBounds().height/2);
    playerSprite->s.setPosition(s.getPosition());
    if(life <= 0) alive = false;
}
void GamePlayer::powerUpCheck(){
    if(numberOfPowerups != effects.size()){
        while(effects.size() > 6) effects.pop_back();
        makeTexture();
        damage = damageBackup; s.setScale(scaleBackup); playerSpeed = speedBackup;
        apply(); numberOfPowerups = effects.size();
    }
    playerSprite->s.setScale(s.getScale());
}
void GamePlayer::makeTexture(){
            Image temp;
            temp.loadFromFile("Resources/Graphics/PlayerShip.png");
            if(effects.size() > 0){
                Image temp2;
                temp2.loadFromFile("Resources/Graphics/" + ((effects.begin())->name) + ".png");
                temp.copy(temp2,58-(temp2.getSize().x/2),9-(temp2.getSize().y/2));
            }
            if(effects.size() > 1){
                Image temp2;
                auto b = effects.begin();
                b++;
                temp2.loadFromFile("Resources/Graphics/" + ((b)->name) + ".png");
                temp.copy(temp2,42-(temp2.getSize().x/2),19-(temp2.getSize().y/2));
            }
            if(effects.size() > 2){
                Image temp2;
                auto b = effects.begin();
                b++; b++;
                temp2.loadFromFile("Resources/Graphics/" + ((b)->name) + ".png");
                temp.copy(temp2,18-(temp2.getSize().x/2),19-(temp2.getSize().y/2));
            }
            if(effects.size() > 3){
                Image temp2;
                auto b = effects.begin();
                b++; b++; b++;
                temp2.loadFromFile("Resources/Graphics/" + ((b)->name) + ".png");
                temp.copy(temp2,30-(temp2.getSize().x/2),17-(temp2.getSize().y/2));
            }
            if(effects.size() > 4){
                Image temp2;
                auto b = effects.begin();
                b++; b++; b++; b++;
                temp2.loadFromFile("Resources/Graphics/" + ((b)->name) + ".png");
                temp.copy(temp2,7-(temp2.getSize().x/2),18-(temp2.getSize().y/2));
            }
            if(effects.size() > 5){
                Image temp2;
                auto b = effects.begin();
                b++; b++; b++; b++; b++;
                temp2.loadFromFile("Resources/Graphics/" + ((b)->name) + ".png");
                temp.copy(temp2,7-(temp2.getSize().x/2),0);
            }
            playerSprite->t.loadFromImage(temp);
            playerSprite->s.setTexture(playerSprite->t);
}
void GamePlayer::events(){ playerInput(); shootInput(); }
void GamePlayer::playerMovement(){
    //Utilizes basic Euler integration in order to control velocity.
	vx = vy = 0;
	#define P_VELOCITY 0.0001875
	vx = dt*P_VELOCITY*(moveRight - moveLeft);
	vy = dt*P_VELOCITY*(moveDown - moveUp);
	//Collision
	stayInBounds();
	s.move(vx*playerSpeed,vy*playerSpeed);
}
void GamePlayer::playerInput(){
   int waitTime = 200000;
   elapsedtkTime += timeKeeper.restart().asMicroseconds();
   if(elapsedtkTime > waitTime){elapsedtkTime = waitTime;}

    //The controller.
    if(inControl){
        if(PressKey("Up")     || PressKey("W"))   moveUp    = true;
        if(PressKey("Right")  || PressKey("D"))   moveRight = true;
        if(PressKey("Left")   || PressKey("A"))   moveLeft  = true;
        if(PressKey("Down")   || PressKey("S"))   moveDown  = true;
        if(ReleaseKey("Up")   || ReleaseKey("W")) moveUp    = false;
        if(ReleaseKey("Right")|| ReleaseKey("D")) moveRight = false;
        if(ReleaseKey("Left") || ReleaseKey("A")) moveLeft  = false;
        if(ReleaseKey("Down") || ReleaseKey("S")) moveDown  = false;
        if(ReleaseKey("F1") && elapsedtkTime >= waitTime){
            inControl = false;
            moveUp = moveRight = moveDown = moveLeft = false;
            pause = new GameObject();
            pause->t.loadFromFile("Resources/Graphics/Paused.png");
            pause->s.setTexture(pause->t);
            objects.push_front(pause);
            elapsedtkTime = 0;
        }

    } else if(!inControl){
        if(ReleaseKey("F1") && elapsedtkTime >= waitTime){
            inControl = true;
            if(Keyboard::isKeyPressed(stringMap("Up"))) moveUp = true;
            if(Keyboard::isKeyPressed(stringMap("Left"))) moveLeft = true;
            if(Keyboard::isKeyPressed(stringMap("Right"))) moveRight = true;
            if(Keyboard::isKeyPressed(stringMap("Down"))) moveDown = true;
            elapsedtkTime = 0;
            pause->alive = false;
        }
    }
}
void GamePlayer::shootInput(){ if(ReleaseKey("Space") && inControl) shooting = true; }
void GamePlayer::shoot(){ if(shooting){ shootBullet(); shooting = false; } }
void GamePlayer::collide(){
    int damage = collision(this,"enemies");
    if(damage){
            damageHandling(s.getPosition(),allies,EnemyInstanceExplosionSize,EnemyInstanceExplosionDamage, damage);
            invuln = 1500000;
    }
}
//Helper method to produce basic bullets.
void GamePlayer::shootBullet(){
    GameObject*newObject = new Bullet(s.getPosition().x+s.getLocalBounds().width,s.getPosition().y+(s.getLocalBounds().height/2),"enemies",effects);
    allies.push_front(newObject);
}
void GamePlayer::apply(){
    for(auto i = effects.begin(); i!=effects.end(); i++) (i->first)(this,i->name,i->metaInt,i->metaFloat,i->metaBool);
}
