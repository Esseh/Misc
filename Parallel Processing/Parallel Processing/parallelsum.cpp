	bool done = false;
	int core_difference = 1;
	int core_difference_lookahead = core_difference+1
	int sum = my_value;
	// Continue so long as there will be processors to work with in the future.
	while(core_difference_lookahead <= p && !done){
		// Check if if this is the last action to be performed by this core.
		if(my_rank % core_difference_lookahead == 0){
			int partner = my_rank + core_difference;		// Recieve Right
			// Make sure partner actually exists.
			if(partner < p) sum += recieve(partner);
		} else {
			/* Summation Code */
			int partner = my_rank - core_difference;	// Send Left
			send(partner)
			done = true;								// Finish
		}
		core_difference *= 2;
		core_difference_lookahead *= 2;
	}		
