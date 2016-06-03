/// We wont be needing the enum our directions, they are already enumed in the SFML library and accessible through pressKey and releaseKey
/// in the user API.
//enum Direction {Up, Down, Right, Left, W, A, S, D};


/// Good, this will be moved to be members of the player object.
/// Thus they will be future accessible with player->moveUp and so on.
bool moveUp = false;
bool moveDown = false;
bool moveLeft = false;
bool moveRight = false;

//while(window.isOpen())
//{
//    sf::Event event;

///  our event poller is located in GameManager for future reference.
    while(window.pollEvent(GameManager::event))
    {
	/// too complex, we should use pressKey and releaseKey as defined in userAPI
		/*switch(event.type)
        {
        case sf::Event::Closed:
            Window.close();
            break;
        case sf::Event::KeyPressed:
            if(event.key.code == sf::Keyboard::Up || sf::Keyboard::W)
                moveUp = true;
            else if(event.key.code == sf::Keyboard::Down || sf::Keyboard::S)
                moveDown = true;
            else if(event.key.code == sf::Keyboard::Left || sf::Keyboard::A)
                moveLeft = true;
            else if(event.key.code == sf:: Keyboard::Right || sf::Keyboard::D)
                moveRight = true;
            break;
        case sf::Event::KeyReleased:
            if(event.key.code == sf::Keyboard::Up || sf::Keyboard::W)
                moveUp = false;
            else if(event.key.code == sf::Keyboard::Down || sf::Keyboard::S)
                moveDown = false;
            else if(event.key.code == sf::Keyboard::Left || sf::Keyboard::A)
                moveLeft = false;
            else if(event.key.code == sf:: Keyboard::Right || sf::Keyboard::D)
                moveRight = false;
            break;
        case sf::Event::Closed:
            window.close();
            break;
        default:
            break;
			*/
			///Modified using PressKey and ReleaseKey
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
