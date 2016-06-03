int stageTime;
GameStage1::~GameStage1(){delete generator;}
GameStage1::GameStage1(int seed){
    generator = new InvertableMap(seed);
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
    #define quickAdd(n) possiblePowerups.push_back(PowerUp<powerUpPair>(*(powerUpMap.find(n))));
    //#define patternAdd(n) movementPatterns.push_back(*(enemyMap.find(n)));

    quickAdd("homingShot");
    quickAdd("sizeUp");
    ///quickAdd("mimeHelper");   ///THERE IS SOME BUG WITH THE HELPER, cannot be used. ;-;
    quickAdd("sizeDown");
    quickAdd("growingShot");
    quickAdd("speedUp");
    quickAdd("slowShot");
    quickAdd("fastShot");
    quickAdd("planetaryShot");
    ///quickAdd("pausingShot");  ///If enemy uses it crashes the game.
/**
	moveStraight
	alternateStraight
	strafeLeave
	strafeStay
	kamikaze
	camp
	randomLeave
	randomStay

**/
    movementPatterns.push_back("moveStraight");
    movementPatterns.push_back("alternateStraight");
    movementPatterns.push_back("strafeLeave");
    movementPatterns.push_back("strafeStay");
    movementPatterns.push_back("kamikaze");
    movementPatterns.push_back("camp");
    movementPatterns.push_back("randomLeave");
    movementPatterns.push_back("randomStay");

    stageTime = 0;
}
void GameStage1::simulate(){spawnRandomEnemy();}
void GameStage1::draw(){return;}



//Probabilities are determined with a Gaussian Distribution.
void GameStage1::spawnRandomEnemy(){
/**
	Given a List of Power ups and a Seed
		Select For Probability(Partially Filled Gaussian Distribution)
			Light: Likely
				Group of 1-5(20:20:20:20:20) - Select for Random/Edge(50:50)
					For Each Generated:
						Make List of Random Powerups(size 3) and apply transformations
			Medium: Unlikely
				Group of 1-5(30:30:20:10:10) - Select for Random/Edge(50:50)
					For Each Generated:
						Make List of Random Powerups(size 4) and apply transformations
			Large: Very Unlikely
				Group of 1-2(20:80) - Select for Random/Edge(50:50)
					For Each Generated:
						Make List of Random Powerups(size 8) and apply transformations
						Additionally attach between 1-3 Helpers.
**/
    int timeStep = 8000000;
    elapsedTime += dt;
    if(elapsedTime > timeStep){
        ///Number Produced is from 0-400, the median is 200 which is
        ///most likely produced. 0 and 400 are statistically unlikely to occur.
        string isItRandom;
        string sizeClass;
        int amountSpawned;
        int numberOfPowerups;
        bool enemySelected = false;
        int enemySpawnDistribution = generator->rand() % (200+1) + generator->rand() % (200+1);
        if(generator->rand() % 2 == 0) isItRandom = "random"; else isItRandom = "edge";
        ///Light Case
        if(enemySpawnDistribution >= 120 && enemySpawnDistribution < 280){
            sizeClass = "Small";
            amountSpawned = (generator->rand() % 5) + 1;
            numberOfPowerups = 3;
            enemySelected = true;
        }
        ///Medium Case
        else if((enemySpawnDistribution > 70 && enemySpawnDistribution < 120) || (enemySpawnDistribution >= 280 && enemySpawnDistribution < 170)){
            sizeClass = "Medium";
            amountSpawned = (generator->rand() % 5) + 1;
            numberOfPowerups = 4;
            enemySelected = true;
        }
        ///Large Case
        else{
            sizeClass = "Large";
            amountSpawned = (generator->rand() % 2) + 1;
            numberOfPowerups = 8;
            enemySelected = true;
        }
        if(enemySelected){
            for(int i = 0; i < amountSpawned; i++){
                list<PowerUp<powerUpPair> > powerUpList;
                string commonPattern = movementPatterns[generator->rand() % movementPatterns.size()];
                for(int i = 0; i < numberOfPowerups; i++){
                    int key = generator->rand() % possiblePowerups.size();
                    ///cout <<"Key:" << key << endl;
                    PowerUp<powerUpPair> important = possiblePowerups[key];
                    ///cout << important.name << endl;
                    powerUpList.push_front(important);
                }


               new EnemyInstance(isItRandom,powerUpList,commonPattern,sizeClass);

            }
        }
        elapsedTime = 0;
    }
}
