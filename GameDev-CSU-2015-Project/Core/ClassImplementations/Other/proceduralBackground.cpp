proceduralBackground::proceduralBackground(){
    ++n;
    makeBackground();
    s.setTexture(t);
    if(n==1){
        proceduralBackground*second = new proceduralBackground();
        second->s.setPosition(s.getPosition().x + s.getGlobalBounds().width,0);
        backgrounds.push_back(second);
    }
}

void proceduralBackground::simulate(){
    if(n==1){
        proceduralBackground*second = new proceduralBackground();
        second->s.setPosition(s.getPosition().x + s.getGlobalBounds().width,0);
        backgrounds.push_back(second);
    }
    if(s.getPosition().x < 0 - s.getGlobalBounds().width){
        alive = false;
        n--;
    }
    s.move(-0.0005*dt,0);
}
void proceduralBackground::makeBackground(){
    //Initialize Map
    vector<vector<bool> > cmap(cells,vector<bool>(cells,false));
    for(int y = 0; y < cells; y++)
        for(int x = 0; x < cells; x++)
            if(screenSeeds.rand() % 101 < spawnChance)
                cmap[x][y] = true;
    for(int i = 0; i<numberOfSteps; i++)
        doSimulationStep(cmap);
    Image temp;
    temp.create(512,512,Color(20,10,220,255));
    for(int y = 0; y < cells; y++)
        for(int x = 0; x < cells; x++)
            if(cmap[x][y])
                for(int i = 0; i < (512/cells); i++)
                    for(int j = 0; j < (512/cells); j++)
                        temp.setPixel((512/cells)*x+i,(512/cells)*y+j,Color(0,160,230,255));
    t.loadFromImage(temp);
}

void proceduralBackground::doSimulationStep( vector<vector<bool> > &input){
    vector<vector<bool> > cmap(cells,vector<bool>(cells,false));
    for(int i = 0; i < cells; i++){
        for(int j = 0; j < cells; j++){
            int nbs = countAliveNeighbors(input,i,j);
            if(input[i][j]){
                if(nbs < deathLimit)
                    cmap[i][j] = false;
                else
                    cmap[i][j] = true;
            }
            else{
                if(nbs > birthLimit)
                    cmap[i][j] = true;
                else
                    cmap[i][j] = false;
            }
        }
    }
    input = cmap;
}
int proceduralBackground::countAliveNeighbors( vector<vector<bool> > input, int x, int y){
    int count = 0;
    for(int i = -1; i<2; i++){
        for(int j = -1; j<2;j++){
            int nx = x+i;
            int ny = y+j;
            if(i == 0 && j == 0)
                continue;
            else if(nx < 0 || ny < 0 || nx >= cells || ny >= cells)
                count++;
            else if(input[nx][ny])
                count++;
        }
    }
    return count;
}
