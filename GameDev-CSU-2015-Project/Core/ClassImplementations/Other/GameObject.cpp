/*
    Implementation details of GameObject can be seen here.
    For more information check out the header file.
*/



GameObject::GameObject(){alive = true; appearing = true; invuln = 2500000/3; elapsedTime = 0; generator = NULL; damage = 1;}
void GameObject::draw(){window.draw(s);}
void GameObject::simulate(){return;}
void GameObject::events(){return;}
void GameObject::fadeIn(){
	invuln -= dt;
	if(invuln < 500000/3){appearing = false;}
	else if(invuln < 1000000/3)
		s.setColor(Color(255,255,255,255));
	else if(invuln < 1500000/3)
		s.setColor(Color(255,255,255,200));
	else if(invuln < 2000000/3)
		s.setColor(Color(255,255,255,150));
	else if(invuln < 2500000/3)
		s.setColor(Color(255,255,255,50 ));
}



void GameObject::dieIfOutOfBounds(){
	if(s.getPosition().x > window.getSize().x + s.getGlobalBounds().width)
		alive = false;
	if(s.getPosition().x < 0 - s.getGlobalBounds().width)
		alive = false;
	if(s.getPosition().y > window.getSize().y + s.getGlobalBounds().height)
		alive = false;
	if(s.getPosition().y < 0 - s.getGlobalBounds().height)
		alive = false;
}


void GameObject::stayInBounds(){
	if(s.getPosition().x > window.getSize().x - s.getGlobalBounds().width)
		vx = -1*abs(vx);
	if(s.getPosition().x < 0 - s.getGlobalBounds().width + s.getGlobalBounds().width)
		vx = 1*abs(vx);
	if(s.getPosition().y > window.getSize().y - s.getGlobalBounds().height)
		vy = -1*abs(vy);
	if(s.getPosition().y < 0 - s.getGlobalBounds().height + s.getGlobalBounds().height)
		vy = 1*abs(vy);
}



void GameObject::invincibility(){
	if(invuln > 0){
		invuln -= dt;
		s.setColor(Color(255,255,255,invuln % 255));
	}
	else{
		s.setColor(Color(255,255,255, 255));
	}
}



void GameObject::takeDamage(int dmg){
	if(invuln <= 0){
	life-=dmg;
	invuln=200000;
	}
}

void GameObject::damageHandling(Vector2f pos,list<GameObject*> &c,float mag, int dmg, int damageTaken){
	takeDamage(damageTaken);
    if(life == 0){ alive = false; explosion(pos,c,mag,dmg);}
}


void GameObject::spawnEdge(){
	unsigned int wx = window.getSize().x;
	unsigned int wy = window.getSize().y;
	if(generator->rand() % 2 == 0)
		s.setPosition((generator->rand() % 2) * wx ,generator->rand() * wy);
	else
		s.setPosition(generator->rand() % wx ,(generator->rand() % 2) * wy);
}


void GameObject::spawnRandom(){
	s.setPosition((generator->rand() % (window.getSize().x / 2) + window.getSize().x/2),generator->rand() % window.getSize().y);
}
