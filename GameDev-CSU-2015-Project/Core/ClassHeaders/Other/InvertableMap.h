/*
    The InvertableMap Random Number Generator
*/
struct InvertableMap{
	unsigned int x;
	InvertableMap(unsigned int seed);
	unsigned int rand();
};
