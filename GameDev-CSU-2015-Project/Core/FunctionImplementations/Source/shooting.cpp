void explosion(Vector2f pos,list<GameObject*> &c, float magnitude = 1.0010, int damage = explosionBaseDamage){
   		GameObject*newObject = new GameExplosion(magnitude,damage);
		newObject->t.loadFromFile("Resources/Graphics/Explosion1.png");
		newObject->s.setTexture(newObject->t);
		newObject->s.setPosition(pos.x,pos.y);
		c.push_front(newObject);
}
