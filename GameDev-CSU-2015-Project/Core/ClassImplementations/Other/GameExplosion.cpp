/*
    Game Explosion Implementation file.
*/

//When constructed Explosion is in phase one.
GameExplosion::GameExplosion(float exp = 1.0010, int dmg = explosionBaseDamage){
    explosionFactor = exp;
    elapsedTime = 0;
    damage = dmg;
}
void GameExplosion::simulate(){
    elapsedTime += dt;
    //Phase 4 is self termination.
    if(elapsedTime > explosionSpeed*3){
        alive = false;
    }
    //Go to phase 3
    else if(elapsedTime > explosionSpeed*2){
        t.loadFromFile("Resources/Graphics/Explosion3.png");
        s.setTexture(t);
    }
    //Go to phase 2
    else if(elapsedTime > explosionSpeed){
        t.loadFromFile("Resources/Graphics/Explosion2.png");
        s.setTexture(t);
    }
    //Ensure that we are looking at the untrasnformed anchor before transforming.
    s.setOrigin(s.getLocalBounds().width/2,s.getLocalBounds().height/2);
    //Transform.
    s.scale(explosionFactor,explosionFactor);
}
