EnemyInstance::EnemyInstance(string spawn, list<PowerUp<powerUpPair> > e, string mov, string file){
    generator = new InvertableMap(enemySeeds.rand());
    t.loadFromFile("Resources/Graphics/"+ file + ".png");
    s.setTexture(t);
    sizeClass = file;
    if(spawn == "random") spawnRandom(); else spawnEdge();
	s.setColor(Color(255,255,255,0));

	if(sizeClass == "Small"){
        life = EnemyInstanceLife*1;
        damage = EnemyInstanceDamage*1;
	}
	if(sizeClass == "Medium"){
        life = EnemyInstanceLife*2;
        damage = EnemyInstanceDamage*2;
	}
    if(sizeClass == "Large"){
        life = EnemyInstanceLife*4;
        damage = EnemyInstanceDamage*4;
    }
	s.scale(EnemyInstanceSize,EnemyInstanceSize);
	damage = EnemyInstanceDamage; movementPattern = (enemyMap.find(mov))->second; effects = e; apply();
	enemies.push_front(this);
}
EnemyInstance::~EnemyInstance(){ delete generator; }
void EnemyInstance::simulate(){ elapsedTime += dt; if(appearing) fadeIn(); else{invincibility(); movement(); collide();} }
//The movement pattern is also responsible for shooting the projectile.
void EnemyInstance::movement(){ s.setOrigin(s.getLocalBounds().width/2,s.getLocalBounds().height/2); movementPattern(this,"",metaInt,metaFloat,metaBool); }

void EnemyInstance::shoot(){
    GameObject*newObject = new Bullet(s.getPosition().x,s.getPosition().y,"allies",effects);
    enemies.push_front(newObject);
}
void EnemyInstance::collide(){
    int damage = collision(this,"allies");
    if(damage){damageHandling(s.getPosition(),allies,EnemyInstanceExplosionSize,EnemyInstanceExplosionDamage, damage);};
    static int killed = 0;
    if(life <= 0){
            killed++;
            alive = false;
            int result = generator->rand() % 4;
            if(result == 0){
                int dist = (generator->rand() % (effects.size() - 1));
                auto a = effects.begin();
                for(int i = 0; i < dist; i++) a++;
                GameObject* o = new GamePowerup((a)->name);
                o->s.setPosition(s.getPosition());
            }
            if(killed >= 12){
                int result = generator->rand() % 5;
                if(result == 0){GameObject*o = new GamePowerup("pausingShot"); o->s.setPosition(s.getPosition());}
                else{GameObject*o = new GamePowerup("mimeHelper"); o->s.setPosition(s.getPosition());}
                killed = 0;
            }
        }

}
void EnemyInstance::apply(){
    for(auto i = effects.begin(); i!=effects.end(); i++) (i->first)(this,i->name,i->metaInt,i->metaFloat,i->metaBool);
}
