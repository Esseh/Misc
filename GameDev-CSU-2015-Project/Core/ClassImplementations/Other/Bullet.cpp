/*
    Implementation File for Bullets
*/
Bullet::Bullet(float curr_x, float curr_y, string alliance, list<PowerUp<powerUpPair> > pwp,string bounce = ""){
	t.loadFromFile("Resources/Graphics/EnemyBullet.png");
    s.setOrigin(t.getSize().x/2,t.getSize().y/2);
    ally = alliance;
	riccochet = bounce;
	s.setPosition(curr_x,curr_y);
	s.scale(BulletSize,BulletSize);
	if(alliance == "enemies"){ vx = 0.0005; vy = 0.0; }
    else{
        Vector2f result =  - s.getPosition() + player->s.getPosition();
        vx = result.x / 2000000; vy = result.y / 2000000;

    }
	damage = BulletDamage; effects = pwp;
	originalScale = s.getScale();
	originalvx = vx;
	originalvy = vy;
}
void Bullet::simulate(){movement(); collide();}
void Bullet::movement(){
    vx = originalvx;
    vy = originalvy;
    s.setScale(originalScale);
    compositeTexture = Texture(t);
    apply();
    s.setTexture(compositeTexture);
    dieIfOutOfBounds();
    s.move(dt*vx*BulletSpeed,dt*vy*BulletSpeed);
}
void Bullet::collide(){
    if(collision(this,ally)){
        alive = false;
        explosion(s.getPosition(),allies,BulletExplosionSize+(s.getScale().x/2000),BulletExplosionDamage);
    }
}
void Bullet::apply(){
    for(auto i = effects.begin(); i!=effects.end(); i++){
        (i->second)(this,i->name,i->metaInt,i->metaFloat,i->metaBool);
    }
}
