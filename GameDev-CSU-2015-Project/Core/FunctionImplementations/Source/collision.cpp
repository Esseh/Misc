int collision(GameObject*a,string container){
    if(container == "allies")
        for(auto i = allies.begin(); i!=allies.end(); i++)
            if(a->s.getGlobalBounds().intersects((*i)->s.getGlobalBounds()))
                return (*i)->damage;
    if(container == "enemies")
        for(auto i = enemies.begin(); i!=enemies.end(); i++)
            if(a->s.getGlobalBounds().intersects((*i)->s.getGlobalBounds()))
                return (*i)->damage;
    return false;
}
