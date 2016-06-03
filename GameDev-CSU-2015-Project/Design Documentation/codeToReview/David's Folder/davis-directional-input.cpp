enum Direction {Up, Down, Right, Left, W, A, S, D};

bool moveUp = false;
bool moveDown = false;
bool moveLeft = false;
bool moveRight = false;

while(window.isOpen())
{
    sf::Event event;
    while(window.pollEvent(event))
    {
        switch(event.type)
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
        }
}