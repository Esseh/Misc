#!/usr/bin/python
import sys,re 							#file arguments , regular expressions
#============================================================================
# FresnoF15 Interpreter (Interpreter for .f15)
# By Kenneth Willeford
# Run with "python F15Interpreter.py file_name.f15"
#
# The interpreter runs the FresnoF15 scripting language and returns outputs
# defined in the FresnoF15 scripting language.
#
# The input file must exist. 
#
# The language performs lexical analysis before running as well as
# semantic and syntactical analysis at runtime. 
#
# The Interpreter has been prepared to be extended easily in the future for mroe types, operations, even user defined types/functions.
#
# A Formal Description of the language can be found near relevant definitions.
#
#============================================================================
#----------------------------------------------------------------------------
#A simple input/output stream class I've made
#It is constructed with stream_name(string_input)
#----------------------------------------------------------------------------
class iostream:

	#constructor, also initializes the iterator at 0.
	def __init__(self,string):
		self.stream = string;				#store string
		self.iterator = 0					#initialize iterator
		
	#If the stream is at it's end it returns the string "eof" and does nothing to the iterator.
	#Otherwise it advances the iterator and grabs the value in the previous stream position.
	def get(self):x
		if self.iterator == len(self.stream): return "eof"			#End of Stream, return eof
		else: self.iterator+=1; return self.stream[self.iterator-1] #Advance iterator, return previous value
		
	#If the iterator isn't at the beginning it will move the iterator backwards a step.
	def putback(self):
		if self.iterator!=0: self.iterator-=1				#Move iterator back if not at start.
		
	#More of a wrapper than anything else. Works in conjunction with get() to determine if it is the end of the stream.
	def eof(self):
		return "eof"

#----------------------------------------------------------------------------
#A container class holding various information to reduce code smell.
#----------------------------------------------------------------------------
class con:
		@staticmethod
		def operators(): 				#Operators in our language.
			return "+-/*^="

		@staticmethod
		def operands():  				#Operands in our language.
			return "123456789"

		@staticmethod
		def operatorOperand():			#Combination of all Operators and Operands
			return con.operands() + con.operators_e()

		@staticmethod
		def operators_e():			    #Operators extended with parenthesis.
			return con.operators()+"()"

		@staticmethod
		def varnames():   			    #variable names in our language.
			return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

		@staticmethod
		def symbolList():  				#list of symbols in our language.
			return con.operators_e()+con.varnames()+con.operands()+"program begin end var input output ; ,"

		@staticmethod
		def exitMsg():					#Error Exit Message
			return "\nPress Enter to Exit\n"

		@staticmethod
		def errorCheck(pre,errorMsg,post):			#Checks for errors, if errors exist then display message before exiting.
			if errorMsg != "": raw_input(pre + errorMsg + post + con.exitMsg()); sys.exit(1)

		@staticmethod
		def errorGathering(Error,List,Key):			#Constructs a list of error messages with "Error X" of "X in List" that match "Key".
			return "".join([Error + " " + i + "\n" for i in List if Key(i)])
			
		@staticmethod
		def validTypes():							#List a valid types to declare.
			return "var"
			
		@staticmethod
		def expressionTypes():						#List of valid types for an expression to return.
			return "var"


#----------------------------------------------------------------------------
#The Lexical Analyser - Prints any lexical errors it finds in the input.
#----------------------------------------------------------------------------
def lexicalAnalyser(string):
	#Make Table
	s_table = re.sub("\n|\t"," ",string).replace(';',' ; ').replace(',', ' , ').split()	#construction of s_table

	#Gather Lexical Errors in one pass.
	error = con.errorGathering("Lexical Error: Unresolved Symbol",s_table,lambda x:x not in con.symbolList() and x[0] not in con.operatorOperand())

	#Print Errors if any
	con.errorCheck("",error,"")

	
	
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#Implementation of the Following Language
#<Prog> ::= program <Declarations> begin <Statements> end
#<Declarations> ::= <Declaration> | <Declaration> <Declarations>
#	...
#<Statements> ::= <Statement> <Statements> | empty
#	...
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
# The right recursion for statements/declarations are handled with iteration to keep things light on Python's stack.
#----------------------------------------------------------------------------
def prog(string):
	lexicalAnalyser(string) # Lexical Analysis

	#Gather Instructions
	program = map(lambda x:x.replace('@',' '),string.replace(';',';\t').replace('program','program\t').replace('begin','begin\t').replace(' ','@').replace('\n',' ').replace('\t',' ').split()) #"""	Should be able to be shortened with regex"""

	for i in ["program","begin","end"]: 		#Making sure the program has key terminals.
		if i not in program: con.errorCheck("","Syntax Error: Missing '" + i + "'","")
		
	mode = False 							#Mode to run interpreter, False is declaration, True is run statements		
	for i in program: 						#Run Program
		if i == 'program': continue								# program terminal, ignore and continue.
		if i == 'begin': mode = True; continue					# begin terminal, switch to statements and continue.
		if i == 'end': break									# end terminal, end program.
		if mode == False: declaration(i.lstrip(' '))			# initial mode: run declaration stripped of preceding white space.
		elif mode == True: evaluateStatement(i.lstrip(' '))		# second  mode: run statements  stripped of preceding white space
	
#----------------------------------------------------------------------------	
#Implementation of the Following Language
#<Declaration> ::= var <Id-list>; | empty
#<Id-List>     ::= <Id> | <Id> , <Id-List>	
#----------------------------------------------------------------------------
# Simple iterative representation of the right recursive declarations.
#----------------------------------------------------------------------------
def declaration(string):
	#Check for Missing Semicolon
	if ';' not in string: con.errorCheck("Syntax Error: Expected ';' in",string,"")
	
	#Prepare for parsing.
	copy = string.replace('var','var*').replace(';','').split('*');
	
	#Check if valid type.
	if copy[0] not in con.validTypes(): 
		con.errorCheck("Semantic Error:" , copy[0] + "is not valid type in ", string)

	#Split declared variables into token list.
	copy[1] = copy[1].replace(' ','').split(',')
	
	#Error checking making sure the variable names are valid.
	for i in copy[1]: 
		if i not in id or id[i][0] != None or copy[1].count(i) > 1: con.errorCheck("Semantic Error: Invalid variable name " , i + " in " ,string)

	#Declare variables as [typedef,None]
	for i in copy[1]: id[i][0] = copy[0]
		
#----------------------------------------------------------------------------	
#Implementation of the following language.
# <Statement>  ::= <Assign-St> | <Input-St> |  <Output-St>
# <Assign-St>  ::= <Id> = <Exp>;
# <Input-St>   ::= input <Id>;
# <Output-St>  ::= output <Id>; | output<Exp>;
# <Id>		  ::= a|b|c|..|z|A|B|C..|Z"""
#----------------------------------------------------------------------------	
#Determines the nature of the statement and applies the correct function.
#----------------------------------------------------------------------------	
#<Statement>  ::= <Assign-St> | <Input-St> |  <Output-St>
#----------------------------------------------------------------------------	
def evaluateStatement(string):
	#Missing semicolon return an error.
	if string[-1] != ';': con.errorCheck("Syntax Error: Expected", "; in " + string) 

	#Strip whitespaces and remove ';' for ease of parsing.
	string = string.replace(" ",'').replace(';','') 
	
	#assignment branch
	if '=' in string: assign(string)
	#input branch
	elif 'input' in string: input(string) 
	#output branch
	elif 'output' in string: print output(string) 
	#otherwise error
	else: con.errorCheck("Syntax Error","Invalid Statement ",string)
	
#----------------------------------------------------------------------------			
# Assigns an expression into the variable.
#----------------------------------------------------------------------------	
# <Assign-St>  ::= <Id> = <Exp>;
#----------------------------------------------------------------------------	
def assign(string):
	#split it into left and right values.
	string = string.split('=') 

    #Variable is not a valid name.
	if string[0] not in id: con.errorCheck("Syntax Error: '", string[0] +"' is not a valid name in ", "=".join(string))
	
	#The variable hasn't been declared. (No type in variable space)
	if id[string[0]][0] == None: con.errorCheck("Semantic Error: Undeclared Identifier '", string[0] + "' in " ,"=".join(string))

	#Expected an expression, got an id.
	if string[1] in con.varnames(): con.errorCheck("","Syntax Error: Expected Expression in " + "=".join(string),"") 

	#TYPE CHECKING
	if id[string[0]][0] not in con.expressionTypes(): con.errorCheck("","Semantic Error: Type mismatch in ","=".join(string))
	
	# store the result of the expression into the variable.
	id[string[0]][1] = evaluateExpression(string[1]) 

#----------------------------------------------------------------------------	
# Takes in user input and stores it into the variable.
#----------------------------------------------------------------------------	
# <Input-St>   ::= input <Id>;	
#----------------------------------------------------------------------------	
def input(string):
	#remove irrelevant information.
	string = string.replace('input','')
	
	#Variable is not a valid name.
	if string not in id: con.errorCheck("Syntax Error: '" + string , "' is not a valid name in " , "input " + string) 

	#Undeclared variable, typedef is empty.
	if id[string][0] == None: con.errorCheck("Semantic Error: Undeclared Identifier '" + string, "' in input ", string)
	
	#store value in variable and check types.
	temp = raw_input()
	
	#TYPE CHECKING
	#if id[string][0] not in str(type(temp)): con.errorCheck("","Semantic Error: Type mismatch in ",string)  <-- For use later when/if we extend to more types.
	
	id[string][1] = temp
#----------------------------------------------------------------------------	
# Prints what is in the expression or variable.	
#----------------------------------------------------------------------------	
# <Output-St>  ::= output <Id>; | output<Exp>;
#----------------------------------------------------------------------------	
def output(string):
	#remove irrelevant information.
	string = string.replace('output','')

	#Assume Expression, let it's error handling handle the rest and send out the result.
	if len(string) > 1 or string in con.operands(): return evaluateExpression(string)

	#Variable is not a valid name.
	if string not in id: con.errorCheck("Syntax Error: '" + string , "' is not a valid name in " + "output ", string)

	#The variable hasn't been declared.
	if id[string][0] == None: con.errorCheck("Semantic Error: Undeclared Identifier '" + string , "' in Output " , string) 

	#Send out the variable's value.
	return id[string][1]
#----------------------------------------------------------------------------
#<Id> ::= a|b|c|..|z|A|B|C..|Z
#----------------------------------------------------------------------------
# Variable Space
# A given id is represented by a pair [TypeDef,Value]
#----------------------------------------------------------------------------
id = {ch:[None,None] for ch in con.varnames()}

#----------------------------------------------------------------------------	
#Implementation of following Language
# <Exp>   ::= <Term> <Exp2>
# <Exp2>  ::= + <Term> <Exp2> | - <Term> <Exp2> | Empty
# <Term>  ::= <Factor> <Term2>
# <Term2> ::= * <Pwr> <Term2> | / <Pwr> <Term2> | Empty
# <Pwr>   ::= <Factor>^<Pwr> | Empty
# <Factor>::= <Num> | (<Exp>)
# <Num>   ::= 0|1|2|3|4|5|6|7|8|9"""
#----------------------------------------------------------------------------
#Evaluates the above language. Also encapsulates it into a function and performs syntax error handling on the statement before using it.
#----------------------------------------------------------------------------
def evaluateExpression(string):
		#Declaration of global expression_stream, used for all expression evaluations.
		global expression_stream 
		#Creates the stream based off a string it receives mid-parse
		expression_stream = iostream(string) 

		error = ""

		#Forgive me for the following error checking, 
		#I couldn't think of a nice way to do it.
		
		#------<MESSY CODE>---------------------------------------------------------------------
		for i in range(len(string)-1): 
			#Check for adjacent operands.(We only support single integers currently.)
			if string[i] in con.operands() and string[i+1] in con.operands(): error += "Syntax Error: Adjacent operands " + string[i] + " , " + string[i+1] + " in " + string +"\n" 
			#Check for adjacent operators.
			if string[i] in con.operators() and string[i+1] in con.operators(): error += "Syntax Error: Adjacent operators " + string[i] + "," + string[i+1]+ " in " + string +"\n"
			#Make sure there are operators where they are supposed to be.
			if string[i] in con.operands() and string[i+1] == '(': error += "Syntax Error: Missing operator between " + string[i] + string[i+1] + " in " + string +"\n"   
		
		#Generate list of only parenthesis to check them.
		last_check = "".join([x for x in string if x == '(' or x == ')'])
		#Continuously collapse each parenthesis pair until hopefully nothing remains.
		while '()' in last_check: 
			last_check = last_check.replace('()','') 
		 #Parenthesis without pair remaining implies missing or mismatched.
		if last_check != "": error += "Syntax Error: Mismatched or Missing Parenthesis in " + string + "\n"

		#Display the errors and exit.
		if error != "":	raw_input(error + "Press Enter to Exit \n"); sys.exit()

		#------</MESSY CODE>---------------------------------------------------------------------
		
		#Send out the evaluated result.
		return Exp() 
#----------------------------------------------------------------------------
# <Exp>   ::= <Term> <Exp2>
#----------------------------------------------------------------------------
def Exp(): return Exp2(Term())

#----------------------------------------------------------------------------
# <Term>::= <Factor> <Term2>
#----------------------------------------------------------------------------
def Term(): return Term2(Pwr())

#----------------------------------------------------------------------------
# <Exp2> ::= + <Term> <Exp2> | - <Term> <Exp2> | Empty
#----------------------------------------------------------------------------
def Exp2(inp):
	cur = expression_stream.get()								#Extract from Stream
	if cur != expression_stream.eof():							#If not eof
		if   cur == '+': return Exp2(inp + Term()) 				# + <Term> <Exp2> to final result.
		elif cur == '-': return Exp2(inp - Term()) 				# - <Term> <Exp2> to final result.
		elif cur == ')': expression_stream.putback() 		    # Putback into stream to parse later.
	return inp													#Irrelevant character return current result.

#----------------------------------------------------------------------------	
# <Term2>::= * <Pwr> <Term2> | / <Pwr> <Term2> | Empty	
#----------------------------------------------------------------------------
def Term2(inp):
	cur = expression_stream.get()								#Extract from stream
	if cur != expression_stream.eof():							#If not eof
		if   cur == '*': return Term2(inp*Pwr()) 				#  * <Pwr> <Term2> to final result.
		elif cur == '/': return Term2(inp/Pwr()) 				#  / <Pwr> <Term2> to final result.
		elif cur in '+-)': expression_stream.putback()  		# Putback into stream to parse later.
	return inp													#Irrelevant character return current result.

#----------------------------------------------------------------------------
# <Pwr>   ::= <Factor>^<Pwr> | Empty
#----------------------------------------------------------------------------
def Pwr():
	p = Fact()		 											   #Grab left value.
	cur = expression_stream.get() 								   #Extract from stream.
	if cur == '^': p = p**Pwr() 								   # <Factor>^<Pwr>
	elif cur in '+-*/)': expression_stream.putback() 			   #Putback into stream to parse later.
	return p													   #Send out value regardless of relevance. (Pwr() has no input so steps can't be skipped.)

#----------------------------------------------------------------------------
# <Factor>::= <Num> | (<Exp>)
#----------------------------------------------------------------------------
def Fact():
	cur = expression_stream.get()										 #Extract from stream.
	if cur == '(': temp = Exp(); expression_stream.get(); return temp;   # (<Exp>)
	# <Num> ::= 0|1|2|3|4|5|6|7|8|9
	return ord(cur) - 48

	
prog("\t".join(open(sys.argv[1],'r'))) 							#Run Program from Command Line Argument
raw_input("\nSuccessful: Press Enter to Finish Program\n") 		#YAY IT WORKED
sys.exit()