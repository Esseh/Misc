EnemyHelper::EnemyHelper(EnemyInstance* m){
    generator = new InvertableMap(enemySeeds.rand());
    t.loadFromFile("Resources/Graphics/enemyHelper.png");
    s.setTexture(t);
	s.setColor(Color(255,255,255,0));
	life = EnemyHelperLife + 3;
	s.scale(EnemyHelperSize,EnemyHelperSize);
	damage = EnemyHelperDamage;
	master = m;
	int rx1 = (generator->rand() % int(master->s.getLocalBounds().width));
	int rx2 = (generator->rand() % int(master->s.getLocalBounds().width));
	int ry1 = (generator->rand() % int(master->s.getLocalBounds().height));
	int ry2 = (generator->rand() % int(master->s.getLocalBounds().height));
	anchor_x = rx1 - rx2 + 0.f;
	anchor_y = ry1 - ry2 + 0.f;
	isPlayer = "false";
	enemies.push_front(this);
}
EnemyHelper::~EnemyHelper(){ delete generator; }
void EnemyHelper::simulate(){
    elapsedTime += dt;
    if(appearing)
        fadeIn();
    else{
            invincibility();
            movement();
            collide();
            if(elapsedTime > 1000000){shoot(); elapsedTime = 0;}
    }
    master->collide();
    master->dieIfOutOfBounds();
    if(master->life <= 0){
        alive = false;
    }
}
//The movement pattern is also responsible for shooting the projectile.
void EnemyHelper::movement(){
    s.setOrigin(s.getLocalBounds().width/2,s.getLocalBounds().height/2);
    s.setPosition(master->s.getPosition().x + anchor_x, master->s.getPosition().y + anchor_y);
}

void EnemyHelper::shoot(){
    GameObject*newObject = new Bullet(s.getPosition().x,s.getPosition().y,"allies",master->effects);
    enemies.push_front(newObject);
}
void EnemyHelper::collide(){
    int damage = collision(this,"allies");
    if(damage) damageHandling(s.getPosition(),allies,EnemyHelperExplosionSize,EnemyHelperExplosionDamage, damage);
    if(life < 0) alive = false;
}
void EnemyHelper::apply(){
    for(auto i = master->effects.begin(); i!=master->effects.end(); i++) (i->first)(this,i->name,i->metaInt,i->metaFloat,i->metaBool);
}
