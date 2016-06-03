Rational Acting
	Performance Measure: A way of quanitifying how good a behavior is. (IE: Heuristics and Utility Functions)
Rational Thinking
	"Correct Thinking": Propositional Logic
Humanly Acting
	Turing Test: A computer passes if a human interrogator cannot tell it apart from a human.
Humanly Thinking
	Cognitive Science: CSCI modelling with Psychological experimentation methods to construct testable theories about the human mind.
Percept
	An action taken.
Percept Sequence
	All actions taken.
PEAS(Compare to Pacman for Practice)
	Performance Measure
		The Score
		Distance to Pellets/Capsules
		Pellets/Capsules remaining
		Distance to Ghost
	Environment
		The Maze
	Actuators
		Movement(Or staying still)
	Sensors
		Fully Observable
		Knows Everything About the Environment.
Breadth First Search
	Expands All Current Children First...
		1
		
		1
		|\
		2 3
		
		1
		|\
		2 3
		|\
		4 5

		1
		|\
		2   3
		|\  |\
		4 5 6 7
		etc.
	For Fringe it uses a Queue
		Think about Queue Behavior, FIFO
		Assume the leftmost value is the front of the queue.
		1 Pop 1 and Expand
		23 Pop 2 and Expand
		345 Pop 3 and Expand
		4567 ... etc
	Breadth First Search Has the Following Properties-
		1. Finds the shortest path assuming all edges have the same cost.
		2. Finds the path with the shortest amount of nodes.
		3. Complete for all domains except those with inifnite branches.
Depth First Search
	Expands Child First and Then Child's Child ... ...
		1
		|  \
		2     7
		|\   / \
		3 5 8  9
		|\
		4 6
	For Fringe it uses a Stack
	Think of Stack's FILO behaviors..
		1 pop 1 and expand..
		27 pop 2 and expand..
		357 pop 3 and expand
		4567 , 4 is dead end pop off
		657  , 6 is dead end pop off
		57   , is dead end pop off
		7	pop 7 and expand
		89  and so on...
	Depth First Search Has the Following Properties-
		1. It does not garuntee the shortest node path or cost path.
		2. It is complete in all domains, except those with an infinite depth.
Uniform Cost Search
	Expands Lowest Path Cost Node First...
		In this case numbers will represent cost of an edge, X is the goal..
			I
			1  2
			O    O
			7 9 12
			O  X 
	For Fringe it uses a Priority Queue
		The PQ will pop values out based on it's total path cost..
		We start at I and try to reach our goal X
		Expand I
		(1)(2)	Pop (1)
		(2)(1+7)(1+9) Pop (2)
		(1+7)(1+9)(2+12) Pop (1+7) Dead End
		(1+9)(2+12) Pop (1+9), Goal Found
	Uniform Cost Search Has the Following Properties-
		It will find the path with the lowest cost. Though not efficiently.
Greedy Best First Search
	Selects the cheapest node it can see and views the state from that position instead.
	Repeats until failure.
	Very Low Space Requirements, very bad algorithm.
A* Search
	Like Uniform Cost Search but it adds in an additional node cost based on a Heuristic function.
	Examples are hard to fit in so practice on your own with online resources.
	A* has the following properties-
		1. Complete, except in domains where there are inifnitely many nodes such that f(N) <= f(Goal)
		2. O(N^(e*l)) time complexity, where N is the number of nodes, e is the error of the heuristic function, and l is the length to the solution
		3. O(M) space complexity where M is the number of nodes explored
		4. Optimal	
Heuristics
	A function the returns an integer in response to a state
	Admissability		
		for all h(n) , h(n) <= goal cost
		Thus an admissable heuristic never overestimates its goal.
	Consistency
		A consistant Heuristic is also Admissable
		for all h(n) , h(n) <= c(n,a,n') + h(n) 
		That is to say for each position the current heuristic value should be less than the computed A* cost of the successor. 
		
		the sum of the path cost combined with the heurstic is non-decreasing on any path
	Dominance
		If for all n in h1(n) and h2(n)   h1(n) >= h2(n') then h1 dominates h2
		As long as h2 is consistant and admissable then it will be better for search.
		A more dominant heuristic will ensure less nodes expanded towards solution.
Minimax
	Actions are evaluated based on a Utility Function, a higher value is considered a better option by Minimax.
	We have to consider two sets of players.
	A set of players that want to achieve the best possible result.
	A set of players that want that first set of players to achieve the worst possible result.
	For simplicity we will only consider one of each.
	So let's assume we have binary actions..
	We end up with a tree like so..
					  Max
					/     \
				  Min     Min
				 /  \     /  \
			   Max  Max  Max  Max
			   / \   /\   / \  / \
			  3   8 7  2 6  1  1  2
	This can be evaluated literally as...
	Max(Min(Max(3,8),Max(7,2)),Min(Max(6,1),Max(1,2)))
	But a recursive pattern can be seen.
	The tree then reduces like so.
					  Max
					/     \
				  Min     Min
				 /  \     /  \
			     8   7    6   2
		Max(Min(8,7),Min(6,2))

					  Max
					/     \
				  7        2
				 /  \     /  \
			     8   7    6   2
		Max(7,2)
	From there we can see that the left action is probably better.
Alpha Beta Pruning
	For Alpha Beta Pruning we will follow the same rules as Minimax only we now have some additional rules.
	Initially for the root node its alpha is -inf and its beta is +inf
	For a Max node(including root) it's beta is the largest value found in its children.
	For a Min node its beta is the smallest value found in its children.
	A child node's alpha and beta is initialized as the alpha/beta of its parent.
	if at anytime beta <= alpha then nodes at the level can be pruned.
	Trace an example to understand why..
	When considering the parents choices wether it be a max parent or a min parent it will only prune when there is no reason to continue.
	
	tl;dr, the algorithm says 'screw it, none of these are gonna be chosen anyway'
Expectiminimax
	Consider a situation where there are no good options currently but a good option may open up in the future.
	We can then cosntruct a new type of tree using 'chance' nodes instead of an assumption of minimizing..
	
				   Max
				/      \
			 Cha        Cha
			 / \      /    \
		   Max Max    Max   Max
		   /\    /\  /   \   / \  
		   1 9  12 3 19  0   0  10
		 We need a way to compute our chance nodes at Cha.
		 We can define the chance function then as sum(map(actions,max))/chance
		 Where chance is a value passed in by the parent node and is equal to the 1/actions.length at the parent node.
		 So we can treat this tree literally as..
		 
		 max(sum(max(1,9),max(12,3))/actions.length,sum(max(19,0),max(0,10))/actions.length)
		 
		 Which then reduces into..
	
				   Max
				/      \
			 Cha        Cha
			 / \      /    \
		    9  12    19     10

		 max(sum(9,12)/2,sum(19,10)/2)
		 
		 
				   Max
				/      \
			 Cha        Cha
			 / \      /    \
		    9  12    19     10

		 max(21/2,29/2)
		 
				   Max
				/      \
			 10.5      14.5

		 max(21/2,29/2)
		 
		 So we can see that the action on the right is probably better. 
Constraint Satisfaction Problems-
	Our problem is in terms of...
		A group of variables X
		A variable Xi had a domain Di
		
		The goal is to use a set of constraints in order to reduce the domain needed to search.
	Constraint Graphs
		A graph representing when a node is placing a constraint on another node.
		Given the example in the slide..
		We have 6 presenters A,B,C,D,E,F
		We have the following constraints.
		1. Sumultanious presenters cannot be in the same room Simultanious are the pairs (A,B) , (C,D) , and (E,F)
		2. A and C cannot be in the same room.
		3. B and F cannot be in the same room.
		4. B and D cannot be in the same room.
		
		Applying constraint's 2-3 we get the following graph.
		A---C
		
		B---F
		
		B---D
		
		Applying constraint 1 we have..
		A---B
		
		C---D
		
		E---F
		
		So if we put them together..
		
		A---C
		 \   \
		  \   D
		   \ /
		    B----F---E 
	Backtracking Search	
		A DFS traversal occurs, it tests a domain.
		If the result cannot produce a valid successor or goal state, it is pruned.
		Some ways the search can be improved if possible is...
			1. determining which variables are best to assign next.
			2. knowing which order to try values (testing failure early?)
			3. can the problem structure be taken advantage of?
	Arc Consistency	
		if y in Y and x in X
		X -> Y (or X onto Y) is consistent if.. 
		E(y) for A(x)
		
		Thus we can enforce an arc and check if it's consistent.
		IE: 
			We have three variables A,B,C
			and the following constraints..
			1. A and B and C are not equal to eachother.
			2. A < C
			with a domain of {1,2,3}
			
			So our initial legal state is .
			A:{1,2,3}
			B:{1,2,3}
			C:{1,2,3}
			
			We can then enforce A -> C
			So A < C
			This leaves
			A:{1,2}    (if A were 3 then there's no possible way for A to be less than C)
			B:{1,2,3}
			C:{1,2,3}
			
			We can now enforce B onto A
			so A < C and B != A
			A:{1,2}
			B:{1,2,3}
			C:{1,2,3}
			Now we can enforce C onto A
			So C != A, B != A, and A < C
			A:{1,2}
			B:{1,2,3}
			C:{2,3}		(we constrain C, C can never be 1 as that would prevent A from having any valid options such that A < C.)