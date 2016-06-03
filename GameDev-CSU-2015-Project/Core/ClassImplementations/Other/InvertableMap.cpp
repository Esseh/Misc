InvertableMap::InvertableMap(unsigned int seed){x = seed;}
unsigned int InvertableMap::rand(){
	x = x + ((x*x) | 5);
	//Mid square method is used in order to keep from even-odd patterns.
	return x + ((x >> 16));
}
