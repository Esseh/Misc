//The members of GameObject are as follows.
//public Sprite s;
//public virtual void draw()=0;
//public virtual simulate() = 0;
//If you for example uncommented the following line....

//int b;        //It is automatically public without specifying.

//It would produce an instance variable of int b that all Children of GameObject will have.

//Virtual Methods are methods that 'MUST' be implemented by the children classes.
//If you uncomment the following...

//virtual void collide()=0;     //It is automatically public without specifying.

//It would force all children to have to implement a collide() method.


//Otherwise you can use any inline C++ class syntax here to add to GameObject.

//However anything put here should be with the intention for it's children to use.
