
class Projectile
{
public:
	Projectile();
	virtual ~Projectile();

	void Update(float elapsedTime);
	void Draw(sf::RenderWindow &rw);

	bool Destroy();

protected:
	bool shouldDestroy;

private:
	float _timeBetweenShots;
	float _velocity;

};
