/*
    The procedural background element.
    It utilizes Cellular Automata in order to create unique patterns to scroll across.
*/
int spawnChance = 27;
int numberOfSteps = 6;
int deathLimit = 3;
int birthLimit = 4;
int cells = 8;

struct proceduralBackground:GameObject{
    static int n;           //Number of Screens Active
    proceduralBackground();
    void simulate();
    void makeBackground();  //Actually Constructs the Background
    void doSimulationStep( vector<vector<bool> > &input);               //A step in the Cellular Automata algorithm we used.
    int countAliveNeighbors( vector<vector<bool> > input, int x, int y);//A helper function for the Cellular Automata algorithm.
};

int proceduralBackground::n = 0;
