//requires #include<ctime>
//requires #include<cstdlib>

struct GameEnemy:GameObject{
	int vx,vy;
    GameEnemy(int a,int b){
		srand(time(NULL));
		vx = a;
		vy = b;
		s.x = (rand() % (window.getSize().x-2)) + 1;
		s.y = (rand() % (window.getSize().y-2)) + 1;
	}                                 
    void simulate(){movement(); shoot(); collide();}
    void movement(){
		s.move(vx,vy);
	}                             
    void shoot(){
		//Spawn Davis's bullet
	}
    void collide(){
		//Iterate through player bullet container.
		//Check against player object.
		//If any of these, take a health in damage.
	}
};