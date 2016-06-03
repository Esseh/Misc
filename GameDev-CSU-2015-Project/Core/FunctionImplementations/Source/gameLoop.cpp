void GrabObjectSequence(int scene){
    //MAIN STAGE
    _scene(0) has
        player(GamePlayer)
        //object(GameStage,"Resources/Graphics/empty.png")
        background(proceduralBackground)
        {
            GameObject*t = new GameStage1(7);
            objects.push_front(t);

        }
    _end

    //GAMEOVER
    _scene(2) has
        player(GameOverScreen)
    _end

}

void BackgroundDraws(){
    for(auto i = backgrounds.begin(); i!=backgrounds.end(); i++){(*i)->draw(); (*i)->simulate();}
}

void ObjectDraws(){
    for(auto i = allies.begin(); i!=allies.end(); i++){(*i)->draw();}
    for(auto i = enemies.begin(); i!=enemies.end(); i++){(*i)->draw();}
    for(auto i = objects.begin(); i!=objects.end(); i++){(*i)->draw();}
    player->draw();
}

void ObjectSimulates(){
    for(auto i = allies.begin(); i!=allies.end(); i++){(*i)->simulate();}
    for(auto i = enemies.begin(); i!=enemies.end(); i++){(*i)->simulate();}
    for(auto i = objects.begin(); i!=objects.end(); i++){(*i)->simulate();}
    player->simulate();
}
void ObjectEvents(){
    for(auto i = allies.begin(); i!=allies.end(); i++){(*i)->events();}
    for(auto i = enemies.begin(); i!=enemies.end(); i++){(*i)->events();}
    for(auto i = objects.begin(); i!=objects.end(); i++){(*i)->events();}
    player->events();
}

//Enemy Patterns Go Here
void initializeEnemyMap(){
    // USED METAFLOAT 0:4
    // USED METAINT   0:1
    // USED METABOOL  0:3
    // META BOOL   2 and 3 IS RESERVED FOR PROCESSING FLAGS
    // META FLOAT 3 IS RESERVED FOR DETERMINING SHOT FREQUENCY
    // META FLOAT 4 IS RESERVED FOR GENERAL TIME ELASPING
        ///Randomly select a direction and move in that direction.
        enemyMap.insert({"moveStraight",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->dieIfOutOfBounds();
            if(metaBool.size() < 3) metaBool.resize(3,false);
            if(!metaBool[2]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);

                character->vx = result.x;
                character->vy = result.y;
                metaBool[2] = true;
            }
            if(metaFloat.size() < 4) metaFloat.resize(4,0);
            if(metaFloat[3] >= 1000000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"alternateStraight",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->dieIfOutOfBounds();
            if(metaBool.size() < 4) metaBool.resize(4,false);
            if(!metaBool[3]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);

                if(projectiles.rand() % 2 == 0) result.x*=-1;

                character->vx = result.x;
                character->vy = result.y;
                metaBool[3] = true;
            }
            if(metaFloat.size() < 4) metaFloat.resize(5,0);
            metaFloat[3]+=dt;
            metaFloat[4]+=dt;
            if(metaFloat[4] >= 1500000){
                    character->vx*=-1;
                    character->vy*=-1;
                    metaFloat[4] = 0;
            }
            if(metaFloat[3] >= 1000000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"strafeLeave",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->dieIfOutOfBounds();
            if(metaBool.size() < 3) metaBool.resize(3,false);
            if(!metaBool[2]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);
                    character->vx = result.x;
                    character->vy = result.y;
                if(projectiles.rand() % 2 == 0) character->vx*=-1; else character->vy*=-1;
                metaBool[2] = true;
            }
            if(metaFloat.size() < 4) metaFloat.resize(4,0);
            if(metaFloat[3] >= 600000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"strafeStay",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->stayInBounds();
            if(metaBool.size() < 3) metaBool.resize(3,false);
            if(!metaBool[2]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);
                    character->vx = result.x;
                    character->vy = result.y;
                if(projectiles.rand() % 2 == 0) character->vx*=-1; else character->vy*=-1;
                metaBool[2] = true;
            }
            if(metaFloat.size() < 4) metaFloat.resize(4,0);
            if(metaFloat[3] >= 1000000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"kamikaze",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->stayInBounds();
            Vector2f result(character->s.getPosition() - player->s.getPosition());
            result = result/dist(character->s.getPosition(),player->s.getPosition());
            float sca = -0.01;
            result =result*(sca*dt/character->s.getLocalBounds().width);

            character->vx = result.x;
            character->vy = result.y;
            if(metaFloat.size() < 4) metaFloat.resize(4,0);
            if(metaFloat[3] >= 800000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            character->s.move(character->vx,character->vy);
        }});
        enemyMap.insert({"camp",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->stayInBounds();
            if(metaBool.size() < 4) metaBool.resize(4,false);
            if(!metaBool[3]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);

                if(projectiles.rand() % 2 == 0) result.x*=-1;

                character->vx = result.x;
                character->vy = result.y;
                metaBool[3] = true;
            }
            if(metaFloat.size() < 4) metaFloat.resize(5,0);
            metaFloat[3]+=dt;
            metaFloat[4]+=dt;

            if(metaFloat[4] >= 4500000){
                    character->vx*=0;
                    character->vy*=0;
                    metaFloat[4] = 0;
            }
            if(metaFloat[3] >= 400000 && character->vx == 0 && character->vy == 0){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"randomLeave",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->dieIfOutOfBounds();
            if(metaBool.size() < 3) metaBool.resize(3,false);
            if(!metaBool[2]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);
                    character->vx = result.x;
                    character->vy = result.y;
                if(projectiles.rand() % 2 == 0) character->vx*=-1; else character->vy*=-1;
                metaBool[2] = true;
            }
            if(metaFloat.size() < 5) metaFloat.resize(5,0);
            if(metaFloat[3] >= 600000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            metaFloat[4]+=dt;
            if(metaFloat[4] >= 3000000){
                if(projectiles.rand() % 2 == 0) character->vx*=-1;
                if(projectiles.rand() % 2 == 0) character->vy*=-1;
                metaFloat[4] = 0;
            }
            character->s.move(character->vx*dt,character->vy*dt);
        }});
        enemyMap.insert({"randomStay",
        [](GameObject*character,string name, vector<int>&metaInt, vector<float>&metaFloat, vector<bool>&metaBool){           //Character Part
            character->stayInBounds();
            if(metaBool.size() < 3) metaBool.resize(3,false);
            if(!metaBool[2]){
                Vector2f result(character->s.getPosition() - player->s.getPosition());
                result = result/dist(character->s.getPosition(),player->s.getPosition());
                float sca = -0.004;
                result =result*(sca/character->s.getLocalBounds().width);
                    character->vx = result.x;
                    character->vy = result.y;
                if(projectiles.rand() % 2 == 0) character->vx*=-1; else character->vy*=-1;
                metaBool[2] = true;
            }
            if(metaFloat.size() < 5) metaFloat.resize(5,0);
            if(metaFloat[3] >= 600000){
                dynamic_cast<EnemyInstance*>(character)->shoot();
                metaFloat[3] = 0;
            }
            metaFloat[3]+=dt;
            metaFloat[4]+=dt;
            if(metaFloat[4] >= 3000000){
                if(projectiles.rand() % 2 == 0) character->vx*=-1;
                if(projectiles.rand() % 2 == 0) character->vy*=-1;
                metaFloat[4] = 0;
            }
            character->s.move(character->vx*dt,character->vy*dt);
        }});
}

int RunGame(){
    window.setFramerateLimit(60);
    window.create(VideoMode(512,512),"Title");
    initializePowerUpMap();
    initializeEnemyMap();
    while(true){
        GrabObjectSequence(scene);
        int current_scene = scene;
        dt = 0;
        while(scene == current_scene){
            while(window.pollEvent(event)){
                if(event.type == Event::Closed){
                    window.close();
                    return 0;
                }
                ObjectEvents();
            }
            window.clear();
            BackgroundDraws();
            ObjectDraws();
            ObjectSimulates();
            window.display();
            if(player->alive==false){scene = gameover();}
            backgrounds.remove_if([](GameObject*i){if(!i->alive){delete i; return true;} return false;});
            allies.remove_if([](GameObject*i){if(!i->alive){delete i; return true;} return false;});
            enemies.remove_if([](GameObject*i){if(!i->alive){delete i; return true;} return false;});
            objects.remove_if([](GameObject*i){if(!i->alive){delete i; return true;} return false;});
            dt = deltaClock.restart().asMicroseconds();
            if(!inControl){dt = 0;}
        }
        while(!enemies.empty()){
            delete *(enemies.begin());
            enemies.pop_front();
        }
        while(!allies.empty()){
            delete *(allies.begin());
            allies.pop_front();
        }
        while(!objects.empty()){
            delete *(objects.begin());
            objects.pop_front();
        }
        while(!backgrounds.empty()){
            delete *(backgrounds.begin());
            backgrounds.pop_front();
        }
    }
    return 0;
}
