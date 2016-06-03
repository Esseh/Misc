#ifndef ENTITY_H
#define ENTITY_H

class Entity{

public:
    Entity();
    Entity(float px, float py): mPosX(px), mPosY(py) {}
    // use virtual ~Entity(); ???
    ~Entity();

    //Getters
    float GetPosX() {return mPosX;}
    float GetPosY() {return mPosY;}
    //Setters
    void SetPosX(float val){mPosX = val;}
    void SetPosY(float val){mPosY = val;}

protected:
    float mPosX;
    float mPosY;
};

#endif // ENTITY_H
