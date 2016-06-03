#=======================================================================
#	Simulation for 16Bit ALU and 16Bit Multiplier
#		By Kenneth Willeford
#	This simulation imitates the two titled modules by copying them 
#	structurally. This program handles the structuring with more of a
#	functional approach than object oriented.
#	My signals and registers are represented with numbered arrays
#		ie: [0,1,0,0] is the same as 0100
#	Due to this I made my own shift functions so that they can have the
#	functionality of the shift registers.
#	Just run the code in a ruby interpreter and it will run on it's own,
#	the test cases are already in, you just have to press enter when 
#	prompted.
#=======================================================================
#-----------------------------------------------------------------------
# Logic Gates-
#	Computes &,|,^,!
#-----------------------------------------------------------------------
def AND(x,y); 	if x==1 && y==1 	then 1 else 0 end; end
def OR(x,y); 	if x==1 || y == 1 	then 1 else 0 end; end
def NOT(x); 	if x ==1 			then 0 else 1 end; end
def XOR(x,y); OR(AND(NOT(x),y),AND(x,NOT(y))); end

#-----------------------------------------------------------------------
#	2x1 MUX for the Signal Inverter-
#		Demonstrated The correctness of it in the VHDL programs.
#		Essentially the logic table overlapped with XOR. 
#-----------------------------------------------------------------------
def MUX2X1(x,y) XOR(x,y); end

#-----------------------------------------------------------------------
#	1-Bit Full-Adder
#		Built Structurally, it outputs sum and carry out as a 2 element
#		array
#-----------------------------------------------------------------------
def ADDER(a,b,cin)
	return XOR(XOR(a,b),cin) , OR(AND(a,b),AND(cin,XOR(a,b)))
end

#-----------------------------------------------------------------------
# 2Bit-Decoder
#	Maps a 2bit op signal into a size 4 array of signals. 
#	Only one of which are true.
#-----------------------------------------------------------------------
def DECODER2(x,y) 
	#Sends out an array of decoded values
	return AND(NOT(x),NOT(y)),AND(NOT(x),y),AND(x,NOT(y)),AND(x,y)
end

#-----------------------------------------------------------------------
#	4X1 MUX
#		Utilizes the 2Bit-Decoder to map the op signal to the correct ALU
#		output.
#-----------------------------------------------------------------------
def MUX4X1(x,y,a,b,op1,op0)
	d = DECODER2(op1,op0)
	OR(OR(AND(x,d[0]),AND(y,d[1])),OR(AND(a,d[2]),AND(b,d[3])))
end

#-----------------------------------------------------------------------
#	1Bit ALU
# 		Computes and,or,sum and sends out the overflow, result and a 
#		carry out.
#-----------------------------------------------------------------------
def ALU1BIT(a,b,cin,binv,op1,op2) 
	b = MUX2X1(b,binv)
	sUM_RESULT = ADDER(a,b,cin)
	#Send out an array pair of result, cout
	return MUX4X1(AND(a,b),OR(a,b),sUM_RESULT[0],0,op1,op2), sUM_RESULT[1]
end

#-----------------------------------------------------------------------
#		OF_CHECKING for special 1Bit ALU
#			Determines the overflow structurally.
#-----------------------------------------------------------------------
def OF_CHECKING(a,b,sum) 
	AND(XOR(sum,a),NOT(XOR(a,b)))
end

#-----------------------------------------------------------------------
#	1Bit ALU with Overflow Checking
#		Same as ALU but with Overflow Checking
#-----------------------------------------------------------------------
def ALU1BIT_OF (a,b,cin,binv,op1,op2)
	b = MUX2X1(b,binv)
	sUM_RESULT = ADDER(a,b,cin)
	puts sUM_RESULT[0]
	ovf = OF_CHECKING(a,b,sUM_RESULT[0])
	#Send out an array triple of result, cout, overflow
	return MUX4X1(AND(a,b),OR(a,b),sUM_RESULT[0],0,op1,op2), sUM_RESULT[1], ovf
end

#-----------------------------------------------------------------------
#	16Bit ALU
#		Connects 16 1Bit ALUs to create a 16 bit result.
#		The last ALU checks for overflow.
#-----------------------------------------------------------------------
def ALU16BIT(a,b,cin,binv,op1,op2)
	result = [nil]*16
	15.downto(1).each{|i| result[i],cin = ALU1BIT(a[i],b[i],cin,binv,op1,op2)}
	result[0],cout,ovf = ALU1BIT_OF(a[0],b[0],cin,binv,op1,op2)
	#Send out our result, carry out, and overflow
	return result,cout,ovf
end

#-----------------------------------------------------------------------
#	Prints the State of the 16Bit Multiplier
#-----------------------------------------------------------------------
def printState(count,md,mq,ac)
	puts(count.to_s(2))
	puts("MD:" + md.join)
	puts("AC:" + ac.join)
	puts("MQ:" + mq.join)
end

#-----------------------------------------------------------------------
# 16Bit Multiplier
#	Performs shift multiplication on two register values and outputs
#	the values in a 32bit register. 
#-----------------------------------------------------------------------
def MULTIPLIER16BIT(multiplicand,multiplier)
	accumulator = ([0]*16)+multiplier													#Initialize Concatenated Register [AC]+[MQ]
	count = 16																			#Initialize n-bit count.
	printState(count,multiplicand,accumulator[16,32],accumulator[0,16])
	while(count>=0)																		#Start:
		if shiftRight(accumulator) == 1													#Shiftout rightmost bit of [AC|MQ] and test it.
			accumulator[0,16] = ALU16BIT(multiplicand,accumulator[0,16],0,0,1,0)[0]		#If it's 1 then AC = AC+MD
		end
	printState(count,multiplicand,accumulator[16,32],accumulator[0,16])
		count -=1																		#Decrement n-bit count by 1.
	end																					#If count >= 0 then goto Start
	count = 0								
	printState(count,multiplicand,accumulator[16,32],accumulator[0,16])
	accumulator+multiplier
end

#-----------------------------------------------------------------------
# Shifts a Register to the Right
#-----------------------------------------------------------------------
def shiftRight(register)
	register.unshift(0).pop
end
#-----------------------------------------------------------------------
# Shifts a Register to the Left
#-----------------------------------------------------------------------
def shiftLeft(register)
	register.shift
	register.push(0)
end

#-----------------------------------------------------------------------
# Main
#	Runs each of the test cases.
#-----------------------------------------------------------------------
def main
	puts "begin press enter..."
	wait = gets
	MULTIPLIER16BIT([0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0])
	puts "next case, press enter..."
	wait = gets
	MULTIPLIER16BIT([0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0],[0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1])
	puts "next case, press enter..."
	wait = gets
	MULTIPLIER16BIT([1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0],[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1])
	puts "next case, press enter..."
	wait = gets
	MULTIPLIER16BIT([0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1],[1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0])
	puts "press enter to exit the program..."
	wait = gets
end
main