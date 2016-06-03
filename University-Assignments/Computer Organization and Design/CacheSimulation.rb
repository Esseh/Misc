#=================================================================
#	Cache Simulation by Kenneth Willeford
#	CSCI 113
#	This is a simulation of a cache utilizing the following
#	memory heiarchy. CPU -> Cache -> Main Memory
#	For our write policies we will be using Write-Back for hits
#	and Write-No-Allocate for Miss.
#	Together this essentially translates into 
#		if hit: Write to cache
#		if miss:Write to memory
#	For a store word operation.
#
#	The replacement policy is LRU(Least Recently Used)
#	and a read policy wasn't provided so my simulation uses
#	No Read Through, that is to say that during a 
#	Load Word operation if it cannot be found it will first be loaded
#	into the Cache, and then from the Cache into the Register.
#
#	The program requires no input, to run it just use a ruby 
#	interpreter.
#=================================================================



#====================Initialization=============================================================================================
#The instructions for the simulation. An associative array is utilized to directly map it during the parse to the 'machine code'
#				Load Word								Store Word
INSTRUCTION = {"100011" => lambda{|n| load_word(n[0],n[1],n[2].to_i(2))}, "101011" => lambda{|n| store_word(n[0],n[1],n[2].to_i(2))}}
#The Registers for the simulation. An associative array is utilized to directly map it during the parse to the 'machine code'
#				$zero		    $s1           $s2           $s3           $s4           $s5           $s6           $s7
REGISTERS    = {"00000" => 0, "10001" => 0, "10010" => 0, "10011" => 0, "10100" => 0, "10101" => 0, "10110" => 0, "10111" => 0}
#Block class, all values are initialized to 0.
class Block
	def initialize
		#Valid bit
		@valid = 0
		#Tag field.
		@tag   = 0
		#Data field.
		@data  = 0
	end
	#Setter Methods
	def valid=(newval)
		@valid = newval
	end
	def tag=(newval)
		@tag = newval
	end
	def data=(newval)
		@data = newval
	end
	#Getter Methods
	def valid
		@valid
	end
	def tag
		@tag
	end
	def data
		@data
	end
end


#Constructing the simulated CACHE.
CACHE = Array.new(8,Array.new(2,nil)).map{|i| i.map{Block.new}}

#A bit to check for Least Recently Used
LRU   = Array.new(8,0)
#Constructing simulated main memory.
MAIN_MEMORY = Array.new(128,0); (0..127).each{|i| MAIN_MEMORY[i] = i+5}
#====================END Initialization=============================================================================================

#Gets the tag value as a string using the formula discussed in class.
def getTag(n)
	((n/8).to_s(2).rjust(5,"0"))
end

#Gets the set value as a string using the formula discussed in class.
def getSet(n)
	((n%8).to_s(2).rjust(3,"0"))
end

#Splits apart the machine code for the parse.
#Maps it to the proper function and passes along the rest of the machine code.
def run(binary)
	binary = binary.split
	INSTRUCTION[binary[0]].call(binary[1,3])
end

#Handles the load word operation.
#on read:	 CACHE memory
def load_word(loc,in_register,offset)
	#Loads from memory with offset into memory[register location]
	#Get Location in memory.
	location = (offset+REGISTERS[loc])/4
	setnum = getSet(location).to_i(2)
	tag = getTag(location).to_i(2)
	#Hit Block 1? If so use it.
	if((CACHE[setnum.to_i][0]).tag == tag && (CACHE[setnum.to_i][0]).valid == 1)
		print "hit\n"
		REGISTERS[in_register] = (CACHE[setnum.to_i][0]).data
	#Hit Block 2? If so use it.
	elsif((CACHE[setnum.to_i][1]).tag == tag && (CACHE[setnum.to_i][0]).valid == 1)
		print "hit\n"
		REGISTERS[in_register] = (CACHE[setnum.to_i][1]).data	
	else
	print "miss\n"
	#No Hits, Then move to CACHE and then load into the register.
		#If left is LRU
		if(LRU[setnum.to_i] == 0)
			LRU[setnum.to_i] = 1
			(CACHE[setnum.to_i][0]).valid = 1
			(CACHE[setnum.to_i][0]).tag = tag
			(CACHE[setnum.to_i][0]).data = MAIN_MEMORY[location]
			REGISTERS[in_register] = (CACHE[setnum.to_i][0]).data
		else
		#If right is LRU
			LRU[setnum.to_i] = 0
			(CACHE[setnum.to_i][1]).valid = 1
			(CACHE[setnum.to_i][1]).tag = tag
			(CACHE[setnum.to_i][1]).data = MAIN_MEMORY[location]
			REGISTERS[in_register] = (CACHE[setnum.to_i][1]).data			
		end
	end
end

#Handles the store word operation.
def store_word(loc,out_register,offset)
	#Get Location in memory.
	location = (offset+REGISTERS[loc])/4
	setnum = getSet(location).to_i(2)
	tag = getTag(location).to_i(2)
	#Hit Block 1?	If Hit: UPDATE CACHE
	if((CACHE[setnum.to_i][0]).tag == tag && (CACHE[setnum.to_i][0]).valid == 1)
		(CACHE[setnum.to_i][0]).data = REGISTERS[out_register]
		print "hit\n"
	#Hit Block 2?	If Hit: UPDATE CACHE
	elsif((CACHE[setnum.to_i][1]).tag == tag && (CACHE[setnum.to_i][0]).valid == 1)
		(CACHE[setnum.to_i][1]).data = REGISTERS[out_register]
		print "hit\n"		
	else
		#If Miss:UPDATE MEMORY
		print "miss\n"
		#Store register value in memory.
		MAIN_MEMORY[location] = REGISTERS[out_register]
	end
end


#Main Runs the input example and then prints the final system state.
def main
	run "100011 00000 10001 0000000000000100"
	run "100011 00000 10010 0000000000010000"
	run "100011 00000 10011 0000000000100000"
	run "100011 00000 10100 0000000000010100"
	run "101011 00000 10001 0000000001010000"
	run "101011 00000 10010 0000000001000100"
	run "101011 00000 10011 0000000001001100"
	run "101011 00000 10100 0000000011100000"
	run "100011 00000 10001 0000000000100100"
	run "100011 00000 10010 0000000000101100"
	run "100011 00000 10011 0000000000010000"
	run "100011 00000 10100 0000000010101100"
	run "101011 00000 10001 0000000000010100"
	run "101011 00000 10010 0000000000011000"
	run "101011 00000 10011 0000000000100100"
	run "101011 00000 10100 0000000001000100"
	run "100011 00000 10001 0000000000100100"
	run "100011 00000 10010 0000000000101100"
	run "100011 00000 10011 0000000000010000"
	run "100011 00000 10100 0000000010101100"
	run "101011 00000 10001 0000000001100000"
	run "101011 00000 10010 0000000001010100"
	run "101011 00000 10011 0000000001011100"
	run "101011 00000 10100 0000000011110000"
	print "\n\nRegisters \n" + REGISTERS.to_s
	print "\n\nCACHE \n"
	counter = 0
	(CACHE.to_s.gsub("],","\n").split(">\n")).each{|i| print "Set " + ((counter+=1)-1).to_s + i + "\n"}
	counter = 0
	print "\n\nMAIN MEMORY\n"
	MAIN_MEMORY.each{|i| print "Memory Cell " + ((counter+=1)-1).to_s + " has " + i.to_s + "\n"}
	""
end

main