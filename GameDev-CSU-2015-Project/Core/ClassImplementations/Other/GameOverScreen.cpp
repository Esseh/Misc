GameOverScreen::GameOverScreen(){
    t.loadFromFile("Resources/Graphics/GameOver.png");
    s.setTexture(t);
    elapsedTime = 0;
}
void GameOverScreen::simulate(){
    elapsedTime += dt;
    if(elapsedTime > 3*1000000 && Event::KeyPressed) scene = 0;
}
