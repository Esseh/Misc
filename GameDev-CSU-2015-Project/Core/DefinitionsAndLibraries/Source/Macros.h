//List of Macros see GameLoop for usage.

#define _scene(i) if(scene == i)
#define has {
#define _end }
#define player(T) {\
                        player = new T();\
                        allies.push_front(player);\
                    }
#define background(T) {\
                        GameObject*newObject = new T();\
                        backgrounds.push_front(newObject);\
                    }
#define ally(T,F) {\
                        GameObject*newObject = new T();\
                        newObject->t.loadFromFile(F);\
                        newObject->s.setTexture(newObject->t);\
                        allies.push_front(newObject);\
                    }
#define enemy(T,F) {\
                        GameObject*newObject = new T();\
                        newObject->t.loadFromFile(F);\
                        newObject->s.setTexture(newObject->t);\
                        enemies.push_front(newObject);\
                    }
#define object(T,F) {\
                        GameObject*newObject = new T();\
                        newObject->t.loadFromFile(F);\
                        newObject->s.setTexture(newObject->t);\
                        objects.push_front(newObject);\
                    }
