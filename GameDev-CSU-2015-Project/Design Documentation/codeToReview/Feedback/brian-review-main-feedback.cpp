/**
	Decent practice, hope you're getting comfortable with the environment. 
	Everything wont be as low level as the example.
**/
#include <SFML/Graphics.hpp>
#include <iostream>

using namespace sf;
using namespace std;

int main()
{
	RenderWindow window(VideoMode(800, 600), "TriangleTest");
	CircleShape triangle(30, 3); // define a triangle
	triangle.setPosition(250, 250); // set the triangle near the middle of the screen
	triangle.setFillColor(Color::Blue); // set the color of the triangle to blue

	while(window.isOpen())
	{
		//Define the event variable
		Event eventSF;

		//Check if there is an event
		while(window.pollEvent(eventSF))
		{
			switch(eventSF.type)
			{
			case Event::KeyPressed:
				if(eventSF.key.code == Keyboard::Up || eventSF.key.code == Keyboard::W)
				{
					cout << "P Up\n";
					triangle.move(0, -20); // move up
				}
				if(eventSF.key.code == Keyboard::Down || eventSF.key.code == Keyboard::S)
				{
					cout << "P Down\n";
					triangle.move(0, 20); // move down
				}
				if(eventSF.key.code == Keyboard::Left || eventSF.key.code == Keyboard::A)
				{
					cout << "P Left\n";
					triangle.move(-20, 0); // move left
				}
				if(eventSF.key.code == Keyboard::Right || eventSF.key.code == Keyboard::D)
				{
					cout << "P Right\n";
					triangle.move(20, 0); // move right
				}
				break;
			case Event::Closed:
				window.close(); // close window when finished
				break;
			}
		}

		window.clear();
		window.draw(triangle);
		window.display();
	}

	return 0;
}
