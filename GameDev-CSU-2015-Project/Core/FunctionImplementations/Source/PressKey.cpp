bool PressKey(string input){
    if (event.type == Event::KeyPressed){
        return event.key.code == stringMap(input);
    }
    return false;
}
