#=========================================================================================
# Encapsulates the abstract behaviour of an agent.
#=========================================================================================
class Agent
	attr_accessor :index
	attr_accessor :actions
	attr_accessor :searchDepth
    def initialize(actionList=[],index=0,searchDepth=0)
		#=========================================================================================
		# An agent has an index. This is its ID.
		#=========================================================================================
        self.index = index
		#=========================================================================================
		# An agent has a list of action. This is its actuators 'A' in the P.E.A.S. model.
		#=========================================================================================
		self.actions = actionList
		#=========================================================================================
		# The maximum depth a search is allowed to go by the agent.
		#=========================================================================================
		self.searchDepth = searchDepth
	end
end
#=========================================================================================
# Encapsulates an action.
#=========================================================================================
class Action
	attr_accessor :parameters
	attr_accessor :evalFunction
	def initialize(p={},evaluationFunction=lambda{|x,y| 0})
		#=========================================================================================
		# An action may have various parameters such as Cooldown, Damage, and Reach
		#=========================================================================================
		self.parameters = p
		#=========================================================================================
		# An action will have an evaluation function. This may utilize its parameters or the game environment.
		# Note that what is held is a lambda. For more diverse behavior the lambda should midirect into a function.
		#=========================================================================================
		self.evalFunction = evaluationFunction
	end
	def evaluate(gameState)
		#=========================================================================================
		# Note that the gameState is usable here. This is the sensors 'S' in the P.E.A.S. model.
		#=========================================================================================
		return self.evalFunction.call(gameState,self)
	end
end
#=========================================================================================
# Encapsulates a representation of the game state.
#=========================================================================================
class GameState
	#=========================================================================================
	# The agents exist in a world with state. This is the Environment 'E' in the P.E.A.S. model.
	#=========================================================================================
	attr_accessor :agents
	attr_accessor :world
	attr_accessor :successorFunction
	def initialize(successor = nil, agents = [], world = nil, successorFunction = lambda{|x,y,z| 0})
		#=========================================================================================
		# A game state should be capable of producing a successor state given an action.
		#=========================================================================================
		if successor != nil
			self.agents = successor.agents.clone unless successor.agents.nil?
			self.world = successor.world.clone unless successor.world.nil?
			self.successorFunction = successor.successorFunction.clone  unless successor.successorFunction.nil?
		else
			#=========================================================================================
			# A game state should have agents capable of action.
			#=========================================================================================
			self.agents = agents
			#=========================================================================================
			# A game state should have a representation of the world.
			#=========================================================================================
			self.world = world
			#=========================================================================================
			# A game state should be capable of producing a successor.
			#=========================================================================================
			self.successorFunction = successorFunction
		end
	end
	#=========================================================================================
	# Returns the successor of the Game State given an agent and its action.
	#=========================================================================================
	def getSuccessor(agent,action)
		return self.successorFunction.call(self,agent,action)
	end
end
#=========================================================================================
# Cry, so much work on this. Pass by reference issues, pass by value issues. 
# Getting Ruby to do what I want it to do.
# Applies the minimax algorithm to the agent behaviour.
#=========================================================================================
def minimax(agent,gameState,depth,initialIndex)
	bestScore = -1.0/0.0    							# Default best(worst) result is a catastrophic failure.
	bestAction = Action.new({"name"=>"doNothing"})		# Default best(worst) action is to stand still.
	alpha = -1.0/0.0	    							# Alpha
	beta  = 1.0/0.0	                					# Beta
	#For each action...
	for action in gameState.agents[initialIndex].actions.reverse
		#=========================================================================================
		# ... get the minimax value of each action..
		# Uses some Evil magic to get around ruby specific copying problems.
		#=========================================================================================
		lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[initialIndex], action))")
		minimax = minValue(lookAhead, depth, alpha, beta, (initialIndex+1)%2, action)
		#=========================================================================================
		# Keep track of every better outcome.
		#=========================================================================================
		if minimax > bestScore
			bestScore = minimax
			bestAction = action
		end
		#=========================================================================================
		# Ignore children when we are bigger than beta.
		#=========================================================================================
		if bestScore > beta
			break
		end
		#=========================================================================================
		# Update alpha
		#=========================================================================================
		alpha = [alpha,bestScore].max
	end
	#=========================================================================================
	# Return the best action.
	#=========================================================================================
	return bestAction
end


def minValue(gameState, depth, alpha, beta ,index, curraction)
	#=========================================================================================
	#If we're as deep as can go then return our result.
	#=========================================================================================
	if terminalTest(gameState,depth)
		val = curraction.evaluate(gameState)
		return val
	end
	#=========================================================================================
	# Our default worst result is an infinitely good success.
	#=========================================================================================
	worstResult = 1.0/0.0
	#=========================================================================================
	# For each action the agent can make...
	#=========================================================================================
	for action in gameState.agents[index].actions.reverse
		#=========================================================================================
		# Look ahead
		#=========================================================================================
		lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[index], action))")
		worstResult = [worstResult, maxValue(lookAhead, depth-1, alpha, beta,(index+1)%2,action)].min
		#=========================================================================================
		# Ignore children who are smaller than alpha.
		#=========================================================================================
		if worstResult < alpha
			break
		end
		#=========================================================================================
		# Update beta
		#=========================================================================================
		beta = [beta,worstResult].min
	end
	return worstResult
end

def maxValue(gameState, depth, alpha, beta ,index, curraction)
		#=========================================================================================
		#If we're as deep as can go then return our result.
		#=========================================================================================
		if terminalTest(gameState,depth)
			val = curraction.evaluate(gameState)
			return val
		end
		#=========================================================================================
		# Our default best result is an infinity bad failure.	
		#=========================================================================================
		bestResult = -1.0/0.0
		#=========================================================================================
		# For each action the agent can make...
		#=========================================================================================
		for action in gameState.agents[index].actions.reverse
			#=========================================================================================
			# Take the best result from our branches.
			#=========================================================================================
			lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[index], action))")
			bestResult = [bestResult, minValue(lookAhead, depth, alpha, beta, (index+1) %2, action)].max
			#=========================================================================================
			# Ignore children when we are bigger than beta.
			#=========================================================================================
			if bestResult > beta
				break
			end
			#=========================================================================================
			# Update alpha
			#=========================================================================================
			alpha = [alpha,bestResult].max
		end
		#=========================================================================================
		# Return the best result.
		#=========================================================================================
		return bestResult
end

#=========================================================================================
# Applies the expectimax algorithm to the agent behaviour.
#=========================================================================================
def expectimax(agent,gameState,depth,initialIndex)
	bestScore = -1.0/0.0								 # Our  best action is initially nothing.
	bestAction = Action.new({"name"=>"doNothing"})		 # Default best(worst) action is to stand still.
	for action in gameState.agents[initialIndex].actions # For Each action...
		#=========================================================================================
		# Look ahead and grab our expectimin value from the other agent.
		#=========================================================================================
		lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[initialIndex], action))")
		expmaxVal = expectiminValue(lookAhead,depth,(initialIndex+1)%2,action)
		#=========================================================================================
		# If this is a new best probabilistic value then take this action instead.
		#=========================================================================================
		if expmaxVal > bestScore
			bestScore = expmaxVal
			bestAction = action
		end
	end
	#=========================================================================================
	# Return the best action we can.
	#=========================================================================================
	return bestAction
end

def expectiminValue(gameState, depth ,index, curraction)
	#=========================================================================================
	# Check if we're done.
	#=========================================================================================
	if terminalTest(gameState,depth)
		#=========================================================================================
		# If so evaluate the worth of the current action.
		#=========================================================================================
		return curraction.evaluate(gameState)
	end
	#=========================================================================================
	# Initialize average value to be 0.
	#=========================================================================================
	expVal = 0
	for action in gameState.agents[index].actions			# For Each action...
		#=========================================================================================
		# Look ahead and sum up the values for the actions we can take.
		#=========================================================================================
		lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[index], action))")
		expVal += expectimaxValue(lookAhead,depth-1,(index+1)%2,action)
	end
	#=========================================================================================
	# Average our resulting sum across our actions
	#=========================================================================================
	return expVal/gameState.agents[index].actions.size.to_f
end

def expectimaxValue(gameState, depth ,index, curraction)
	#=========================================================================================
	# If we're done, that's that.
	#=========================================================================================
	if terminalTest(gameState,depth)
		return curraction.evaluate(gameState)
	end
	#=========================================================================================
	# Initialize our best value to be negative infinity.
	#=========================================================================================
	bestResult = -1.0/0.0
	for action in gameState.agents[index].actions		# For each action...
		#=========================================================================================
		# Look ahead and take the best result out of possible actions.
		#=========================================================================================
		lookAhead = eval(gameState.class.to_s+".new(gameState.getSuccessor(gameState.agents[index], action))")
		bestResult = [bestResult,expectiminValue(lookAhead,depth-1,(index+1)%2,action)].max
	end
	#=========================================================================================
	# Return the best result.
	#=========================================================================================
	return bestResult
end
#=========================================================================================
# Misdirection into minimax
#=========================================================================================
$miniwrapper = lambda{|v,x,y,z| minimax(v,x,y,z) }
#=========================================================================================
# Misdirection into expectimax
#=========================================================================================
$expectiwrapper = lambda{|v,x,y,z| expectimax(v,x,y,z) }

#=========================================================================================
# Needs to be implemented in some way, checks if the simulation is over or max depth reached.
#=========================================================================================
def terminalTest(gameState,depth)
	#=========================================================================================
	# Check if player is dead.
	#=========================================================================================
	pos = nil
	iterator = 0
	while pos == nil
		pos = iterator if(gameState.world[iterator][1] == true)
		iterator+=1
	end	
	if gameState.world[pos][1] && gameState.world[pos][2]
		return true
	end
	#=========================================================================================
	# Check if player is win.
	#=========================================================================================
	pellets = 0
	gameState.world.each{|x| pellets +=1 if x[0]==true}
	if pellets == 0
		return true
	end
	#=========================================================================================
	# Check if we're too stupid to look further.
	#=========================================================================================
	if depth <= 0
		return true
	else
		return false
	end
end