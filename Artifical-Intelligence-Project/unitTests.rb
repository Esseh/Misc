require_relative "Algorithm.rb"
#=====================================================================================================================================
#==============UNIT TESTS=============================================================================================================
#=====================================================================================================================================
#=====================================================================================================================================
class UnitTestWorld < GameState
	attr_accessor :score
	def initialize(copyConstructor=nil)
		if copyConstructor == nil
			self.score = 0 # Performance measure.
			evaluationFunction = lambda{|x,y| unitTestEvaluation(x,y)} # Evaluation Function 
			moveLeft  = Action.new({"name"=>"left" },evaluationFunction) # Action
			moveRight = Action.new({"name"=>"right"},evaluationFunction) # Action
			goodGuy = Agent.new([moveLeft,moveRight],0,5)	# Friendly Agent
			badGuy  = Agent.new([moveLeft,moveRight],1,5)	# Unfriendly Agent
			agents  = [goodGuy,badGuy]
			# [[pellet,player,enemy]..]
			world = [[false,false,false],[false,false,false],[true,false,true],[false,true,false],[true,false,false],[true,false,false]]
			successorFunction = lambda{|x,y,z| unitTestSuccessorFunction(x,y,z)} # Successor Function 		
			super(nil, agents, world, successorFunction)
		else
			# Copy old state
			self.score = Marshal.load(Marshal.dump(copyConstructor.score))
			self.agents = copyConstructor.agents.clone
			self.world = Marshal.load(Marshal.dump(copyConstructor.world))
			self.successorFunction = copyConstructor.successorFunction.clone
		end
	end
end

# Calculates Resulting Points and new positions. Player death is prioritized over victory.
def unitTestSuccessorFunction(gameState,agent,action)
	gS = gameState.clone
	ag = agent
	ac = action
	# determine if friendly or evil
	id = ag.index
	pos = nil
	iterator = 0
	# Get the position of the agent.
	while pos == nil
		pos = iterator if (id == 0 && gS.world[iterator][1] == true) || (id == 1 && gS.world[iterator][2] == true)
		iterator+=1
	end
	
	# MOVE THE AGENT
	if ac.parameters["name"] == "right"
		((gS.world[pos][1] = false;gS.world[pos+1][1] = true;pos+=1) unless pos == (gS.world.size - 1)) if id == 0
		((gS.world[pos][2] = false;gS.world[pos+1][2] = true;pos+=1) unless pos == (gS.world.size - 1)) if id == 1
	end
	if ac.parameters["name"] == "left"
		((gS.world[pos][1] = false;gS.world[pos-1][1] = true;pos-=1) unless pos == 0) if id == 0
		((gS.world[pos][2] = false;gS.world[pos-1][2] = true;pos-=1) unless pos == 0) if id == 1
	end
	
	#determine score stuff!
	gS.score -=1 # -1 point for taking a step.
	if gS.world[pos][1] == true && gS.world[pos][2] == true 
		# Dying is a big loss.
		gS.score-=10
		return gS
	end
	# If the player stepped on a pellet add some points.
	(gS.world[pos][0] = false; gS.score += 5) if gS.world[pos][0] == true && id == 0
	# If it's a victory add a bunch of points.
	pellets = 0
	gS.world.each{|x| pellets +=1 if x[0]==true}
	if pellets == 0
		gS.score += 100
	end
	return gS
end

# score gain/loss and some factor based on pellet distance? Actually grabbing the pellet can be prioritized, but not over death.
def unitTestEvaluation(gameState,action)
	#Find the Player Position
	iterator = 0
	pos = nil
	while pos == nil
		pos = iterator if(gameState.world[iterator][1] == true)
		iterator+=1
	end	
	return -9999999+rand/1000 if pos == (gameState.world.size - 1) && action.parameters["name"] == "right"
	return -9999999+rand/1000 if pos == 0 && action.parameters["name"] = "left"
	# Make value copies
	testState = UnitTestWorld.new(gameState)
	# Look into the future the result of taking this action.
	testState = unitTestSuccessorFunction(testState,testState.agents[0],action)
	# Grab future score.
	score = testState.score
	## REPLACE WITH SUM OF DISTANCES, subtract from result
	# Get the minimum distance to a pellet.
	iterator = 0
	sumofdistances = 0.0
	while iterator != gameState.world.size
		if gameState.world[iterator][0] == true
			sumofdistances += (pos-iterator).abs
		end
		iterator +=1
	end
	# Return the score and the reciprocal of the minimum distance.
	return 3*score - sumofdistances + rand()/1000
end

def actionTestUnit()
	return false unless Action.new.evaluate(1) == 0
	return false unless Action.new({},lambda{|x,y| 1}).evaluate(1) == 1
	return false unless Action.new({1=>"hello"},lambda{|x,y| y.parameters[1]}).evaluate(1) == "hello"
	return true
end

def testUnitAgent()
	a = Agent.new
	return false unless a.index == 0 && a.actions == []
	a = Agent.new([])
	return false unless a.index == 0 && a.actions == []
	a = Agent.new([],1)
	return false unless a.index == 1 && a.actions == []
	a = Agent.new([1])
	return false unless a.index == 0 && a.actions == [1]
	a = Agent.new([1,2,3],12382318123912389182312938)
	return false unless a.index == 12382318123912389182312938 && a.actions == [1,2,3]
	return true
end

def gameStateUnitTest()
	return false unless GameState.new.getSuccessor(1,1) == 0 
	return false unless GameState.new(GameState.new(nil,[1,2])).agents == [1,2]
	return true
end


def unitTestWorldUnitTest
	t = UnitTestWorld.new
	return false unless t.score == 0
	return false unless t.agents.size == 2
	return true
end

def unitTestSuccessorFunctionUnitTest
	t = UnitTestWorld.new
	return false unless t.score == 0
	t = t.getSuccessor(t.agents[0],t.agents[0].actions[0])
	(puts t.world[1][0]; return false) unless t.world[1][0] == false	# Pellet Grabbed
	(puts t.world[1][1]; return false) unless t.world[1][1] == true   # Player In New Position
	(puts t.world[2][1]; return false) unless t.world[2][1] == false  # Player no longer in Old Position
	(puts t.world[3][2]; return false) unless t.world[3][2] == true   # Enemy should be in same position
	return false unless t.score == 4 # The score should be -4
	t = UnitTestWorld.new
	t = t.getSuccessor(t.agents[0],t.agents[0].actions[1])
	return false unless t.world[3][1] == true # Player should be on same spot as enemy.
	return false unless t.world[3][2] == true # Enemy Should Remain in same spot
	return false unless t.world[3][0] == true # Pellet Should Still be there even if player is there since player died.
	return false unless t.score == -11
	t = UnitTestWorld.new
	t.world[0][0] = false
	t.world[3][0] = false
	t = t.getSuccessor(t.agents[0],t.agents[0].actions[0])
	return false unless t.score = 99
	return true
end


def runTests()
	print("GameState Test:",gameStateUnitTest(),"\n")
	print("Agent Test:",testUnitAgent(),"\n")
	print("Action Test:",actionTestUnit(),"\n")
	print("Unit Test World Test:",unitTestWorldUnitTest(),"\n")
	print("Unit Test World Successor Function Test:",unitTestSuccessorFunctionUnitTest,"\n")
end

# Runs the simulation using either expectimax or minimax
def simulateUnitTestWorld(searchMethod)
	# Construct the Test World
	state = UnitTestWorld.new
	# Set the Maximum Search Depth
	searchDepth = 7
	# Initialize the simulation step counter
	simulationStep = 0
	
	#================================================
	# Run the simulation.
	#================================================
	while true
		#================================================
		#Find the Player Position and check if they have lost.
		#================================================
		iterator = 0
		pos = nil
		while pos == nil
			pos = iterator if(state.world[iterator][1] == true)
			iterator+=1
		end	
		if state.world[pos][1] && state.world[pos][2]
			puts("player loses with a score of ",state.score)
			return
		end
		
		#================================================
		#  Check If it's a victory.
		#================================================
		pellets = 0
		state.world.each{|x| pellets +=1 if x[0]==true}
		if pellets == 0
			puts("player wins with a score of ",state.score)
			return
		end
		

		#================================================		
		# Player Gets to Move
		#================================================
		actionTaken = searchMethod.call(state.agents[0],state,searchDepth,0)
		puts actionTaken.parameters["name"]
		state = state.getSuccessor(state.agents[0],actionTaken)

		#================================================
		# Move the enemy on the 7th turn
		#================================================
		simulationStep += 1
		if simulationStep == 6
			# Enemy Moves Right
			#state = state.getSuccessor(state.agents[1],state.agents[1].actions[0])
		end
		if simulationStep > 20
			puts "Simulation Interrupted"
			return
		end
	end
end

def testSearches
	runTests()
	simulateUnitTestWorld($miniwrapper)
	simulateUnitTestWorld($expectiwrapper)
end

testSearches