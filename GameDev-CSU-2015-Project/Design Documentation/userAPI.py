Making a Scene up in Here!
	A scene id is loaded like so..
		_scene(id) has
			object(Type,FilePath)
			..
		_end
	An example..
		_scene(0) has
			object(GamePlayer,"__Resources/Graphics/player.png")
		_end
	This will initialize scene 0 with the GamePlayer object and the player sprite.
	Scene 0 is always the first scene loaded.

The Basic Game Object-
	struct GameObject{
		Sprite s;
		Texture t;
		//As these are virtual if you do not redfine them
		//it will simply default on these old definition.
		//For example you will almost never have to redefine draw.
		virtual void draw(){window.draw(s);}	//Draws the event.
		virtual void simulate(){return;}		//Runs event behavior.
		virtual void events(){return;}			//Runs events per frame.
	};
	
	Here's an example...
		struct GamePlayer:GameObject{
		bool moveUp,moveLeft,moveDown,moveRight;
		float vx,vy;
		GamePlayer(){moveUp = moveLeft = moveDown = moveRight = false; vx = vy = 0;}
		void simulate(){playerMovement();}
		void events(){playerInput();}
		void playerMovement(){
			vx = vy = 0;
			#define P_VELOCITY 0.0005
			vx = dt*P_VELOCITY*(moveRight - moveLeft);
			vy = dt*P_VELOCITY*(moveDown - moveUp);
			s.move(vx,vy);
		}
		void playerInput(){
			if(PressKey("Up") || PressKey("W"))
				moveUp    = true;
			if(PressKey("Right") || PressKey("D"))
				moveRight = true;
			if(PressKey("Left") || PressKey("A"))
				moveLeft  = true;
			if(PressKey("Down") || PressKey("S"))
				moveDown  = true;
			if(ReleaseKey("Up") || ReleaseKey("W"))
				moveUp    = false;
			if(ReleaseKey("Right") || ReleaseKey("D"))
				moveRight = false;
			if(ReleaseKey("Left") || ReleaseKey("A"))
				moveLeft  = false;
			if(ReleaseKey("Down") || ReleaseKey("S"))
				moveDown  = false;
		}
		};

Here are the variables you have access to..
	Clock deltaClock 
		this is equivalent to a SFML clock. it can grab elapsed time until
		a loop's completion. You could use it if for some reason what you
		were doing was so time sensitive it couldn't wait for the frame to 
		be over.
	float dt
		this is our delta time, how many microseconds that have passed in the previous frame. 
		It always holds a whole number but being a float means you don't have to be as careful
		with coersion.
	Event event
		this is our sfml event which we can use for polling.
		It's better to ask for API additions than using it directly.
	RenderWindow window
		our sfml window, like the event if you need to modify this 
		it's best to ask for API additions.

Helper Functions to Help You.
	bool PressKey(string)
		Checks if a key has been pressed. If so returns true.
	bool ReleaseKey(string)
		Checks if a key has been released. If so returns true.

Remember: Abstraction is your friend, if you need more functionality ask for API
additions. It can only make things easier in the future.