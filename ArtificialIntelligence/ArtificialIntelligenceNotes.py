"""The notes are in python for use in an IDE, this allows easy collapsing to quickly get to critical sections or to hide
unnecessary information."""

#Utilize Class Sections to determine the questions to ask and information to observe in the detailed textbook notes.
Chapter 1 What is AI	-Class Section
	Ruby's Example of the Locked Door
		Enters room and is accidentally locked in.
		Actions are performed-
			1. Check for keys. But there is no key. [Binary Decision Yes/No]
			2. Check for other entrances.			[Binary Decision Exists/Doesn't Exit]
			3. Beginning to Worry					[Looks to Adapt] 
			4. Scream								[Probability of Being Heard]
			5. Alternate Accesses?(Modify Object to Act as Entrance)
			6. Break Door? (Costs and Injury)
			7. Remove Door Hinge? It works!
		This Problem requires some intelligence to solve.
			Perceiving the world: "Door is LOCKED" "I don't have KEY."
			(Knowledge + Evidence) -> Anwer Query-
					Is there a window?
					Is there an alternate access?
					Is there a key alternative?
		Modeling the World:
			Backdoor Access
			Detailed Door Mechanism
		World Knowledge can be Determinitstic
				The door is OPEN or LOCKED
				The window exists YES or NO
				DO HAVE KEY or DO NOT HAVE KEY.
		World Knowledge can be Probalistic:
				Anyone can hear me scream?
		Constraints: 
				No access unless can open the door.
		Intelligent Action:
				Remove door hinges.
				remove door.
		Adaption
				door opened without key
	Turing Test(1950)
		Alan Turing
		Turing Test Requires-
			Natural Language
			Knowledge Representaiton
			Automated Resoning
			Machine Learning
			Total Turing Test - Vision & Robotics
	Thinking Humanly: Cognitive Modeling
		Cognitive Science-
			AI Computational Models + Psychological Experimentation
	Thinking Rationally: Logic - Laws of Thought
		Perhaps a set of perfect thought rules exist.
		Logicist Tradition
		Aristotle
	Thinking Rationally: Probalistic Reasoning
		Perhaps mathematical rules vs EXPECTED Return: Prob(Return)*Return
			Bayesian Methods
			Prob(Flu|Sneeze)=Prob(Sneeze|Flu)*Prob(Flu)
	Acting Rationally!
		Maybe we can't prove algorithm is "intelligent"
		But behavior evaluated as "intelligent"
		Solar Powered Robotic Pool Skimmer
	Robotic Pacman
		Pacman Projects
	Rational Agents
		Agent: Something that act
		Rational Agent: Acts out to best achieve aim.
			-> Books Approach
	Acting Humanly
		"The art of creating machines that perform functions that require intelligence when performed by people."
		"The study of how to make computer do things at which, at the moment, people are better."
	AI Foundations
		Philosophy
			Aristotle...
				(384-3222 bc) was first to formulate a precise set of laws governing the rational part of the ming.
			Rene...
				Descartes(1596-1650) gave the first clear discussion fo the distinction between mind and matter and of the problems that arise.
			The...
				empiricism movement starts with Francis Bacon(1561-1626) works to understand the world through observations.
			Thinking...
				to action also proposed by Aristotle as taking goals and looking for actions to achieve them.
		Mathematics
			Logic/Computability/Probability
				George Bool(1815-1864)...
					fully formalized Boolean Logic.
				The.. 
					first non-trivial algporithm is considered euclid's (300 BC) for finding greatest common divisor.
				Alan Turing(1912-1954)... 
					developed a theory for what was computable.
				Steven Cook(1971) and Richard Karp(1972)...
					introduced idea of determining intrractable problems with NP completeness
				Gerolamo Cardano (1501-1576)...
					first proposed probabilities to understand games of chance.
				Thomas Bayes(1702-1761)
		Economics
			Adam Smith(1723-1790) Wealth of Nations
				Economies as inidividual agents acting to maximize their own economic well being.
			Preferred coutcomes with utility theory and game theory.
				Jogn von Neumann and Oskar Morganstern
			Operations Research looked at multiple decision before feedback
				Markov Decision process with Richard Bellman
				Bellman equation
			Herb Simon Nobel Prize in economics in 1978 for satisficing decisions rather than optimal decisions.
		Neuroscience
			Neurons
			Inspiration for Neural Nets
		Psychology
			Cognitive Science born in 1956 at MIT workshop.
				Noam Chomsky
				Allen Newell and Herb Simon
			A Cognitive Theory should be like a computer program(Anderson,1980)
				Well accepted in Psychology but not Universal.
		Computer Engineering
			First operational computer
				Heath Robinson built by Alan Turing's team in 1940
					Bombe?
				Electro-Mechanical to decipher Enigma Code
				Team built general purpose machine with vacuum tubes.
					12/1943 Mk 1
					6/44 Mk 2
					Colo
			First Oeprational Programmable Computer	Z3 by Conrad Zuse 1943 in Germany
		Control theory and Cybernetics
			How can artifact oeprate under their own control.
			Modern Control Theory-
				Design of systems that maximize an objective function over time.
			Modern Control Theory... 
				differs from AI in its close coupling with its set of mathematical tools.	
		Linguistics
			How does language rela te to thought.
			Psychotherapy based on self udnerstanding based on language.
				Work on writing/rewriting ones own story to imporove quality of life.
			Computational Linguistics
			Natural Language Processing
	History of AI
		Gestation of AI
			1943 Warren McCulloch and Wlater Pitts: Earliest Work Combined:
				Early understanding of the neuron
				propositional logic
				alan turing's computability theory
			Marvin Minsky
			Alan Turing
		Birth of AI - 1946
			John McCarthy coninced
				Marvin MinskyClaude Shannon
				Nathaniel Rochester
			Organized 2-month Darmouth Workshop
			Allen Newell and herbert simon.
		Early Enthusiasm(1952-1969)
			Lots of interesting problems can be solved by computers..
			Newell and Simon Gneeral Problem Solver
				-subgoal ordering
			Herbert Gelernter (1958)  Geometry Theorem Prover
			Arthur Samuel (1952) Checkers
		A dose of reality(1966-1973)
			These early systems failed to scale!
			Limitations with initial representations.
			Limitations with initial computing power.
		Knowledge Based Systems (1969-1979):
			Expert Systems/AI Industry (1980->)
		More Neural Nets 1986->
			Back propagation methods.
		AI and Rigor scientific method: 1987->
			Early Work: 
				"Look Ma! No hands!"
			Later Work:
				Rigorous Empirical Experiments
				Statistical Anlysis of Results
				Shared repositories of test data and code.
			Judea Pearl's work with Bayesian Networks...
				let to an acceptance of Probabilistic Reasoning in AI.
		Intelligent Agents: 1995->
			Web-Bots a common example
		Very Large Data Sets: 2001 ->
			Big Data
			Data Mining
			Machine LearningHuman Genome ProjectsInternet Click Streams
			Sensor Data
			Internet of Things
Chapter 2 Intelligent Agents -Class Section
	A
		What's an agent?
			"perceives" environment through "sensors"
			"acts" out into environment through "actuators"
			ie: Pacman-
				sensors: Current location, capsule locations, ghsot locations, etc...
				actuators: direction to move
			ie: 2 square Vacuum Cleaner World
				sensors: Current location, dirt
				acutators: left,right, suck
		PEAS-
			Performance Measure
				Be able to determine how well the agent is doing.
			Environment
				The world the agent exists in.
			Actuators
				How the agent can act upon the world.
			Sensors
				What the agent can understand about the world.
			EXAMPLE-
				Taxi Driver-
					Performance Measure: safe, fast, legal, comfortable, maximize fprofits
					Environment: Roads, other traffic, pedestrians, customers.
					Actuators: Steering, accelerator, brake, signal, horn, display
					Sensors: Cameras, sonar, speedometer, GPS, odometer, accelerometer.
		Fully Observable World vs Partially Observable-
			Former-
				Can see the entire world.
				ie: pacman
			Latter-
				Can only see a subsection of the world.
				ie: poker
		Single Agent vs Multiagent-
			Former-
				Solitary
			Latter-
				Multiple or Adversarial
		Deterministic vs Stochastic
			Environment is deterministic if the next sate is completely determined by the current state and the action executed by the agent
			Uncertain Environment if not fully observable or not deterministic.
		Episodic vs Sequential
			Episodic environments are broken down into separate episodes.
			Each episode is an independent task.
			Each Episode does not depend on pevious episodes.
			Classification taks are often episodic.
		Static vs Dynamic
			Is the world changing or not?
		Continuous vs Discrete
			Affects the algorithms and tools you need to be aware of.
		Known vs Unknown
			Do you know how the world works?
	B
		Agent consists of: 
			Architecture: Computing device with physical sensors and actuators
			Program: implements the agent function that maps percepts to actions
			Agent = Architectures + Program
		Agent Program:
			Input: percept
				agent program takes as input the current percept
			output: action
				agent fucntion returns action based on the percept sequence
		Table Driven Agent Simplest
			Actions are indexed based on current percept sequence.
		Simple Reflex Agent
			Acts according to a rle whose condition matches the current state, as defined by the percept.
		Model-based Agent
			Partial Observability issues
			agent needs to keep track fo the world it can't see.
			agent maintains an anternal stateinternal state is updated due to agent percepts
			
			Has an internal model of the world, operates on that model.
		Goal-based Agent
			...
		Utility-based Agent	
			Uses World States
			Uses a UTILITY Function
		Learning Agent
			Improve as time goes on..
		Environment Representations
			Atomic: 
				A -> B
			Factored:
				O				I
				I				I
				O				I
				I				O
				[***]		   [**]
				[*****] 	-> [*]
			Structured:
				Graph A -> Graph B
				First Order Logic
				Natural Language
Chapter 3 Solving Poblems by Searching -Class Section (More Scratch Notes, seems like examples will be more useful here.)
	Romania Example	I'm in Ara, Romania
		-Sight Seeing
		-Photos
	Wait
		I have a non-refundable ticket leaving out of Bucharest tomorrow!
	The goal is to get from Ara to Bucharest.
	We have to reason-
		Im in arad romania!
		I have a non refundable ticket leaving out of bucharest romorrow..
		Better Adopt Goal: IN BUCHAREST
		
		Environment is Observable
			-Agent always know where it is.
			-I'm in Fresno, Agent in Arad.
		Environment is Discrete	
			Finite number of actions from an state.
		Envrionment is Known
			We have a map.
		Environment is DETERMINISTIC
			-Roads don't magically deliver us to different destinations.
		Search-
			Process of looking for the sequence of actions that lead to goal.
	SEARCH-
		Process of looking for the sequence of actions that lead to goal.
		Thinking(Searching) Agent closes eyes to the world.
		Executes solution (sequence of actions) found one step at a time.	
	function SIMPLE PROBLEM SOLVING AGENT(percept) returns an action
		def pbolsolvage(percept):
			global sequence
			global state
			global goal
			global problems	
			state = updateState(state,percept)
			if not seq:
				goal = formulateGoal(state)
				problem = formulateProblem(state,goal)
				seq = Search(problem)
				if not seq: return Nonaction = seq[0]
				seq = seq[1:]
				return action:
		Search Problem-
			Initial statepossible actions	-actions available actions in states
			Action behaviors(transition model)
			Result(s,a): state that results from doing action a in state s
			Goal Test
			Path Cost
		SuccessorFN: Used by many treatments of problem solving.
		SuccessfulFN: Defined with ACtions(state), Result(state, action)
		Def Successors(state):
			return[(action,Result(state,action))] for
			action in Actions(state)]
		SuccessorFN	getSuccessors: used by pacman worldgetSuccessors(s): Pacman returns[(s1,a1,c1)..n] with state s, action a, and cost c
		
		Modeling/Abstraction
			State Space Defined by: 
				Initial state,possible actions, and action behavior
			Abstraction requires to create representations	Detail removed from state descriptions/action behaviors.
			Valid Abstraction: Any abstract solution can be expanded into actual solution.
			Usuful Abstraction: Executing abstract solution is easier than original problem.
		Search Problem, Tree of Graph not expanded
		State Space: Robot Block World	Given a set of locks in certain configuration,
		move the blocks into a goal configurationexample
			CBA -> BCA
		Travelling Salesman Problem
		8-Queens Problem
		Tile Sliding Problem

#Textbook Section
Chapter 1 Artificial Intelligence
	1. Introduction
		What is AI?
			Rationality-
				A measure of ideal performance
				A system is 'rational' if it does the correct thing.
			Thinking Humanely-
				The effort to make computers think in the full and literal sense.
				To do this we need to understand human thinking we can do this in three ways...
					1. Introspection: Catching our thoughts as they go by.
					2. Psychological Experiments: Observing a person in action.
					3. Brain Imaging: Observing the brain in action.
				Cognitive Science-
					AI Computational Models + Psychological Study to construct precise and tstable theories of the human mind.
					While the goals of AI and Cognitive Science may be different their breakthroughs affect eachother.
			Acting Humanely-
				Creating machines that perform functions that require intelligence when performed by people.
				The Turing Test (Alan Turing) a test for acting humanely, the system passes the test if an 
				'interregator' cannot tell that it is a machine.
				To pass the test the machine needs the following capabilities...
					1. Natural Language Processing: To communicate in English
					2. Knowledge Representation: To store what is knows or hears.
					3. Automated Reasoning: To use the stored information to answer questions and draw new conclusions.
					4. Machine Learning: To adapt to new circumstances and to detect and extrapolate patterns.
				The hardware required would be...
					1. Computer Vision: To percieve objects
					2. Robotics: To munipulate objects and move about.
			Thinking Rationally-
				Studying mental faculties through computational models.
				Logic-
					Formal Reasoning and Propositional Reasoning (Deductive vs Inductive)
					"I am a man, all men are mortal, therefore I am mortal"
			Acting Rationally-
				Computational Intelligence is the study of the design of intelligent agents.
				"Agent"-
					Something that acts.
				"Rational Agent"-
					An agent that acts so as to achieve the best expected outcome.
					A rational agent may need to make correct inferences about a situation.
					Alternatively logical reasoning may be more important to achieve the best outcome.
					Reflexive Actions may also be necessary to achieve the best outcome.
				"Limited Rationality"-
					Acting appropriately when there is not enough time to do all the computations one might like.
		The foundations of AI
			Philosophy-
				Can Formal rules be used to draw valid conclusions?
				How doe sthe mind arise from a physical brain?
				Where does knowledge come from?
				How does knowledge lead to action?
				"Aristotle"
				"Ramon Lull"
				"Thomas Hobbes"
				"Leonardo Da Vinci"
				"Wilhelm Schickard"
				"Blaise Pascal"
				"Gottfried Wilhelm Leibniz"
				"Rene Descartes"
				"David Hume"
				"Ludwig Wittgenstein"
				"Bertrand Ruseel"
				"Rudolf Carnap"
				"Carl Hempel"
			Mathematics-
				What are the formal rules to draw valid conclusions?
				What can be computed?
				How do we reason with uncertain information?
				...
			Economics-
				...
			Neuroscience-
				...
			Psychology-
				...
			Computer Engineering-
				...
			Control Theory and Cybernetics-
				...
			Linguistics-
				...
		The History of AI
			The Gestation of AI(1943-1955)
			The birth of AI(1956)
			Early Enthusiasm, great expectations(1952-1969)
			A dose of reality(1966-1973)
			Knowledge-based systems: The key to power?(1969-1979)
			AI Becomes and Industry(1980-present)
			The Return of Neural Networds(1986-present)
			AI Adopts the scientific method(1987-present)
			The emergence of intelligent agents(1995-present)
			The availability of very large data sets(2001-present)
		The State of the Art	
			...
	2. Intelligent Agents
		Agents and Environments
			"Agent"-
				An agent can be said to be anything that can percieve its environment through sensors(taking in information) and 
				actuators(acting)
			"Percept"-
				An agent's perceptual inputs at any given instant.
			"Percept Sequence"-
				A history of what an agent has percieved.
			"Agent Function"-
				Maps a percept sequence to an action
			"Agent Program"-
				Concrete Implementation of agent function
			"Vaccuum World"-
				Test Program "ChapterTestPrograms/VaccuumWorld.py"
		Good Behavior: The Concept of Rationality
			For each possible percept an action should be taken to maximize its performance measure given whatever evidence it has.
			Omniscience vs Rationality-
				An omniscient agent knows the actual outcome of its actions and can act accordingly
				but it's impossible in reality.
				Rationality maximizes expect performance, it is not perfection.
		The Nature of Environments
			PEAS-
				Performance- 
					Determine the performance measure, how is good behavior defined?
				Environment
					What is the world the agent resides in?
				Actuators
					What can the agent do?
				Sensors
					What can the agent know?
			Fully observable vs Partially Observable-
				Can the agent sense the entire environment?
			Single-Agent vs Multi-Agent-
				Is there one agent or more?
				Is it competetive? cooperative?
			Deterministic vs Stochastic-
				Is the next state entirely decided by the current state?
			Episodic vs Sequential-
				Does the current state not depend on the previous?
			Static vs Dynamic-
				Does the environment stay the same while the agent is thinking?
			Discrete vs Continuous-
				Is the space limited?
			Known vs Unknown-
				Are the outcomes for a percept given?
		The structure of Agents
			agent = architecture + program-
				physical architecture to run the program and take in the environmental information it needs
				the program to implement the agent program.
			Simple-Reflex Agent-
				Select based on current percept, act accordingly
				function simple-reflex-agent(percept)
					state  <- Interpret-input(percept)
					rule   <- Rule-Match(state,rules)
					action <- rule.Action
					return action
			Model-Based Reflex Agent-
				Select based on how the world is changing
				function model-based-reflex-agent(percept)
					state <- Update-State(state,action,percept,model)
					rule  <- Rule-Match(state,rules)
					action<- rule.Action
					return action
			Goal-Based-Agent
				Select based on getting closer to goal
				function Goal-Based-Agent
					return(reflex(),goal Information())
			Utility-Based
				Like goal but based on some measure instead of absolutes.
			Learning Agents
				LEARNS		
Chapter 2 Problem-Solving
	3. Solving Problems by Searching
		Problem-Solving Agents
		function Simple-Problem-Solving-Agent(percept)
			persistent: seq, 	an action sequence, initially empty
						state, 	some description of the current world state
						goal, 	a goal, initially null
						problem,a problem formulation
			state <- Update-State(state,percept)
			if seq is empty then
				goal <- Formulate-Goal(state)
				problem <- formulate-problem(state,goal)
				seq <- search(problem)
				if seq = failure then return a null action
			action <- First(seq)
			seq <- Rest(seq)
			return action
		
		This has an initial state such as In(Arad) in the reaching Bucharest problem.
		ELEMENTS-
			Actions- 
				A description of possible actions available. Given a state s, ACTIONS(s) return a list of actions that can be executed.
				ie: The actions in In(Arad) are {Go(Sibiu),Go(Timisoara),Go(Zerind)}
			Transition Model-
				A description of what each action does. Represented with Result(s,a) which returns the state from performing action a in state s
				ie: Result(In(Arad),Go(Zerind)) will give us In(Zerind)
			State Space-
				The state space is either explicitly or implicitly defined and acts as a graph with paths.  Links between nodes are actions.
			Goal Test-
				A simple test to see if it is the goal state. For example in the bucharest problem our goal is In(Bucharest)
			Path Cost- 
				A function that provides a numeric cost to taking a path. Thus travelling certain ways towards bucharest could be more 
				expensive(more distance travelled) even if the nodes traversed are less.
		Example Problems
			Vaccuum World
			8-Puzzle
			8-Queens
			Route-Finding Problem (Real-World)
				Touring-Problem
				Travelling Salesman
			VLSI Layout
			Automatic Assembly Sequencing	
		Searching for Solutions
			Possible action sequences perform the 'search tree' with branches as actions and nodes as states.
			By 'expanding' the current state we can reach new states.
			After expanding we need to choose which child node to explore next.
			If there are no children produced it is a leaf node. If it is not the goal state then it is a dead end.
			The set of nodes available for expansion at any point is known as the frontier.
			The 'search strategy' helps to choose which nodes to expand next.
			Loops CAN form.
			
			function TREE-SEARCH(problem)
				initialize the frontier using the initial state
				loop do
					if the frontier is empty then return failure
					choose a leaf node and remove it from the frontier
					if the node contains a goal state then return the corresponding solution
					expand the chosen node, adding the resulting nodes to the frontier
					
			function GRAPH-SEARCH(problem)
				initialize the frontier using the initial state of problem
				initialize the explored set to be empty
				loop do
					if the frotnier is empty then return failure
					choose a leaf node and remove it from the frontier
					if the node contains a goal state then return the corresponding solution
					add the node to the explored set
					expand the chosen node, adding the resulting nodes to the frontier only if not in the frontier of explored set
					
			Search Infrastructure
				Search Algorithms need to keep track of certain information
					State: the state in the state space to which the ndoe corresponds
					Parent: the node in the search tree that generated this node.
					Action: the action that was applied to the parent to generate the node
					Path-cost: The cost, traditionally denoted by g(n), of the path from the initial state to the node.
			
			function child-node(problem,parent,action) returns a node
				return a node with
					State = problem.result(parent.state,action)
					Parent = parent, Action = action
					Path-cost = parent.path-cost + problem.step-cost(parent.state,action)
		
			Nodes can be stored in a queue
			
			Measuring-problem solving performance
				Completeness:		Is it garunteed to find a solution if it exists?
				Optimality:			Is the solution optimal?
				Time compexity:		Time it takes to find a solution.
				Space Complexity:	The memory needed to search.
		Uninformed Search Strategies
			Breadth-first search
				Choose Shallowest Node to Expand First
				
				function BFS(problem) returns a solution or failure
					node <- a node with state = problem.initial-state, path-cost = 0
					if problem.goal-test(node.state) then return solution(node)
					frontier <- FIFO queue with node as only element
					explored <- empty set
					loop do
						if empty?(frontier) then return failure
						node <- pop(frontier) //Choose shallowest node in frontier
						add node.state to explored
						for each action in problem.actions(node.state) do
							child <- child-node(problem,node,action)
							if child.state is not in explored or frontier then
								if problem.goal-test(child.state) then return solution(child)
								frontier <- insert(child, frontier)
								
			Uniform-cost search
				Expand cheapest node first
				
				function UCS(problem) returns a solution or failure
					node <- a node with state = problem.initial-state, path-cost = 0
					frontier <- a priority queue ordered by path cost with node as only element.
					explored <- an empty set.
					loop do
						if empty?(frontier)  then return failure
						node <- pop(frontier) /* choose lowest cost node */
						if problem.goal-test(node.state) then return solution(node)
						add node.state to explored
						for each action in problem.actions(node.state) do
							child <- child-node(problem,node,action)
							if child.state is not in explored or frontier then
								frontier <- insert(child,frontier)
							else if child.state is in frontier with higher path-cost then
								replace that frontier node with child

			Depth-first search
				Expand most recent node first
					Uses LIFO instead of FIFO

			Depth-limited search
				Limiting how deep DFS can explore.
			Iterative-Deepening Depth First Search
				Perform depth-limited search on incrementing depths until goal is found.
			Bidirectional Search
				Search from start to reach goal,  search from goal to reach start. When they meet the solution is found.
			COMPARING SEARCH STRATEGIES
				p.91
		Informed(heuristic) Search Strategies
			Best-First Search
				Expand the node that is closest to the goal first
			A*
				Best-First Search with Heuristic, expands cheapest path + heuristic in 'frontier' not the current expansion
		Heuristic Functions
			Heuristic is an Integer-
				In the 8 puzzle
					h1 = the number of misplaced tiles
					h2 = the sum of the distances of the tiles from their goal positions
					
					h2 DOMINATES h1
					
				Heuristic should always be less than the solution	(admissable)
				Cost + Heuristic should be non-decreasing			(consistent)
				WHEN MAKING HUERISTICS ESTIMATE COST
Chapter 4 Beyond Classical Search
	Local Search Algorithms and Optimization Problems
		Simulated Annealing-
			Local search inspired by statistical physics
		Gentic Algorithms-
			Local search inspired by evolutionary biology
		More about..
			The idea of local search is that if the path isnt known then a decision must be made based on some 'contingency'
			Local search works by utilizing a 'single node' instead of paths and only moves to neighbors. Path isn't retained.
			This has two advantages-
				1. Low memory overhead
				2. can find reasonable solutions in infinite search spaces
			They are also useful for optimization based on objective functions. In this the goal is to find the global minimum(for cost)
			and the global maximum(for evaluating the objective function.)
		Hill-Climbing Search-
			Algorithm-
				func HillClimb(problem) returns localMax:
					current = makeNode(problem.InitialState)
					loop do:
						neighbor = highestSuccessor(current)
						if neighbor.Value <= current.Value then return current.State
						current = neighbor
			While good at finding local maxima it may run itno problems finding the global maxima. Meaning it may get close to a solution
			but not actually solve it. At the very least it may be easier to work off of this enarly solved state.
			There may also be a sequence of local maxima meaning it's even harder to find the global maxima.
			Otherwise there may be a flat plateaux of values (for all we know it could go for all eternity) and there's
			no way to know at this point that we can't go higher so we get caught in an loop.
		Simulated Annealing-
			Algorithm-
				func simulatedAnnealing(problem,schedule):
					current = makeNode(problem.initialState)
					for t = 1 to infinity do:
						T = schedule(t)
						if T = 0 then return current
						next = randomSuccessor(current)
						deltaE = next.Value - current.Value
						if deltaE > 0 then current = next
						else current = next (only with probability of e^(delta E / T))
		Local Beam Search-
			A local search that runs multiple local searches at once, each local search has information about each other makes sure
			that only fruitful searches are performed. 
		Genetic Algorithms-
			Utilizing a 'fitness function' we determine a random successor by combining two separate parent states. 
			As if through sexual reproduction. Our fitness function is best to be something that increases as we 
			approach our solution. For example with the 8-queens problem we can detect "non-attacking queens" so we can give 7 points to each queen,
			and deduct 1 for each queen it can attack. 
			As such we are garunteed a solution of 8*7 or 56 points.
			From each parent we choose a random 'cross over point' where the states are split at before determining our successors.			
Chapter 5 Adversarial Search
	Minimax
		Max goes first starting from a node, looks for the maximum value from successors.
		Min goes next starting from current node looks for the minimum value from successors.
		Max repeats from current node...
	Alpha Beta Pruning
		Alpha is initially -infinity (Root)
		Beta is initially +infinity  (Root)
		
		A child node inherits the alpha and beta of it's parent.
		
		The beta of a parent node becomes the smallest alpha found in its children.
		The current alpha is the largest value found in the current children.
	
		If at any time in a context B <= A prune the offending node.
Chapter 6 Constraint Satisfaction Problems
	Defining Constraint Satisfaction Problems(CSP)
		{X1..Xn} where X are variables
		{D1..Dn} where D are the domains for a n'th variable.
		C where C is a set of constraints that specify allowable values.
	Map Coloring Problem-
		Say we have australia and we want to make sure each region on the map has it's own color..
		X = {WA,NT,Q,NSW,V,SA,T} (Our regions)
		D{X} = {green,red,blue}
		C = {SA != WA, SA != NT, SA != Q, SA != NSW....  NSW != V} (constraint is that bordering regions can't have the same color)
	Constraint Propagation-
		The idea that enforcing a constraint on a value has rippling effect on the state space.