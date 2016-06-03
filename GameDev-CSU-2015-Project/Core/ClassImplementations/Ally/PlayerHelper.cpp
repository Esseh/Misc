PlayerHelper::PlayerHelper(GamePlayer* m){
    generator = new InvertableMap(enemySeeds.rand() + enemySeeds.rand());
    t.loadFromFile("Resources/Graphics/helper.png");
    s.setTexture(t);
	s.setColor(Color(255,255,255,0));
	life = PlayerHelperLife + 3;
	s.scale(PlayerHelperSize,PlayerHelperSize);
	damage = PlayerHelperDamage;
	master = m;
	int rx1 = (generator->rand() % int(playerSprite->s.getLocalBounds().width));
	int rx2 = (generator->rand() % int(playerSprite->s.getLocalBounds().width));
	int ry1 = (generator->rand() % int(playerSprite->s.getLocalBounds().height));
	int ry2 = (generator->rand() % int(playerSprite->s.getLocalBounds().height));
	anchor_x = rx1 - rx2 + 0.f;
	anchor_y = ry1 - ry2 + 0.f;
	isPlayer = "true";
}
PlayerHelper::~PlayerHelper(){ delete generator; }
void PlayerHelper::simulate(){
    elapsedTime += dt;
    if(appearing)
        fadeIn();
    else{
            invincibility();
            movement();
            collide();
            if(master->shooting && elapsedTime > 200000){shoot(); elapsedTime = 0;}
    }
    master->collide();
    if(master->life <= 0){
        alive = false;
    }
}
//The movement pattern is also responsible for shooting the projectile.
void PlayerHelper::movement(){
    s.setOrigin(s.getLocalBounds().width/2,s.getLocalBounds().height/2);
    s.setPosition(master->s.getPosition().x + anchor_x, master->s.getPosition().y + anchor_y);
}

void PlayerHelper::shoot(){
    GameObject*newObject = new Bullet(s.getPosition().x,s.getPosition().y,"enemies",master->effects);
    allies.push_front(newObject);
}
void PlayerHelper::collide(){
    int damage = collision(this,"enemies");
    if(damage) damageHandling(s.getPosition(),allies,PlayerHelperExplosionSize,PlayerHelperExplosionDamage, damage);
    if(life < 0) alive = false;
}
void PlayerHelper::apply(){
    for(auto i = master->effects.begin(); i!=master->effects.end(); i++) (i->first)(this,i->name,i->metaInt,i->metaFloat,i->metaBool);
}
