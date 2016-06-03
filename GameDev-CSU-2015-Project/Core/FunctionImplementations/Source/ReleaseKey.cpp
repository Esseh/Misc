bool ReleaseKey(string input){
    if (event.type == Event::KeyReleased){
        return event.key.code == stringMap(input);
    }
    return false;
}
