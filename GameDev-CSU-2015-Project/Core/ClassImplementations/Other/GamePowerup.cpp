/*
    An abstracted powerup.
*/

GamePowerup::GamePowerup(string type = ""){
    effects = *(powerUpMap.find(type));
    t.loadFromFile("Resources/Graphics/"+ type + ".png");
    s.setTexture(t);
    objects.push_front(this);

}

void GamePowerup::simulate(){
	s.move((-0.00005*dt)*PowerUpSpeed,0);
	if(s.getPosition().x < 0 - s.getGlobalBounds().width)                                                alive = false;
	if(s.getGlobalBounds().intersects(player->s.getGlobalBounds())){player->effects.push_front(effects); alive = false;} //Grant the power up to the player.
}



/*
    Put in power up entries here.
*/
#include<cmath>

float dist(Vector2f a, Vector2f b){
    return sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
}

void initializePowerUpMap(){
    /**
        homingShot
        sizeUp
        mimeHelper
        sizeDown
        growingShot
        speedUp
        slowShot
        fastShot
        planetaryShot
        pausingShot

    **/
    // homing shots
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("homingShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part

            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                if(dynamic_cast<Bullet*>(projectile)->ally == "enemies"){
                    Vector2f bulletPos = projectile->s.getPosition();
                        if(enemies.size() > 0){
                            Vector2f enemyPos = (*(enemies.begin()))->s.getPosition();
                            Vector2f result = enemyPos - bulletPos;
                            result = result/dist(bulletPos,enemyPos);
                            // Scale the normalized vector by the magnitude of our velocity vector. (sqrt(vx^2+vy^2))
                            double d = (sqrt(pow(projectile->vx,2)+pow(projectile->vy,2)));
                            float r = d;
                            result = result*r;
                            projectile->vx=result.x;
                            projectile->vy=result.y;
                        }
                }
                else{
                    Vector2f bulletPos = projectile->s.getPosition();
                        if(enemies.size() > 0){
                            Vector2f enemyPos = player->s.getPosition();
                            Vector2f result = enemyPos - bulletPos;
                            result = result/dist(bulletPos,enemyPos);
                            // Scale the normalized vector by the magnitude of our velocity vector. (sqrt(vx^2+vy^2))
                            double d = (sqrt(pow(projectile->vx,2)+pow(projectile->vy,2)));
                            float r = d;
                            result = result*r;
                            projectile->vx=result.x;
                            projectile->vy=result.y;
                        }
                }
            }
        )));

    // Increases Ship Size, Increases Health upon pickup.
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("sizeUp",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
                static bool b = true;
                if(b){
                    character->life += 5;
                    b = false;
                }
                character->s.scale(1.5,1.5);
            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part

            }
        )));

    // Mime Helper
    // USES METABOOL 0
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("mimeHelper",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            if(metaBool.size() < 1){metaBool.resize(1,false);}
            if(!metaBool[0]){
                if(character->isPlayer == "true"){
                    GameObject*newph = new PlayerHelper(dynamic_cast<GamePlayer*>(character));
                    allies.push_front(newph);
                }
                else{
                  GameObject*newph = new EnemyHelper(dynamic_cast<EnemyInstance*>(character));
                  enemies.push_front(newph);
                }
                metaBool[0] = true;
            }
            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part

            }
    )));

    // Decreases ship size, halves health upon pickup.
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("sizeDown",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
                static bool b = true;
                if(b){
                    character->life /= 2;
                    b = false;
                }
                character->s.scale(0.5,0.5);
            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part

            }
        )));


    //Causes bullets to gradually scale up in size as they're shot.
    //USES METAFLOAT 0
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("growingShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part

            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                Bullet* source = dynamic_cast<Bullet*>(projectile);
                if(metaFloat.size() < 1){metaFloat.push_back(1.0000);}
                    metaFloat[0]+=0.0040;
                if(projectile->s.getScale().x < 4)
                    source->s.setScale(metaFloat[0],metaFloat[0]);
            }
        )));

    //Slows down bullets.
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("slowShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part

            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                Bullet* source = dynamic_cast<Bullet*>(projectile);
                source->vx /= 2;
            }
        )));


    // Speed Player Up, halves life upon pickup.
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("speedUp",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
                static bool b = true;
                if(b){
                    character->life /= 2;
                    b = false;
                }
                if(character->isPlayer == "true"){
                    playerSpeed *= 1.5;
                }
                else{
                    character->vy*=1.5;
                    character->vx*=1.5;
                }
            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part

            }
        )));


    //Speeds up bullets.
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("fastShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part

            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                Bullet* source = dynamic_cast<Bullet*>(projectile);
                source->vx *= 2;
            }
        )));



    //Causes bullets to periodically pause as they move.
    // USES META FLOATS 1 and 2
    // USES METAINT 0
    // USES META BOOL 1
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("pausingShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part

            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                Bullet* source = dynamic_cast<Bullet*>(projectile);
                if(metaBool.size() < 2){
                    metaBool.resize(2,false);
                }
                if(!metaBool[1]){
                    if(metaFloat.size() < 3){
                        metaFloat.resize(3,0);

                    }
                    metaFloat.at(1) = (source->originalvx); // metaFloat[1]
                    metaFloat.at(2) = (source->originalvy); // metaFloat[2]
                    if(metaInt.size() < 1){
                        metaInt.resize(1,0);
                    }
                }
                if(metaInt[0] > 200000){
                    source->originalvx = 0;
                    source->originalvy = 0;
                }
                if(metaInt[0] > 400000){
                    source->originalvx = metaFloat[1];
                    source->originalvy = metaFloat[2];
                    metaInt[0] = 0;
                }
                metaInt[0] += dt;
            }
        )));


    //Causes bullets to wrap around the screen and continue forward at a random starting location.
    //Additionally adds a lifetime for the bullet of 2 seconds..
    // USES METAINT 1
    powerUpMap.insert(pair<string, pair<powerUpPair, powerUpPair> >("planetaryShot",pair<powerUpPair,powerUpPair>(
            [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            }
            ,
            [](GameObject*projectile,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){         //Projectile Part
                Bullet* source = dynamic_cast<Bullet*>(projectile);


               	if(metaInt.size() < 2){
                    metaInt.resize(2,0);
               	}
               	metaInt[1]+= dt;
                if(metaInt[1] >= 2000000){
                    source->alive = false;
                }
               	if(projectile->s.getPosition().x > window.getSize().x + projectile->s.getGlobalBounds().width / 2)
                    projectile->s.setPosition(0, projectiles.rand() % 512);
                if(projectile->s.getPosition().x < 0 - projectile->s.getGlobalBounds().width / 2)
                    projectile->s.setPosition(512, projectiles.rand() % 512);
                if(projectile->s.getPosition().y > window.getSize().y + projectile->s.getGlobalBounds().height / 2)
                    projectile->s.setPosition(projectiles.rand() % 512, 0);
                if(projectile->s.getPosition().y < 0 - projectile->s.getGlobalBounds().height / 2)
                    projectile->s.setPosition(projectiles.rand() % 512, 512);

            }
        )));

    // USED METAFLOAT 0:2
    // USED METAINT   0:1
    // USED METABOOL  0:1
}
