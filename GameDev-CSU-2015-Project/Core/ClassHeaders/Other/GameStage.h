/*
    The game stage, procedurally generates enemies.
*/
struct GameStage1:GameObject{
    vector<PowerUp<powerUpPair> > possiblePowerups;
    vector<string> movementPatterns;
    GameStage1(int);
    ~GameStage1();
    void simulate();
    void draw();
    void spawnRandomEnemy();
};
