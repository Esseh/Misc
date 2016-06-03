sf::Keyboard::Key stringMap(string input){
	//Turn to lowercase
	for(int i = 0; i < input.length(); i++){input[i] = tolower(input[i]);}
	if(input == "w"){return Keyboard::W;}
	if(input == "a"){return Keyboard::A;}
	if(input == "s"){return Keyboard::S;}
	if(input == "d"){return Keyboard::D;}
	if(input == "up"){return Keyboard::Up;}
	if(input == "left"){return Keyboard::Left;}
	if(input == "right"){return Keyboard::Right;}
	if(input == "down"){return Keyboard::Down;}
	if(input == "space"){return Keyboard::Space;}
	if(input == "f1"){return Keyboard::F1;}
}
