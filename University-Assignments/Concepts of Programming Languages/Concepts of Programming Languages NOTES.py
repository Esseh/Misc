Chapter 1 Preliminaries
	1.1 Reasons for Studying Concepts of Programming Languages
		Increased capacity to express ideas
			"Language defines thoughts and ideas" thus "understanding language helps us express thoughts and ideas"
		Improved background for choosing appropriate languages
			Different languages have different default features and structures.
			Languages can emulate features of other languages, but having a knowledge of different languages means
			you can choose a language appropriate for your project 
			instead of sacrificing efficiency(computation time, computation space, user time, user space) 
			in emulating functionality you can just choose an appropriate language that will handle what you're intending
			in a more efficient fashion.
		Increased ability to learn more languages.
			By examining how programmig languages are made we can learn about them easier.
			Additionally by learning about pariadigms it will be easier to adopt other languages.
			IE: Understanding Lazy Evaluation to learn Haskell or Object oriented to learn Java.
			Finally by learning more languages we can learn more languages easier as we become accustomed to them.
			Syntax carries over often, so understanding syntax helps reading languages you may not program in.
		Better Understanding of the Significance of Implementation
			Understanding underlying implementation of language constructs can help in both debugging and the choice
			of your own implementation. In this way you can choose implementations that are a better fit for the language.
			IE: 'pythonic programming' in python.
		Better Use of Languages that are already known
			Languages are complex, you may not know about every feature in a language.
			By using/learning about features in other languages you may become aware of them in a language 
			you already use.
		Overall Advancement of Computing
			Studying languages will help us know which languages should be adopted and to design languages that should be adopted.	
	1.2 Programming Domains
		Programming is used for many purposes thus different languages are good for different things.
		Scientific Applications(History)
			Fortran was used as a competetitor to assembly with this purpose in mind.
			Fortran is extremely efficient and where only efficiency matters it is still used today.
		Scientific Languages
			These are characterized by efficiency over all else.
		Business Applications(History)
			COBOL was the first successful high level language for business purposes.
			The initial version was produced in 1960 and is still used today.
		Business Languages
			These are characterized by facilities for producing elaborate reports, precise description/storing of decimal values,
			characters, and the ability to specifcy decimal arithmatic operations.
		Artifical Intelligence
			Focuses on Symbolic Computation over Numerical, these require flexibility in language.
			Code creation and execution at runtime are an example of this flexibility.
			LISP, Scheme, and Prolog are all examples of these languages.
		Systems Programming and System Software
			The operating system and and programming support tools are referred to as systems software.
			Systems software are developed through Systems Programming Languages such as PL/S, PL/I, BLIIS, Extended ALGOL
			However these days general purpose languages like C are used.
		Web Software
			Web Languages may operate a lot like other languages but the focus is on 'presentation of data'
	1.3 Language Evaluation Criteria (**)
		Basic Criteria
			Readability - How easily code can be read.
				Simplicity
					Less Basic Constructs instead of More
						More Basic Constructs equals More to Learn to understand the language. 
					Feature Multiplicity is Bad
						Sometimes there is more than one way to do something, this can cause confusion when reading
						as a programer might only want to learn 'one way'
						ie: incrementing
								i++
								++i
								i+=1
								i=i+1
					Operator Overloading is Bad
						Giving new meaning to existing operators or common operators makes the program more complex to understand.
					Oversimplification is Bad
						In an effort to make a program more readable by oversimplfying you can instead make an even less readable program.
						IE: Assembly Language
				Orthogonality
					A Small Set of Primitive Types can be combined in a few ways in order to produce control/data structures.
					Basically, complexity made from simplicity.
					Lack of Orthogonality results in more expections to the rules of your language.
					For example.
						if your language supports pointers but pointers cannot point to arrays
						then structures such as 2D arrays cannot be defined.
					Another example.
						Let's look at the english language.
						"I before E except after C"
						This rule is an example of an exception and learners must now learn when the I comes before or after.
						Hoever
						"I before E" would be more Orthogonal as now I always comes before E.
						In assembly language you often have to pass to a register inbetween moving values.
						
						mov eax , var2
						mov var, eax
						
						Would be an "I before E except after C" situation.
						When it would be simpler and easier to learn if you could just...
						
						mov var, var2
					Too Much Orthogonality is Bad
						If we get to extremes and every operation can perform a meaningful operation with everything else then
						it becomes hard to keep track of the possible combinations. 
				Data Types
					having conventions for certain data types helps with readability..
					IE:
						False instead of 0
						True instead of 1
						NULL instead of 0x00000000
				Syntax Design
					Special Words
						ie: while, class, for
					Form and Meaning
						Statements should be made so that they are easily understood.
			Writability - How easy the code is to write for a domain.
				Simplicity and Orthogonality
					Too many constructs or too few combinations of ways to use them results in 
					misuse or disuse of the language.
				Support for Abstraction
					The ability for complexity to be used while ignoring the details
						Process Abstraction
							The aility to make processes. IE: A sorting algorithm so that you can sort data without having to copy paste.
						Data Abstraction
							The ability to represent data strucutres while leaving out details. IE:
								node->data = 3;
								node->left = secondNode;
								node-> right = thirdNode;
							VERSUS
								nodeData      = [3,4,5]
								leftChildren  = [1,-1,-1]
								rightChildren = [2,-1,-1]
				Expressivity
					Convienence instead of Cubersomeness
			Realiability - Able to perform to it's specifications in all conditions.
				Type Checking
					Checking for Type Errors among values and making sure 'similar' types are treated in their own way.
				Exception Handling
					The ability at runtime to detect problems, correct them, and continue working.
				Aliasing
					The ability to have multiple names that can access the same memory cell.
					IE: 
						Two pointers pointing to the same object.
				Readability and Writability
					Both help produce natural code instead of unusual methods.
					The natural methods are more likely to be safe.
			Cost - The Prices to be Paid when using the programming language..
				Compiling Cost 
					- How long it takes to compile, optimization or lack thereof. 
				Training Time  
					- How long it takes to teach someone how the language works. Readability and Writability counts.
				Development Time 
					- How long it takes to develop a program. Writability and Expressiveness Counts.
				Maintaining Time 
					- How easy it is to work with what has been done. Readability counts.
				Cost of Poor Reliability 
					- It might fail.
				Portability 
					- Can it be used on other systems? Through compilation? Natively?
				Generality 
					- How well it can be applied to many applications. Can reduce costs.
				Well-Definedness 
					- How complete and precise the language defines something. Lack of contributes to costs.
	1.4 Influences on Language Design 
		Computer Architecture
			The von Neumann architecture(the CPU/ Mem / IO model Park likes to draw.)
			The actions are represented as 'one after another after another' which brings us
			Imperative Languages, which operate on this principle. IE: Java/C++
		Programming Design Methodologies(History)
			Cannot be summarized, refer to actual section.
	1.5 Language Catagories (*)
		Imperative
			DO IT LINE BY LINE
			IE: Almost Every Language
		Logical
			Do it not line by line, but how it's defined by the rules in the program.
			IE: Prolog
		Object-Oriented
			Data is collected and treated as a single object. Work is done to 'mutate' the object instead of making new ones.
			A triangle has a base and a height. Instead of making a new triangle you just change the base and height.
			IE: C++/Java
		Functional
			Data is returned by value, instead of changing what exists make a new one.
			IE: Scheme, Haskell		
	1.6 Language Design Trade-Offs
		Reliability vs Cost of Execution
			More reliable could mean slower execution(exceptions)
			or space (more information)
		Design Tradeoffs - Writability vs Readability
			Languages that use operator chaining can result in excellent writability but poor readability.. Take this ruby example..
				(1..10).map{(rand(25)+65).chr}.sort.join
				If you're used to list based languages you may be able to tell what it does but from left to right.
					1. Make a list [1,2,3,4,5,6,7,8,9,10]
					2. Transform each element into the character representation of rand(25)+65
					3. Sort it.
					4. Join it together into a single string.
		Writability vs Reliability
			Take for example strucutres that can make our life easier. "pointers"
			Pointers can make working on different data points nice and easy. But there is nothing stopping them from pointint at an 
			invalid address. (Segmentation Fault)
	1.7 Implementation Methods (***)
		Compilation - Translating the program into machine language to run as an executable.
			Compilation is also referred to as Implementation which translates from a source language(such as C++)
			to a lower level language and eventually machine code.
			Compilation takes place in several phases...
				The lexical analyzer grabs every character in a source file while ignoring comments confirming that they are
				aproriate tokens.
				The syntax analyzer construct parse trees which represent the syntatic structure of the program.
				Depending on how it works a tree wouldn't be literally constructed but made on the fly using the information
				that would have generated it. 
				
				**Refer to Figure 1.3**
					The Symbol Table holds the symbols in your language.
					The Intermediate Code Generator makes a type of 'Psuedocode' that is 1 or more steps above the machine language
					The Optimizer will make existing code smaller and faster if possible. (Such as by combining things that can be combined.)
					The code generator will construct machine language out of your code although...
						You will still need code from your operating system, thus this still isn't portable between OS even if 
						the same processor is used.
						Linking...
							Programs will need to communicate and work with other completed programs
							The linkers puts this all together so that it can run.
		Pure Interpretation - No translation is performed, everything is done through another program.
			The interpreter acts as a "Virtual Machine" that emulates a computer system
			Basically it is a program in your computer that is pretending to be a computer running a program.
			**Refer to Figure 1.4**
		Hybrid Implementation System
			Essentially, a comprimise between the two methods..
			**Refer to Figure 1.5**
		Advantages / Disadvantages of Each
			Compilation
				Programs are Fast(Tailor made for your machine. Executes directly from the most basic/fastest operations.)
				Slow Error Feedback(Errors aren't found until compilation.)
			Pure-Interpretation
				Debugging is Easy(The runtime state is always known)
				Programs are Slow (10 to 100 times slower)
				High portability(It is running on it's own imitation of a computer. So only the intermediate program is needed.)
				Fast Error Feedback(Runtime environment can be loaded quickly.)
				Takes up more space(The symbol table needs to be present at all times.)
			Hybrid
				Comprimises advantages/disadvantages of each.
		Preprocessing - Processing before Compilation
			IE: #include<name>
			in C++ will copy the contents of that file into the current file.
			Another C++ example is Macros which will replace your inline code with what is in the macro.
			IE: #define add(a,b) a+b
	1.8 Programming Environments
			This is the environment used to program.
			A text processor, linker, compiler, file system, etc. will be used.
			Other interfaces may be available(such as in drag and drop programming.)
			In short, programming environments is everything that goes into what we use to program.
Chapter 2 Evolution of Major Programming Languages(History/Too much to Summarize)
Chapter 3 Describing Syntax and Semantics
	3.1 Introduction
		The study of programming languages can be split into two catagories.
			Syntax-
				The form of expressions,statements,program units.
				ie: a+=2; would be a statement which is allowed in the language that is syntactically correct.
			Semantics-
				The meaning on that syntax.
				ie: a+=2; adds to a the integer value of 2.
	3.2 The General Problem of Describing Syntax
		A language is constructed from strings of characters known as a 'sentence' or 'statement'
		The lowest possible level of syntatic unit is the 'lexeme'
		Given the statement..
			index = 2 * count + 17;
			lexeme			token
			index			identifier
			=				equal_sign
			2				int_literal
			*				mult_op
			count			identifier
			+				plus_op
			17				int_literal
			;				semicolon
		Languages can be defined in two ways...
			Language Recognizers
				Suppose we have a language L that uses an alphabet E of characters.
				To define L formally using recognition we need a mechanism R called a 'recognition device'
				capable of reading strings from alphabet E
				R would say wether or not a string was in L.
				R would either accept or reject a string.
				If R only accepts any strings from alphabet E only accepts it when it's in L
				then R is a 'description' of L.
				
				This 'R' is in essence a 'syntactical analyzer'
			Language Generators
				Language generators generate the sentences of a language.
				What is produced is unpredictable however it has a close relationship with recognition devices.(The section ends here.)
	3.3 Formal Methods of Describing Syntax
		Backus-Naur Form and Context-Free Grammars
			Context-Free Grammars
				Prog1 in the Labs is an example CFG which we used to implement math.
				It is nearly identicle to BNF (Backus-Naur Form)
			Backus-Naur Form
				BNF is a 'metalanguage'(a language to describe language)
				meant for programming languages.
				Backus-Naur Form is constructed of productions and terminals.
					Productions...
						A rule that produces terminals or more productions...
							<word> -> John Cena <word> | empty
							Describes a language that will recursively produce "John Cena"
							<word> is a production and generates two terminals "John" and "Cena" followed by a production <word>
							This is also a representation that productions can be recursive.
							Not that it is in tail recursive form, for the development of programming languages this is preferred as
							it is easier for us to garuntee that tail recursion will end.
					Terminals...
						A value that no longer has anywhere to go. The end of the road..
						In the production example only "John Cena" awaited at the end.
				BNF was explored heavily in HW2
			Parse Trees
				What's effective about grammars is that they describe the heiarchy of their language.
				You can visualize this heicarchy by construction a 'parse tree'
				a tree constructed from the recursive rules will naturally show the heiarchy of the language.
				Consider the trees we did in HW1. The order they are completed depends on if we take a left or right derivation.
				For us right derivations are preferred.
				Thus we prefer right associtivity and will need to convert left associative operations into right associative rules.
				Basically if we have something that has to be defined with a left recursive rule.. IE..
					<production> = <production> + <next_production> | <next_production>
				We would make the following conversion.
					<production>  = <next_production> <production prime>
					<production prime> = + <next_production> <production prime> | empty
				Note that both can produce the same language, but the second is right recursive which we prefer.
			Dangling Else
				let's look at the following BNF
					 <if_stmt> -> if <logic_expr> then <stmt>
								 |if <logic_expr> then <stmt> else <stmt>
				Consider the example..
					if done == True
					then if denom == 0
					then quotient = 0;
					else quotient = num / denom;
				Trace the productions and something curious happens.
				We have two possible associations for the else.
				This is the 'dangling else' problem.
				This ambiguity would want to be solved in some way so that an else will be associated with a specific if.
				Common convention is to have else associated with the closest if although other methods can be used.
			Extended Backus-Naur Form (EBNF)
				EBNF is a way to extend BNF for convienence and readability but doesn't make it any more powerful otherwise.
					EBNF additions
						non_terminals starts with upper case letters.
						| -- choice/or
						() -- groups
						{} -- 0 or more times
						[] --optional (such as null)
				Consider the following BNF example..
					E->E+T|T
					T->T*F|F
					F->Digit
					Digit->0..9
				We can represent it in EBNF with the following..
					E-> T{(+|-)T}
					T-> F{(*|/)F}
					F-> Digit
					Digit -> 0..9
				Basically we can reduce it to less productions.
			Syntax Chart
				It's hard to describe in words..
				Refer to wikipedia..
				https://en.wikipedia.org/wiki/Syntax_diagram
	3.4 Attribute Grammars
		An Attribute Grammar is a way to describe certain rules in a language.
		Thus this is how we can define language semantics.
		Static Semantics..
			Rules cannot always be expressed in BNF, take for example 
			that for a production to be legal an unrelated production has to exist.
			FOR EXAMPLE conider the following.
				For a variable to be used it has to be declared..
				Represent this in BNF, I dare you.
				(spoilers)
					You can't.
			Rules such as these are referred to as Static Semantics.
			These have to do with the 'legal form' of programs.
			So these are for concrete specific rules.
		Static Semantics can be described using Attribute Grammars.
		These are 'context free grammars' which contain 'attributes'
		which are similar to productions but are computed with 
		'Attribute computation functions' or 'semantic functions''
		'Predicate functions' state the static semantic rules of the language.
		Defining Attribute Grammars...
			A symbol X has two disjoint sets S(X) and I(X)
			S(X) or Synthesized Attributes pass semantic information up a parse tree.
			I(X) or Inherited Attributes pass semantic information across and down a tree.
			Other than these definitions it's hard to simplify, so using Parks notes is useful here.
		Intrinsic Attributes...
			In a parse tree this would be in the 'leaf nodes'
			These can refer to things that were previous declared
			Semantic functions can then compute these values.
		Examples...
			Let us represent the following rule 
			"The Name of the end of a Procedure must match the procedure's name."
				Syntax Rule:
							<proc_def> -> procedure <proc_name>[1]
							<proc_body> end <proc_name>[2];
				Predicate:
							<proc_name>[1].string == <proc_name>[2].string
				Essentially in the above syntax it is only correct if the predicate is true.
				That being that <proc_name> [1] and [2] are both the same.
			Let us look at another example that works with Type Checking
			In it we will be looking at an assignment statement's actual type vs expected type..
				Syntax Rule:
					<assign> -> <var> = <expr>
					<expr> -> <var> + <var> | <var>
					<var> -> A | B | C
				
				CORRESPONDING PREDICATES/SEMANTIC RULES
				
					Syntax: <assign> -> <var> = <expr>
					Semantic: <expr>.expected_type <- <var>.actual_type
					Meaning: The Expected Type of <expr> is implied to be the Actual Type of <var>
					
					Syntax: <expr> -> <var>[2] + <var>[3]
					Semantic: <expr>.actual type <- 
									if {<var>[2].actual_type = int} and
										{<var>[3].actual_type = int}
										then int
									else real
									end if
					Predicate:	<expr>.actual_type == <expr>.expected_type
					Meaning: The actual type of <expr> is implied to be int if <var>[2] is int and <var>[3] is int.
					Otherwise it is a real value. But only if <expr> actual type is in fact it's expected type.

					Syntax: <expr> -> <var>
					Semantic: <expr>.actual_type <- <var>.actual_type
					Predicate:<expr>.actual_type == <expr>.expected_type
					Meaning: The actual type of <expr> is implied to be the actual type of <var>
					But only if  the actual type of <expr> is the expected type of <expr>

					Syntax: <var> -> A | B | C
					Semantic: <var>.actual_type <- look-up{<var>.string}
					Meaning: The actual type of <var> is implied to be the result of the look-up function.
					Where the look up determines the type of the variable being looked up in the symbol table.
	3.5 Describing the Meanings of Programs: Dynamic Semantics
		Operational Semantics
			These are used to describe the meaning of something by specifying it's effects when running it on a machine.
			These can be seen as a sequence of change in states.
			This is split into...
				Natural Operational Semantics...
					Finding the final result					
					The key is to use an intermediate language (1 level above a low level language like assembly)
					where every syntax is clear and obvious in function and use it to describe the meaning of 
					the higher level statement. This can be seen as a sort of psuedocode.
					For example...
						for(expr1; expr2; expr3){
						...
						}
					Can be described with...
						expr1;
						loop: if expr2 is 0 goto out
						...
						expr3;
						goto loop
						out: ...
				Us as humans can act as the interpreter or build an interpreter for this intermediate-level language.
				As a rule of thumb, if you can't describe what an action does to a child it should not be used for the intermediate level language.
				Structural Ooperational Semantics...
					Finding the complete sequence of state changes
					let us consider a state 's' we will find the sequence of states in an action.
					For example let's look an assignment operation...
						let's suppose our current state is s= {...,<x,3>,...}
						and we are applying the operation x = 5;
						we would have a new state s_prime defined such that..
						s_prime = s overlapping_union(i forget the formal term) {<x,5>}  =>  {...,<x,5>,...}
						so now s_prime = {...,<x,5>,...}
						We can represent this formally like so...
							s(a.source) => V
							s(a.target = a.source;) => s overlapping_union {<a.target,v>}
					For another example we can look at addition...
						First the formal definition...
						s(e1) => v1, r(e2) => v2
						s(e1+e2) => v1 + v2
						
						Now we can combine assignment with addition...
							s(a.source) => 	s(e1) => v1 , s(e2) => v2
											s(e1 + e2) => v1 + v2
							s(a.target = a.source;) => s overlapping_union {<s.target,v1 + v2>}
						To put it into perspective an example...
							var = 1 + 2
							s(a.source) => 	s(e1) => 1 , s(e2) => 2
											s(e1 + e2) => 1 + 2 => 3
							s(var = a.source;) => s overlapping_union {<var,3>}
					Suppose we have a series of statements IE..(sequence of statements)
						var = 1 + 2
						var = var + 3
						We can simply represent this as a sequence of states.
						s1 = s0 overlapping_union s0_prime..
						s2 = s1 overlapping_union s1_prime..
						And so on..
						Consider the Von Neumann Model of computing and this approach makes sense.
						This is a top down sequence of states as we would find in a procedural language. 
					Next we will represent conditionals...
						Simple put we now have something to 'test' which we will represent with .test.
						if (a.test)
							...statement sequence...
						else if (b.test)
							...statement sequence...
						else 
							...statement sequence...
						
						Here is an example of us tracing these states
						if ((a > 1)) a = b + c
						else if ((b == c)) b = a + c
						else  c = b + a  ...
							s0 = {...,<a,0>,<b,1>,<c,2>,...}
							if ((a > 1).test) ... failed
							else if ((b == c).test) ... failed
							else ... passed
							
							s0(a.source) => s0(b) => 1 , s0(a) => 0
										s0(b + a) => 1 + 0 => 1
							s0(c = a.source;) => s0 overlapping_union {<c,1>}(s0_prime)
							s1 = s0 overlapping_union s0_prime
							s1 = {...,<a,0>,<b,1>,<c,1>,...}
					If we consider our previous semantics for loops we can trace this with a test function..
						loop: 
						if (not a.test) goto out 
						... statement sequence ...
						goto loop
						out:
						
						In this sense in that we are able to define a sequence of statements S1;S2
						We ca represent a loop as
						SEQ1;SEQ2;SEQ3... so long as a does not fail.
		Axiomatic Semantics
			These are used to mathematically prove the correctness of logic and the state of the machine is no longer considered.
			The goal of Axiomatic Semantics is to either...
				specify program semantics of verify program correctness.
			In Axiomatics we utilize predicates both before and after the occurance of a statement.
			These are called the 'precondition' and 'postcondition'
			If two statements are next to each other such as...
				S1;S2
			Then...
				{C1}S1{C2}S2{C3}
			Notice that S1 and S2 share a condition. The post condition for a statement is the precondition for the next.
			This is referred to as our 'assertions'
			
			Weakest-Precondition
				The least restrictive precondition that will garuntee the validity of the postcondition.
			Inference Rule
				Inferring the truth of an assertion  from other assertions..
				IE..
					S1,S2,...,S2	(antecendent)
					____________
					      S			(consequent)
				This rule states that if the top is true then the truth of the bottom can be inferred.
				An axiom is a logical statement assumed to be true.
			
			AXIOMS
				Rule of Consequence
					{P}S{Q},P_prime => P , Q => Q_prime
					___________________________________
					{P_prime}S{Q_prime}
					
					Essentially the post condition can always be weakened and the precondition can always be strenghtened.
					The Rule of Consequence can then be used for us to find the weakest pre-condition when we can tell that
					the left side is in fact not the weakest precondition.
					
					We can represent this simply for a given two statements that..
					{P}S1{Q},{Q}S2{R}
					_________________
					{P}S1;S2{R}
					
					So {R} is the consequence of {P}
					as can be seen by this rule..
					If we decide to we can use this rule to prove an entire program by looking at a final result {R}
					and tracing it back then we can see that the initial {P} results in {R} thus the program is correct.
					
				Assignment Axiom
					True
					_____________
					{Q[target/source]} S {Q}
					
					Thus let us consider an assignment statement
					{S} a = b + 2 {a < 10}
					We can substitute the right statement into the post condition to find the weakest precondition on the left..
					{(b + 2) < 10} a = b + 2 {a < 10}
					{b < 8} a = b + 2 {a < 10}
					
				Conditional Rule
					{P and E} S1 {Q},{P and (not E)} S2{Q}
					______________________________________
					{P} if E then S1 else S2 {Q}
				
					Thus we need to prove it when it is both true and false.
					consider
					if (a < 2) then a = a + 2 else a = a + 1
					if (a < 2) then a = a + 2 {a > 0} else a = a + 1 {a > 0} (weakest precondition will be our base postcondition such as if it were the end of the program that satisfies either statement.)
					{P and (a < 2)} a = a + 2 {a > 0},{P and (not (a < 2))} a = a + 1 {a > 0}
					So now we need to find the weakest precondition that can allows it to be true or false.
					{(a < 2) || (a >= 2)}
					This gives us..
					{(a < 2) || (a >= 2) and (a < 2)} a = a + 2 {a > 0},{(a < 2) || (a >= 2) and (not (a < 2))} a = a + 1 {a > 0}
					or simply..
					{a < 2 || a >= 2} if (a < 2) then a = a + 2 else a = a + 1 {a > 0}
	
				While Rule
					{P and E} S {P}
					_______________
					{P} while E do S {P and (not E)}
					
					If you properly understand the conditional rule then this should come easily.
					The post condition is that the condition for the loop failed.
					Thus the precondition has to be what allows it to tail.
					Consider while (a < 10) do b=b+2;a=a+1 we can plug in our knowns.
					
					{P and (a < 10)} b=b+2; a = a+1 {P}
					___________________________
					{P} while (a < 10) do b=b+2; a = a+1 {P and (not (a < 10))}
					
					To make is easier to read we will collpase some logical statements and represent our statement sequence as S..
					
					{P and (a < 10)} S {P}
					___________________________
					{P} while (a < 10) do S {P and (a >= 10)}

					Thus we need to find a precondition P such that {P and (a < 10)} and {P and (a >= 10)} are both True.
					due to the and comparison we know it should be one or the other so..
					{(a < 10) or (a >= 10)} while (a < 10) do S {(a < 10) or (a >= 10) and (a >= 10) }
					applying Imdepotent Boolean Law
					{(a < 10) or (a >= 10)} while (a < 10) do S {(a < 10) or (a >= 10)}
					{(a < 10) or (a >= 10)} while (a < 10) b=b+2; a = a+1 {(a < 10) or (a >= 10)}
					
					Thankfully this means that due to Rule of Consequence a great many amount of post conditions can be true.(after all how can a be less than 10)
					So tracing back in the program we would likely end up with a post condition like.
					{(a < 10) or (a >= 10)} while (a < 10) b=b+2; a = a+1 {(a = 10) and (a >= 10)}
					Which would still be valid.(and is the natural result of such a loop.)
Chapter 4 Lexical and Syntax Analysis
	4.1 Introduction
		The Lexical and Syntactical Analyzer deal with two different constructs-
			The Lexical Analyzer Deals with small-scale language constructs such as-
				names and literals.
			The Syntactical Analyzer deals with large-scale language constructs such as-
				Expressions, statements, and program units.
		There are three reasons lexical analysis is separated from syntactical analysis-
			1. Simplicity-
				Lexical Analysis techniques are typically less complex than syntactical analysis.
				So separating it from the syntactical analyzer means each module will be less complex.
			2. Efficiency-
				Lexical analysis takes a large amount of compilation time, as such optimizing it will help more
				than optimizing the syntactic analyzer. As a result separating it from the syntactic analyzer
				will make it easier to optimize.
			3. Portability-
				Lexical analysis reads from input files and often needs a means to buffer for that input it 
				may not be platform independant. So separating it means you can keep it separate from what may be
				portable.(Such as the syntactical analyzer.)
	4.2 Lexical Analysis
		The lexical analysis has a very specific job-
			A lexical analyzer is essentially a pattern matcher. It will capture 'lexemes' and produce corresponding 'tokens'
			The output of the lexical analyzer can thus be seen as the input of the syntactical analyzer. During lexical analysis
			white spaces is skipped and ignored.
			Additionally it will take user defined lexemes and convert them into a form that can be used for the compiler.
		There are three approaches to building a lexical analyzer-
			1. Write a formal description of the token patterns in the language using a scriptive language related to regex-
				These descriptions can be used in existing software to generate a lexical analyzer for you.
			2. Design a state transition..
				diagram that describes the token patterns of the language and write a program that
				implements the diagram.
			3. Design a state transition..
				diagram that describes the token patterns of the language and hand-construct a table-driven implementation 
				of the state diagram.
		Vocabulary - State Diagram, Finite Automata, Regular Language -
			State Diagram-
				A directed graph, the nodes of the graph contain state names.
				The arcs are labeled with input characters that cause transitions between states.
				An arm may also include actions for the lexical analyzer when a transition occurs.
			Finite Automata-
				A mathematical machine that can be represented with state diagrams for lexical analyzers.
			Regular Language-
				A class of language(the textbook literally didn't say anything else.)
				A Regular Language have generative devices known as 'Regular Grammars'.
				In this sense the tokens of a programming language are a regular language
				and a lexical analyzer is a finite automoton.
		In simplifying our lexical analysis it's good to group things into common classifications. 
		Because of the branching factor in a state diagram these classifications can reduce branching factor.
		For example given a name (52 characters with both upper and lowercase) we can just generalize this into 'LETTER'
		instead of having to branch for each letter.
		State Diagram of a simplified letter/digit regular language-
			Refer to figure 4.1 
		Note that getChar and nextChar would need a function to ignore white space.
	4.3 The Parsing Problem
		Syntax Analysis is often called 'parsing' so the terms may be used interchangebly.
		Introduction to Parsing-
			Parsers construct parse trees for a program.
			Sometimes like in class we only generate a traversal of the tree and not a tree itself.
			There are two goals of syntax analysis-
				First... 
					the syntax analyzer must check the input program to determine wether it's syntactically correct.
					If an error is found the analyzer must produce a diagnostic messageand recover. That is to say
					that it continues and finds as many errors as possible.
				Second.. 
					it must produce a parse tree or trace the structure of a parse tree for syntactically correct input.
					The parse tree is the basis of translation.
		Important Conventions For Discussing Grammar Symbols and Strings-
				1. Terminal symbols...
					lowercase leters starting at beginning of the alphabet
					(a,b,...)
				2. Nonterminal symbols...
					uppercase letters starting at beginning of the alphabet
					(A,B,...)
				3. Terminals or  nonterminals...
					uppercase letters starting at end of the alphabet
					(Z,Y,...)
				4. Strings of terminals...
					lowercase letters starting at beginning of the alphabet
					(z,y,...)
				5. Mixed Strings(terminals and/or nonterminals)...
					lowercase greek letters
					(alpha,beta,...)
		Parsers are catagorized in two broad classes-
			Top-Down-
				From root down to leaves.
				Leftmost derivation
				The general form of a left sentential form is x(A)(alpha) | (terminal string)(nonterminal)(mixed string)
				A's rules may be A -> bB , A -> cBb,  A -> a
				So the next senential form could be 
				xbB(alpha) or xa(alpha) or xcBb(alpha)
				In order to get the correct input we would have to look at our 'next symbol' and form a 'best fit' for our rules.
				The most common top-down parsing algorithms is the recursive-descent parser which we made in our first few labs.
				A recursive-descent parser is based directly on the BNF of a language.
				The most common alternative to Recursive-Descent Parsing is a "Parsing Table" , both of these are called 
				"LL Algorithms"...
					The first L means Left to Right
					The second L means a leftmost derivation is generated.
			Bottom-Up-
				From leaves up to root.
				Given a right sentential form...
					of (alpha) the parser must determine a substring of (alpha) that must be reduced to lefthand
					to produce the previous senetial form in the rightmost derivation.
					A given form may have more than one RHS from the grammar which complicates parsing.
					The correct one is referred to as the 'handle'.
					Consider the following...
						S -> aAc
						A -> aA | b
						S => aAc => aaAc => aabc
					The answer is still ambiguous.
					To solve this problem the bottom-up parser must look at the symbols on both the left and right side of a possible handle 
					this allows it to make the best fit.
		The Complexity of Parsing-
			Parsing algorithms for unambiguous grammar are complicated and are of the order O(n^3)
			For this reason we sometimes must sacrifice genrality for speed as order O(n^3) is 
			incredibly impractical. ( an O(n) input would be calculated instantly but O(n^3) could take 'hours')
			Commercial compilers are typically O(n)
	4.4 Recursive-Descent Parsing
		Recursive-Descent Parsing Process-
			Review CFG, BNF, EBNF
			Additionally Review our Interpreter 
		LL Grammar Class
			A large problem with this method is representing left recursion.
			To solve this we need to replace it with right recursion. (Like in Lab)
		Pairwise Disjointness Test-
			FIRST(alpha) = {'a' | (alpha) =>* 'a'(beta)}(If (alpha) =>* (epsilon),(epsilon) is in FIRST(alpha))
			In which =>* means 0 or more derivation steps.
			IN ENGLISH...
				FIRST(alpha) is a set 'a' from which alpha has 0 or more derivation steps that produces 'a'(beta)
				but only if alpha has 0 or more derivations that produces epsilon
				where epsilon is in FIRST(alpha)
				(I'll go in more detail if Park asks for it.)
	4.5 Bottom-Up Parsing
		The Parsing Problem for Bottom-Up Parsers
			Consider the following grammar...
				E -> E + T | T
				T -> T * F | F
				F -> (E)   | id
			Because we are dealing with bottom-up left recursion is okay.
			Let's follow some productions. The bracketed sections are the sections being operated on...
				E => [E + T]
					 E + [T * F]
					 E + T * [id]
					 E + [T] * id
					 E + [F] * id
					 E + [id] * id
					 [T] + id * id
					 [F] + id * id
					 [id] + id * id
					 id + id * id
			As previously mentioned there may be more than RHS production.
			So we must find the 'handle' in order to determine the next best action.
			HANDLE DEFINITION-
				(beta) is the handle of the right senetial form (gamma) = (alpha)(beta)w if and only if 
				S =>*.rm (alpha)Aw =>.rm (alpha)(beta)(w)
				Where .rm refers to rightmost derivation and => refers to a derivation.
			PHRASE DEFINITION-
				(beta) is a phrase of the right sentential form (gamma) if and only if 
				S =>*(gamma) = (alpha.1)A(alpha.2) =>+ (alpha.1)(beta)(alpha.2)
				Where =>+ means one or more derivation steps.
				
				(beta) is a simple phrase of the right sentential form(gamma) if and only if 
				S =>*(gamma) = (alpha.1)A(alpha.2) => (alpha.1)(beta)(alpha.2)
			Consider figure 4.3...
				Each internal node can be seen as a phrase.
				id is the only simple phrase. This is because it is derived from a source with only one production. (F)
				On the other hand There is also E , T which are phrases that have more possible productions.
				As a result we climb up the parse tree knowing that id is made from F, F is made from T, thus T must 
				make productions (The correct handle thus can be found now with a simple analysis)
				In this case it was '*' which creates a production T. 
				Now we go back to the original T and see that it is made from E. An analysis determines that the handle is '+'
				so we make the correct production and find that the leftmost is a E finishing our parse.
		Shift-Reduce Algorithms
			Another name for Bottom-Up Parsers because their actions are essentially Shift and Reduce
			They typically employ a stack in this approach.
			Shift can be equated to a push a LHS onto the stack. Whereas a reduce pops off the stack, then pushes onto it 
			a corresponding LHS.
		LR Parsers
			Most LR Parsers use a relatively small program in conjuction with a parsing table that is built for a specific programming 
			language.
			The Canonical LR algorithm had the problem of consuming too much resources.
			Later LR Parsers have two important properties-
				1. They require far less computer resources to produce the required parsing table than the canonical LR algorithm.
				2. They work on smaller classes of grammar than the canonical LR algoirthm.
			There are 3 advantages to LR parsers
				1. They can be built for all programming languages..
				2. They can detect syntax errors as soon as it is possible in a left to right scan.
				3. The LR class of grammars is a proper subset of the class parsable by LL parsers for example...
					Many left recursive grammars are LR but none are LL.
			The main disadvantage of LR is that it is hard to hand produce for a complete programming language.
		PARSE STACK(Will only go over in Park asks)
Chapter 5 Names, Bindings, and Scopes
	5.1 Introduction-
		Imperative Languages are essentially abstraction of the Von Neumann Architecture (About the only important information in this section.)
	5.2 Names-
		Name is used interchangebly with identifier
		Design Issues-
			The following are primary design issues for names-
				1. Are names case sensitive?
				2. Are the special words of the language reserved words or keywords?
		Name Forms-
			A name is a string of characters used to identify some entity in a program.
			Fortran 95+ allows up to 31 characters.
			C99 has no length limitation on it's internal names but only the first 63 are significant.
			External names are limited to 31 characters.
			Names in most programming languages have the same form:
			letters,digits, and underscores. Although underscores are much less popular now.
			It has been replaced by 'Camel Notation' in which all of the words except for the first are capitalized.
			ie: 'myStack'
			This issue is a programming style issue, not a language design issue.
			
			All variable names in PHP begin with a dollar sign.
			In Perl the character at the beginning of a variables name determines it's type.($,@,%)
			In Ruby @var would be an instance variable wheras @@ would be a class variable.
			
			In case sensitive languages however var, VAR, and Var are three separate names. This can be a detriment to readability
			and in the case of built-in function affect writability as well.
		Special Words-
			Reserved Words: Held by the program, cannot be changed.
			Keyword: A word that is special in only certain contexts.
	5.3 Variables-
		A program variable is an abstraction of a computer memory cell.
		A variable is broken up into six attributes of four of them are-
			Name- 
				Discussed Previously
			Address- (l-value)
				The memory location of the variable.
				Aliasing means that you can have values that refer to the same memory address.
			Type-
				Refers to the types and range of values it can hold.
			Value- (r-value)
				The contents of the memory cell.
	5.4 The Concept of Binding
		A binding is an association between an attribute and an entity.
		The time at which a binding takes place is called 'binding time' 
		* the multiplication symbol is usually bound at language design time.
		A data type such as 'int' is bound to a range of values at implementation time. (As in C)
		At compile time a vriable is bound to a particular type.
		A variable may be bound to a storage cell when it is loaded into memory or at runtime when it is declared.
		A call to a library subprogram is bound to the subprogram code at link time.
		Consider the following Java statement...
			count = count + 5;
			
			the type of count is bount at compile time.
			the set of possible values of count is bound at compiler design time.
			the meaning of the operator + is bound at compile time when the types of its operands are determined. 
			The internal representation of the literal 5 is bound at compiler design time.
			The value of count is bound at execution time with the statement.
		Binding of Attributes to Variables-	
			A binding is static if it occurs before runtime and remains unchanged throughout program execution.
			If the binding occurs during runtime and/or can change at runtime then the binding is dynamic. 
		Type Bindings-
			Static Type Binding-
				Explicit Declaration is listing variable names and their particular type.
				Implicit Declaration is using some convention to determine the type. (for example, lowercase is integer and uppercase is real)
				If done wrong it can hamper readability regardless of writing convienence. 
				A good way of doing this can be to associate symbols. ie: $,@,% in perl.
				"Type Inference" is a form of implicit binding that uses context to construct the type. For example in C#.
				var variable = "Hello World"
				would bind varable's type to a string.
			Dynamic Type Binding-
				Best demonstrated with an example. Take Python for example...
					var = "Hello World"
					var = 2
					var is now bound to 'string' and then is bound to 'integer'
				There are two disadvantages to this approach-
					1. Less reliability due to hampered error detection..
						Converting to an inappropriate type can be undetected.
					2. Slower programs
						As it has to be done at runtime dynamic binding has to perform additional actions to complete conversions.
		Storage, Bindings, and Liftime-
			Allocation: The process through which a memory cell is bound to a variable.
			Deallocation: The process of taking a memory cell that is not being used and placing it back into free memory.
			Liftime: The time during which a variable is bound to a specific memory location.
			It is easiest to split variables into 4 catagories..
				Static Variables-
					These are bound to memory cells before program execution ends.
					They remain bound until the program ends.
					This lifetime can be convienent for global variables.
					Alternatively subprograms needs to know it's previous history.
					In which case it's values should not reset.
					"One advantage is increased efficiency due to direct addressing"
					"One disadvantage is reduced flexibility"
					A language where all values are global would not be capable of recursion.
					static values cannot share memory either.
					Think of the c++ function..
						void foo(){static int i = 4; i++; cout << i << endl;}
					At first it prints 5, if called again it prints 6, and so on.
				Stack-Dynamic Variables-
					Types are statically bound, however what they are holding is determined when
					they are 'elaborated' upon at runtime.
					Think of the C++ function...
						void foo(){int i = 4; i++; cout << i << endl;}
					It will always print 5, it knows it must be an int, however it's storage is elaborated upon when the program
					reaches it.
				Explicit Heap-Dynamic Variables-
					Nameless abstract memory cells that are allocated/deallocated explicitly at runtime.
					Their lifetime is until deallocated.
					in C++ this would be done with new.
					ie: node *a = new node();
					However to release it we would need to deallocate it..
					delete a;
					but we also need to resolve the memory taken by the pointer.
					a = NULL;
					This can be used to construct linked lists, trees, and the like.
				Implicit Heap-Dynamic Variables-
					ie: Javascript
					highs = [74, 84]
					would bind it to the heap just based on the value.
	5.5 Scope
		The range of statements in which a variable is visible.
		A variable is visible if it can be referenced.
		Static Scope-
			A variable/function can have it's scope determined by location.
			If it's declared in foo() then bar() cannot see it and vice versa.
			However some allow nested scopes...
			foo(){
				a = 2
				foobar(){doStuff}
			}
			foobar would still see a.
			On a failure to find it continues to look at ancestors. 
			If foobar wanted to increment 'b' it would look in itself, then in foo() then in the global scope.
			At which point it's not found and returns an error.
		Blocks-
			A block structured language can construct it's own static scope when it pleases.
			For example in C++ you can do the following...
				int main(){
				int a = 4;
					{
					cout << a << endl;
					int a = 3;
					cout << a << endl;
					}
				cout << a << endl;
				}
			It will print out 4,3,4
			This is because we made a new static scope.
		Declaration Order-
			Location Declarations must be performed,
			For example C89 they msut be done at beginning of function blocks.
			However in C99 you can do it anywhere. 
			Or in a for loop in C-based languages you can declare a a variable that will last throughout the for loop.
		Global Scope-
			Declared outside of the function scope results in variables being globally accessible.
			Another way of thinking about it is they can be accessed as easily as functions.
			So long as something is not in the way it can be seen.
			If something is in the way such as in C++
			you can access the global var with scope syntax.
			::var
		Evaluation of Static Scoping-
			In order to prevent continued restructuring of programs programmers are encouraged to make liberal use of 
			global values which can make the programs messier than they intended to be.
		Dynamic Scope-
			In python for example we can perform nesting like so...
				def foo():
					a = 2
					def bar():
						b = 2
						a += 1
						foobar()
					def foobar():
						a +=1
						b +=1
				foo()
				bar()
			foo is called.
			a is set to 2.
			bar is called.
			b is set to 2.
			a cannot be found so it checks caller main, nothing is in main so it checks parent function.
			It finds it and increments a to 3.
			it calls foobar
			a cannot be found so it checks it's caller, it cannot be found so it checks its parent function and increments a to 4.
			b cannot be found so it checks its caller. There it finds b and increments it to 3.
		Evaluation of Dynamic Scoping-
			Less reliable programming because access can be confusing.
			Programs become almost unreadable to human eyes.
			On the other hand this creates useful constructs that need to be maintained less often or may be 
			easily maintained if some human were to somehow look at it without going insane.
	5.6 Scope and Lifetime
		Expanding on previous sections, lifetime can be further separated into subprogram lifetime and scope lifetime.
		They are not related, because a scope of a function ends does not means that variables passed in are destroyed(unless a copy is made.)
		On the other hand the values decalred inside the function are destroyed.
	5.7 Referencing Environments
		The collection of all variables that are visible in a statement.
	5.8 Named Constants
		C++ example,
		const int size = 100;
		only instantiated once. 
		In addition this can be used reduce work. (for example many arrays of arr[100] to another size would just have to change the single int size.)
Chapter 6 Data Types
	6.1 Introduction
		A data type refers to a collection of data and values and predefined oeprations on those values.
		Abstract Data Types are user implemented types whose implementation are hidden from those using it.
		A descriptor is a collection of attributes about a variable.
	6.2 Primitive Data Types
		These are data types that are not derived from subtypes.
		Numeric Types-
			Integer-
				Has varying lengths- byte(8 bits),short(2 bytes),int(2 shorts), and long.
				Some programming languages have a specialized long type that can hold numbers of unlimited length.
				Negative numbers are held onto by 2's complement.
			Floating-Point
				Floating Points approximate real numbers.
				Float is the normal size. There is also the 'Double' whichr has double the length.
			Complex
				Some programming languages support complex numbers ie: (7 + 3j)
			Decimal
				These hold a fixed amount of 'decimal bits' with the rest dedicated to the exponents.
			Boolean
				Hold True or False, however accessing a single bit isn't always efficient to access so its usually stored in a byte.
		Character Types-
			Characters are an encoded numeric type to represent character representations.
			Look up ASCII and UTF for more.
	6.3 Character String Types
		A character string type is one which contains sequences of characters.
		Design Issues-
			Should it be a primitive type? (It can be made of characters so it doesn't have to.)
			Should strings have fixed or dynamic length?
		Strings and their Operations-
			Assignment: the ability to directly assign a string.
			Catenation: putting strings together.
			substring reference: able to get a range of a string to view a 'slice' of it.
			comparison: being able to directly compare the strings logically.
			pattern matching: getting pieces of the string and such. Look up REGEX for more. (Don't hurt your brain too much if you havent used em before.)
			String Length Options-
				Static: The string has to be remade each time with it's new length.
				Dynamic: The length can vary. 
			Evaluation-
				It's hard to justify NOT having strings as primitives.
	6.4 User-Defined Ordinal Types
		An ordinal type is one whose values can easily be expressed as integer values.
		These are separated into two types-
			Enumeration Types-
				An enumeration type is one in which all values are enumerated(ordered) in definition take for example-
					days {mon,tue,wed,thu,fri,sat,sun}
				If someone were to ask is mon < tue then it would return true because it comes before.
			Subrange Types-
				A subrange type is a contiguous subsequence of an ordinal type.
				IE: 12..14
	6.5 Array Types
		An array is a group of alike things located next to each other.
		Elements are typically accessed with a subscript. IE A[i]
		Implementation of Array-
			Begin by allocating a location in memory. We will call this A
			1. We will be passed in a literal which will represent our size and allocate space on the heap.
			2. We will increment initializing each space so it wont get used.
			3. Once we have reached the end our array is initialzed and the size can be cached.
			4. Accessing an element is as simple as &A + size_of(*A) * i
				This is because *A dereferences to A[0] which contains our type size.
				Additionally this provides a starting location hence why we start at &A.
		Multidimensional Arrays-
			Remember Park's example.
			[1,2,3,4,5,6,7] is one dimension
			2 is 
			[[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
			3 is
			[[[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]],...]
			4 is another level of nested complexity and so on.
	6.6 Associative Arrays
		An unordered collection of elements that are indexed by an equal number of keys.
		The idea is that the keys compute the location of the value.
		Because of this look up and insertion tend to be constant if done well.
		Refer to our unordered_map lab for usage.
	6.7 Record Types
		Elements ensured to be next to each other.
		Implementation specific, hard to explain. Look it up if Park asks us.
	6.8 Tuple Types
		Tuples are immutable sequences of data types, they do not have to be the same data type.
	6.9 List Types
		Another one that's hard to explain, mostly lisp specific. Can normally be represented as an array.
		An exception to the array type is that they may be allowed to have different types and it may be possible
		to have an empty list []. 
	6.10 Union Type
		A type whose variable may store different types at different moments in the program.
		The list type for example if mutable is an example of a Union Type.
	6.11 Pointer and Reference Types
		A variable that can hold a memory address or 'nil'
		Dangling Pointers-
			A dereference pointer must be set to NULL or nil afterward otherwise if it tries to reallocate data it will do so 
			onto the address it is pointing which may have been taken over by some other part of the program.
		Heap Managament(Garbage Collection)-
			Lazy-	Performs when the heap is full or after some criteria is fulfilled.
				Mark Sweep-	
					Pass through activation record marking everything that can be seen.
					Afterward pass through heap and deallocate everything that you didn't mark.
				Copying Collection-
					Store References and occasionally depth first search through and remove what's not in the activation record.
			Eager-  Performs on every allocation.
				Reference Count-
				Keep count of references on every object. If it ever reaches 0 deallocate it.
				Cannot detect circular references.
	6.12 Type Checking
		Static Type Checking like we did in the semantics section is done at compile time. 
		Dynamic Type checking has to perform such actions at runtime.
	6.13 Strong typing
		A language is 'strongly typed' if type errors are always detected.
	6.14 Type Equivalence
		Name type equivalence-
			Two variables have have equivalent types if they are defined in 
			the same declaration or in declarations that use the same name type.
		Structure type equivalence-
			Two variables have equivalent type if their types have identical structures.
		A derived type is a new type that is based on some previously defined type.
	6.15 Theory and Data Types
		IGNORING UNLESS PARK ASKS
Chapter 7 Expressions and Assignment Statements
	7.1 Introduction
		Refers to BNF 
	7.2 Airthmetic Expressions
		When implementing we have to consider the following-
			What are the oeprator precedence rules?
			What are the operator associativity rules?
			What is the order of operand evaluation?
			Are there restrictions on operand evaluation side effects?
			Does the language allow user-defined operator overloading?
			What type mixing is allowed in expressions?
	7.3 Operator Overloading
		Overriding what operators do so that they can be used in ways unexpected in the original language.
		Useful for user defined types, although it can affect readability.
	7.4 Type Conversions
		Narrowing Conversions converts to a type which can hold less.
		Widening Conversion converts to a type which can hold more.
	7.5 Relational and Boolean Expressions
		Relational operators: <,<=,>,>=
		Boolean Operators: ||, && , ==, !=
		PRECEDENCE FROM HIGHEST TO LOWEST-
			postfix ++  , --
			unary +, - , prefix ++, --, !
			*, /, %
			binary +, - 
			< , > , <=, >= 
			=, !=
			&&
			||
	7.6 Short Circuit Evaluation
		Determining the result without performing the total computation.
		For example given (0) * 123123 * 123 * 123
		Once it sees the initial 0 it knows it can stop computing as long as it sees a *,/, or & operator as it'll collapse to 0.
		This applies to logical/relational operations as well.
		check the given example...
			(1 >= 2) && (1==1)
		The moment it sees "False" AND -----
		It knows it's answer already. This property can be used to make certain checks such as if node->next == NULL before checking node->next->key.
	7.7	Assignment Statements
		Simple Assignment-
			Utilizing a simple operator such as = in order to perform assignment.
			If = wants to be used for equality then an alternative assignment needs to exist.
		Conditional Targets-
			Perl allows conditional assignment.. OH DEAR GOD... WHY...
				($flag ? $count1 : $count2) = 0
				Is the same as if flag: count1 = 0 else count2 = 0
		Compound Assignment Operators-
			ie: a+=2 , b/=a
		Unary Assignment-
			ie: a++, ++a
		Assignment as an Expression-
			REFER TO OUR EARLIER LAB WITH getChar()
		Multiple Assignment-
			(a,b,c) = (1,2,3)
			is the same as 
			a = 1
			b = 2
			c = 3
	7.8 NO
Chapter 8 Statement Level Control Structures
	8.1 Introduction
		Control Statement: A means to move along different instruction paths.
		All algorithms can be formed with only two control statement types.
		One to choose between two different paths (if)
		and controlled iterations(while)
		Control Structure: a control statement and the collection of statements it's execution controls.
	8.2 Selection Statements
		A selection statement provides the means for there to be two or more execution paths in a program.
		Two-Way Selection Statements-
			If control_expression
			then clause
			else clause
		REVIEW AMBIGUOUS ELSE FROM PREVIOUS SECTIONS
		Multiple-Selection Statements-	
			IE: Switch
			Though this can be implemented with other structures such as nested if/ifelse
	8.3 Iterative Statements
		An iterative statement is one that causes a statement or collection of statements to occur
		zero, one, or more times.
		It's often called a 'loop'
		The 'body' is the collection of statements that are iterated.
		There are two ways to test if a loop is occuring...
			Pretest: Test happens before the loop.
			Posttest:Test happens after the loop (has to occur atleast once)
		Counter-Controlled Loops-
			Imagine For loops with the classic for(int i = 0; i < num; i++)
			or their while equivalents.
		Logically Controlled Loops-
			These loops persist until a condition is fulfilled of a boolean nature.
		User-Located Loop Controls Mechanics-
			If pretest or posttest are both unsatisfactory many languages have constructs such as 
			the 'break' statement that will allow you to test in the middle of a loop and then exit.
	8.4 Unconditional Branching
		Unconditional Branching transfers control to another part of the program.
		An example is the 'goto' command or the jump command.
	8.5 Guarded Commands
		The structure for this is essentially...
			if <expression> -> statement
			if <expression> -> statement
		and so on.
		This instead looks for a best fit for command flow.
		Haskell is an example of a language that uses these constructs.
	8.6 Conclusions
		This section just summarizes the chapter.
Chapter 9 Subprograms
	9.1 Introduction
		Process abstraction is the use of functions/methods/subprograms in order to hide low level details thus 
		allowing more to be seen about the logical structure of the program.
	9.2 Fundamentals of Subprograms
		General Subprogram Characteristics-
			Each subprogram has a single entry point.
			The calling program is suspended until completion of the subprogram.
			When the subprogram finishes control returns to the caller.
		Basic Definitions-
			subprogram definition: interface to and actions of the subprogram abstraction.
			subprogram call: explicit request for a subprogram to be executed.
			Once called it is said to be 'active'
			subprogram header: the first part of a subprogram definition IE-
				def adder(parameters):
		Parameters-
			Subprograms can get parameter through several ways.
			Pass by value creates a copy of the data.
			Pass by pointer (*) is a value that 'points' to the value that is being passed so it becomes mutable.
			Pass by reference (&) is the location of the value in memory so it becomes mutable.
			They can also recieve them globally.
			Definitions-
				formal parameters: the parameters in the subprogram header, the function reads them as a 'certain name'
				actual parameters: the parameters that are passed in when you cann the function. their 'true name'
				positional parameters: the tendency for parameter binding between formal/actual to be done based on order passed in versus order represented.
				keyword parameters: parameters can be passed in any order (and as many as you want depending on implementation) by binding to existing keywords.
		Procedures and Functions-
			There are two distinct catagories of subprograms-
				Procedures-
					Do not return values.
					Procedures can make changes to the program by editing globals are being passed parameters.
				Functions-
					Return values.
					While similar it has a more.. 'mathematical' purity.
	9.3 Design Issues for Subprograms
		Are variables statically or dynamically allocated?
		How should parameters be passed?
		Are actual types checked against formal types?
		Can subprogram definitions be nested?
		If it can be nested can it have closures?(a nested subprogram and it's referencing environment that can be called anywhere.)
		What is correct referencing for a passed parameter in a nested environment?
		Can it be overloaded?(same name for different functions)
		Can it be generic?(Able to take in multiple forms of data)
	9.4 Local Referencing Environments
		Local Variables-
			Variables defined in the subprogram with a lifetime of the current execution of the subprogram.
			Stack Dynamic Local Variables also allow recursive definitions.
			The disadvantage with this approach is time costs in moving the data around (allocation, deallocation)
			Direct addressing cannot occur because the state of the stack needs to be known to access the variables.
			Static Variables get around this but are only helpful if the history of previous exeuctions of the subprogram are important.
	9.5 Parameter Passing Methods
		These are ways in which values are passed to subprograms.
		Semantic Models of Parameter Passing-
			Formal parameters are characterized by one of three distinct semantics models-
				1. In mode:   They can recieve data from the corresponding actual parameter.	(pass by value)
				2. Out mode:  They can transmit data to the actual parameter.					(pass by result)
				3. Inout Mode:They can do both.													(pass by reference/pointer , pass by name)
		Pass by Name-
			These work by basically taking the variable's context and changing it directly as an extension to the program.
			Macro Expansion is one such example of this occuring.
		Implementing Parameter Passing Methods-
			I will cover this if park asks for it.
		Type Checking Parameters-
			Same here.
		Multidimensional Arrays as Parameters-
			Take for example..
				void fun(int matrix[][10]){
				...}
				void main(){
				int mat[5][10]
				...
				fun(mat);
				}
			First problem, the function doesn't know how many rows, only how many columns.
			Second problem, this function works only for a matrix with 10 columns.
			You will need separate function declarations in order to accomidate different sizes in addition to having the rows as a formal parameter.
			We can solve this problem with pointer arithmatic.
			Let's pass in the matrix as a pointer...
				void fun(int *matrix, int rows, int columns){
					....
				}
			We can access elements with the following formula.
			address(mat[i, j]) = address(mat[0,0]) + i * number_of_columns + j
			Or in c++ form,  *(matrix + (row * column) + col) = x
			It's hard to be read but you can wrap it up in a macro to solve readability.
			In Java the array can be passed in directly and arrays / array elements know their length.
			Java Example...
				int func(int matrix[][]){
					matrix.length....
					matrix[0].length....
				}
			Much easier to work on. std::vector in C++ behaves in this way.
		Design Considerations-
			Efficiency and wether one-way or two-way transfers are needed.
	9.6 Subprograms as Subprogram Parameters*****************************************
			Referencing Environments Choices for Parameters-
				1. Shallow Binding-
					The environment of the call statement that enacts the passed subprogram.
				2. Deep Binding-
					The environment of the definition of the passed subprogram.
				3. Ad-Hoc Binding-
					The environment of the call statement that passed the subprogram as an actual parameter.
			Consider the following Java example...
				function sub1(){
					var x;
					function sub2(){
						alert(x);
					};
					function sub3(){
						var x;
						x = 3;
						sub4(sub2);
					};
					function sub4(subx){
						var x;
						x = 4;
						subx();
					};
					x = 1;
					sub3();
				}
			Consider sub2 when it is called in sub4. For shallow
			binding, the referencing environment of that execution is sub4, so the
			reference to x in sub2 is bound to the local x in sub4, the output of the
			program is 4. For deep binding, the referencing environment of sub2’s is sub1, so the reference to x in 
			sub2 is bound to the local x in sub1, and the output is 1. For ad hoc binding, the binding is to the local x in
			sub3, and the output is 3.

	9.7 Calling Subprograms Indirectly
		Function Pointers
	9.8 Overloaded Subprograms
		Overloaded subprograms shouldn't be ambiguous that way it can be inferred which can be accessed.
		void fun(float b = 0.0);
		void fun();
		is bad because both can be called with empty parameters.
		void fun(float b);
		void fun(); 
		is fine because one requires a parameter and the other doesn't.
	9.9 Generic Subprograms
		Polymorphic Subprograms can take data of many types and operate on them.
		Overloaded Subprograms are one way of dealing with it and are referred to as 'ad hoc polymorphism'
		Languages with pbject-oriented often have inheritance and derivated based types. These can be used for 
		'subtype polymorphism'
		'Paramatric Polymorphism' works by generic parameters and essentially behave the same just with different data.
		ie: an add function could add 2 ints, 2 floats, a float and an int, or concatenate strings(overloaded +)
	9.10 Design Issues for Functions
		Functional Side Effects-
			Variables passed into a function should be by value whenever possible.
			This is because values can change unintentionally and alter the behavior of your program.
			It also makes your subprogram less reusable if it can change data willy-nilly.
		Types of Returned Values-
			Some languages choose to restrict return types wether due to implementation or safety.
		Number of Returned Values-
			In most cases only a single value can be returned but in certain languages such as Python or Ruby 
			you can return multiple parameters.
			def func(): return 1,2,"hello"
			will return the tuple over that data.
			Ruby would return an array.
	9.11 User-Defined Overloaded Operators
		The ability for the user to extend the language by giving new meaning to operators with certain user-defined types.
	9.12 Closures
		A closure (lambda expression) can be seen as an anonoumys function that can be made and accessed on the fly.
	9.13 Coroutines
		Coroutines are functions whose entry points may occur in the middle. These are done by being 'history sensitive' and using static values.
		Instead of 'calling' a Coroutine you simply 'resume' it.
		They can resume eachother and communicate back and forth. For this reason it is referred to as 'quasi concurrency'.
Chapter 10 Implementing Subprograms
	10.1 The General Semantics of Calls and Returns
		"Subprogram Linkage"-
			The subprogram call and return operations as a whole.
		Subprogram calls have numerous actions associated with it-
			The implementation of parameter passing is needed.
			If Local Variables are not static then the call must allocate storage for locals declared in the sub program then bind them.
			It must save the execution status of the calling program.(All the information to resume the caller when the callee is done.)...
				This includes Register Values, CPU status bits, and the environment pointer EP.(Which is used to access 
				parameters and local variables during subprogram execution.)
			The call also must  make sure that control returns to the proper place once the subprogram if finished executing.
		Subprogram returns are much simpler-
			If the subprogram return is in out mode or inout mode and are implemented by copy 
			then the first action of the return process is to move the local values to the actual parameters.
			Next it must deallocate storage used for local variables and then restore the execution status of the 
			caller. Lastly control is returned to the caller.
	10.2 Implementing "Simple" Subprograms
		'Simple' Subprograms have the following charactersitics-
			Subprograms cannot be nested.
			All local variables are static.
		The semantics of a call in a simple subprogram is as follows...
			1. Save the execution status of the current program unit.
			2. Compute and pass the parameters.
			3. Pass the return address to be called.
			4. Tranfer control to the called.
		The semantics of a return in a simple subprogram is as follows..
			1. If pass-by-value-result or out-mode parameters, the current values are moved to or made avaialable to the corresponding values.
			2. If the subprogram is a function the functional value is moved to a place accessible by the caller. 
			3. The execution status of the caller is restored.
			4. Control is transferred back to the caller.
		The call and return actions require storage for the following...
			1. Status information about the caller.
			2. Parameters
			3. Return address
			4. Return value for functions.
			5. Temporaries used by the code of the subprograms.
		"Activation Record"-
			The format or layout of the noncode part of the program.
		"Activation Record Instance"-
			A collection of data in the shape of an activation record.
		Activation Record for Simple Subprograms-
			[Local Variables]
			[Parameters     ]
			[Return Address ]
		"Linker"-
			Part of the operating system which puts various programs and subprograms together into one executable.
		Example Code and Activation Records of a program with simple subprograms-
			Main-[Local Variables]\
				/[Local Variables] \
			  A-|[Parameters     ]  \
				\[Return Address ]   \
			    /[Local Variables]    \_Data 
			  B-|[Parameters	 ]    /
			    \[Return Address ]   /
				/[Local Variables]  /
			  C-|[Parameters     ] /
			    \[Return Address ]/
			Main-[               ]\
			   A-[				 ] \_Code
			   B-[				 ] /
			   C-[				 ]/
	10.3 Implementing Subprograms with Static-Dynamic Local Variables
		An advantage of the Dynamic aspect is a support for recursion.
		Additional Complexities in Linkage-
			Compiler must generate code to cause implicit allocation and deallocation of local variables.
			Recursion adds the possibility of multiple simultanious activations of a subprogram-
				The only limit on instances of a subprogram is computer memory. As a result
				there must be an activation record for each instance. (It can no longer be static)
		Static-Dynamic Activation Record-
			[Local Variables]  .
			[Parameters     ] /|\ Stack top
			[Dynamic Link   ]  |
			[Return Address ]
		Return Address vs Dynamic Link-
			Return Address typically consists of a pointer to the instruction following the call in the caller.
			The dynamic link is a pointer to the base of the activation record instance.
		Dynamic Links in Static and Dynamic Scopes-
			In static languages the link provides traceback information for when errors occur.
			In dynamic languages the link provides access to non-local values.
		Consider the following functions-
			void sub(float total , int part){
			int list[5];
			float sum;
			...
			}
		The corresponding activation record is...
			[Local         ]sum
			[Local         ]list[4]
			[Local         ]list[3]
			[Local         ]list[2]
			[Local         ]list[1]
			[Local         ]list[0]
			[Parameter     ]part
			[Parameter     ]total
			[Dynamic Link  ]
			[Return Address]
		This form of an activation record is known as the "runtime-stack"
		The EP(Execution Pointer)- 
			It intially points to the base of the currently activated subprogram.
			When a subprogram is called the current EP location is saved as the dynamic link.
			Upon return from a subprogram the top is set to the value of the current EP minus 1.
			The EP is then set to the dynamic link.
			This effectively removes the top activation record.
			(If applicable consider how we handle functions in 80x86 assembly.)
		The Caller Actions-
			1. Create an Activation Record Instance
			2. Save the execution status of the current program unit.
			3. Compute and pass the paramters.
			4. Pass the return address to the called.
			5. Transfer control to the called.
		The Prologue(Pre-Execution) Actions-
			1. Save the old EP in the stack as the dynamic link and create the new value.
			2. Allocate Local Variables
		The Epilogue(Post-Execution) Actions-
			1. If there are pass-by-value-result or out-mode parameters move their current values to the corresponding actual parameters.
			2. If a function move the functional value to a place accessible to the caller.
			3. Restore the stack pointer by setting it to EP - 1 and set EP to the old dynamic link.
			4. Restore the execution status of the caller.
			5. Transfer control back to the caller.
		As practice you can set up recursive calls and trace the activation record including links.
		"Dynamic Chain" / "Call Chain"-
			The collection of dynamic links present in a given stack instance.
	10.4 Nested Subprograms
		Essentially this is having subprograms inside your subprograms. 
		"Static Link"-
			A link to the ancestor function.
			Imagine... 
				foo():
					a = 2
					bar():
						print a
						foobar():
							a+=1
			In this case the static pointer is from bar() to foo().
			In addition foobar's static pointer is to bar() which it cannot find a at.
			As a result it has to look at bar's static pointer where it can find a in foo.
		"Static_Depth"-
			an integer associated with a static scope that indicates how deeply it is nested compared to the outermost.
		"Nesting_Depth" / "Chain_Offset"-
			The difference between the current depth and the accessible scope.
	10.5 Blocks
		In C-based languages we can do the following...
			main(){
			int a = 2;
			{
				int a = 3;
				cout << a << endl;
			}
			}
		3 will be printed.
		This creates it's own static scope.
		In languages that utilize static scopes for its subprograms we can 
		simply treat them as parameterless subprograms with an implicit call. 
		When not the values are simply pushed onto the stack and then removed afterward. (In this sense it can be seen as 
		an extension of the current activation record.)
	10.6 Implementing Dynamic Scoping
		NOT UNLESS IT'S ON THE TEST
		Deep Access-
			If local variables are stack dynamic and are part of the activation records in a dynamic-scoped language
			references to nonlocals can be resolved by searching through activation-record instances of other sub-programs
			In this case we search through the dynamic links in order to determine variable access.
			Basic example to illustrate this..
				You have two programs participating in recursion.
				func():
					int b = 2;
					foo();
				foo():
					int a =0;
					b+=1;
					bar();
				bar():
					int b =0;
					a+=1;
					foo();
			Let's ignore that this particular recursion never ends and look at variable accessibility.
			When func() is called foo() initializes a and then increments the b in func().
			Afterward it calls bar() which initializes b and increments the a in foo(), then calls foo()..
			At this point they will be cyclically declaring vairables for eachother to access. 
			In this case it's the caller / callee relationship that decides non-local access. 
		Shallow Access-
			In the Deep Access scenario what if only one variable name could be binded to a variable at a time?
			This is the concept behind Shallow Access.
			In this situation if func() declared bout a and b then foo() and bar() would just alternate incrementing func()'s variables.
Chapter 11 Abstract Data Types and Encapsulation Constructs
	11.1 The Concept of Abstraction
		"Abstraction"-
			The view or representation of an entity that includes only the most significant
			attributes.
			
			A simple example, say we make this generalization, a 'bird' has two wings, two legs, a tail, and feathers.
			Then we can simply say a crow is a bird without assigning those attributes each time.
		Abstraction for programming is thus ways to reduce the complexity of our job as programmers.
		There are two types of abstraction in programming and that is process abstraction and data abstraction.
		We've explored process abstraction already-
			Subprograms allow the hiding of implementation so instead of the algorithm you can just see something like
			sort(list)
	11.2 Introduction to Data Abstraction
		"Abstract Data Type"-
			An enclosure that holds primitives and/or other Abstract Data Types
			that contains subprograms for operating on them.
		"Object"-
			An instance of an Abstract Data Type.
		Existing Abstract Data Type Example-
			Floating-Point implementations are hidden and instead use common operations.
			In this regard Floating-Point can be seen as an Abstract Data Type.
		User-Defined Abstract Data Types-	
			A user-defined type should contain the same characteristics as language types..
				1. A type definition that allows declarations of variables of the type. (while hiding what it represents.)
				2. A set of operations for munipulating the type.
		Formally Defined "Abstract Data Type"-
			A data type that follows the two following conditions..
				1. The representation of objects of the type is hidden from program units that use the type.
				So the only available processes to it are those defined in the type's definition.
				2. The declaration of and protocals of operation of are contained in a single syntactic unit.
				The Type's interface does not depend on the representation of the objects or the implementation
				of the operations.
				Other program units are allowed to create variables of the defined type.
		"Clients"-
			Program units which are utilizing the Abstract Data Type
		Information Hiding of this type increases reliability and reduces the range of code that needs to be checked and corrected.
		"Accessors"-
			These are split into two groups...
			"Getters"-
				Methods for accessing data members if the Client needs them.
			"Setters"-
				Methods for changing data members if the Client needs them.
		Accessors have three advantages...
			1. Read-Only access can be defined by only providing a getter.
			2. Constraints can be set in the setter so that data stays valid.
			3. The actual implementation of the data member can be changed without affecting the Client.
	11.3 Design Issues for Abstract Data Types
		Consider the following C++ code..		
			class foo{
			public:
			type b;
			const int get_a(){return a;}
			private:
			int a;
			int maxRangeSum(int);
			}
		Here we have wrapped together in the syntactic unit "class"
		This syntactic unit needs to be able to facilitate public/private access/visibility 
		as well as support other declared types as well as primitives and even subprograms in either scope.
		This allows us to make full use of process abstraction to facilitate the development of our data abstraction.
	11.4 Language Examples
		This section provides examples in Ada,C++,Objective C, Java, and Ruby.
		It may be just as effective to look up these implementations if we need to online
		than to use the textbook. 
	11.5 Parameterized Abstract Data Types
		This refers to "Generic Programming"
		In this chapter there are Generic Programming examples for Ada, C++, Java, and C#.
		Once again online resources may be just as effective for this section.
	11.6 Encapsulation Constructs
		When a program gets too large two issues may arise..
			1. There may be too much information to be organized on an intellectual level.
			2. Recompilation becomes slow.
		An 'Encapsulation' refers to encapsulating the information separately. In this state it can be precompiled and 
		handled by the linker in the future.
		Encapsulation in C-
			In C we use the #include<head_name>
			to bring in header files.
			This allows type checking between the two files as well as determining which information is actually needed.
			Include operates as a 'copy/paste' that will copy the contents of the header file into the program.
			Issues arise in that modules can simply be hand-copy pasted in, otherwise Clients could be using outdated headers/implementations
			without realizing it has been changed. 
		Encapsulation in C++-
			Refer to online usage of the 'friend' pointer 
			It is essentially C with the added complexity of templates and classes.
		Ada-
			Look online, it is essentially an automated version of C++'s friends constructs.
		C#-
			Eh I don't get these, im too inexperienced when it comes to this language. 
			Look online if park asks for it.
	11.7 Naming Encapsulations	
		"Naming Encapsulation"-
			A way to enforce naming conventions into a bundle
			so as to prevent confusion between developers.
		C++ Namespaces-
			EXAMPLE-
				namespace ex{
				int a;
				int b;
				}
				
				To access a and b you would do so with..
				ex::a and ex::b respectively.
				If you want it to be native to your program(for writability purposes) you could
				using namespace ex;
				then you could access them simply with a and b respectively.
				If you have written C++ programs you have likely used "using namesapce std;"
		Java Packages-
			packages are a lot like namespaces but everything within could be seen as 'friends'
			the package declaration must appear in the first line of a file ie: "package stkpkg;"
			These values can be accessed for example an Abstract Data Type...
			stkpkg.stack
			or a data member of stack..
			stkpkg.stack.top
			As this can make things confusiong you can simply "import stkpkg.stack;"
			which will allow you to now simply just 
			stack.top.
			
			If we wanted to just outright import everything in the package we could.. "import stkpkg.*;"
			Then we could utilizie everything just like in the previous stack example.
		Ada Packages-
			with Ada.Text_IO;
			Ada.Test_IO.put;
			
			vs
			
			use Ada.Text_IO;
			put;
		Ruby Modules-
			Ruby modules work by allowing the defining of constants(through all caps ie: PI = 3.14)
			methods can also be held. In this sense Ruby separates it's object oriented encapsulation from its functional encapsulation.
Chapter 12 Support for Object Oriented Programming - (FOCUS SOLELY ON C++)
	C++ (Park's Notes Version)
		Class/Struct Names are the Type
		Class-
			All members are private by default.
			Example
				class stack{
					...
					char pop();
					...
				};
		Struct-
			All members are public.
		Struct/Classes have the following capabilities-
			Constructors / Destructors (Constructors can be overloaded)
			This allows easier data management of members and intiialization with parameters.
Chapter 13 Concurrency
	13.1 Introduction
		Concurrency can occur at four different levels-
			Instruction Level-
				Executing two or more machine instructions simultaniously.
			Statement Level-
				Executing two or more high level statements simultaniously.
			Unit Level-
				Executing two or more subprogram units simultaniously
			Program Level-
				Executing two or more programs simultaniously.
		Something is said to be 'Scalable' if...
			The speed of execution increases when more processors are available.
		"Hidden Concurrency"-
			The concurrency occuring at the bottom level that greatly influenced the speed of the overall system without 
			enforcing the design of concurrent programs.
		Catagories of Concurrency-
			Physical Concurrency-
				Literal simultanious execution of several program units.
			Logical Concurrency-
				Interleaved execution on a single processor.
		"Thread of Control"-
			The sequence of program points reached as control flows through the program.
		"Quasi-Concurrent"-
			Running coroutines on a single processor. Logical but not physical.
		"Multithreaded Program"-
			A program that has multiple threads of control. Physically concurrent.
		There are four reasons to use concurrency-
			1. Increase in Execution Speed where the hardware is available.
			2. Even when run on a single processor, multithreaded programs tend to be quicker.
			3. Concurrency provides a different method of conceptualizing solutions to problems.
			4. Concurrent programs can be distributed over several machines either locally or through the internet.
	13.2 Introduction to Subprogram-Level Concurrency
		"task" / "processes"-
			A unit of program similar to a subprogram that can be in concurrent execution with other units of the same program.
		"threads"-
			an object that executes tasks
		Tasks fall into two catagories-
			heavyweight task-
				executes in it's own address space.
			lightweight task-
				executes all in the same address space.
		A task is said to be "disjoint" when...
			it does not interact with any other task in the program.
		"Synchronization"-
			A mechanism that controls the order in which tasks execute.
		"Cooperation Synchronization"-
			A mechanism by which Task A must wait for Task B to finish before Task A begins.
		"Competition Synchronization"-
			A mechanism by which Task A and Task B both require a resource that can't be used simultaniously.
		"Race Condition"-
			When without Competition Synchronization the two task race for the resources destroying consistancy in the data.
		"Scheduler"-
			A runtime program that manages the sharing of processors.
		Tasks can be in several different states-
			1. New: Created but not executed.
			2. Ready: Can run but not currently running.(when ready are stored in the "task ready queue")
			3. Running: A process that is currently being executed.
			4. Blocked: A task that was running but then stopped.
			5. Dead: No longer active.
		States of a Task-
			New -> Ready -> (Scheduled) -> Running
											if Time Slice Expired -> Ready
											if Completed -> Dead
											if I/O	-> Blocked -> (If I/O completed) -> Ready
		"Liveness"-
			An attribute in that it can continue to execute until completion.
		"Deadlock"-
			A loss of liveness due to two processes needing exclusive access from data that the other holds.
			IE: Task A holds X and Task B holds Y, Task A also needs Y to run and Task B also needs X to run.
			Both cannot run.
	13.3 Semaphores
		"guard"-
			a linguistic device that allows the guarded code to be executed only when a condition is true.
		"task descriptor"-
			a data structure that stores all the relevant information about the execution state of a task.
		"semaphore"-
			an implementation of a guard for concurrency.
			It holds an integer and queue that stores task descriptors.
		cooperation synchronization and semaphores using a buffer (circular queue)-
			It must know both the number of empty and existing spots.. this is so the buffer doesn't overflow(out of room) or underflow(0 entries)
		"binary semaphore"-
			A specific example of semaphore...
	13.4 Monitors
		Abstracting the concurrent operations by having it handled by the run-time system.
	13.5 Message Passing
		Message Passing is controlled by 'guarded commands' such as those found in Haskell.
		Synchronous Message Passing-
			Task A wants to talk to Task B but Task B is busy, it's not good to interrupt task B so task A will wait until task B says its ready.
		'rendevous'-
			The mutual agreement between sending/recieving of the tasks.
	13.6 Ada Support of Concurrency- Wait for Park to see which we should study..
	13.7 Java Threads - Wait for Park.....
	13.8 C# Threads - Wait for Park....
	13.9 Concurrency in Functional Languages - Wait for Park....
	13.10 Statement-Level Concurrency - Cover only if Park asks for it.
Chapter 14 Exception Handling and Event Handling
	14.1 Introduction to Exception Handling
		"Exception"-
			Unusual event errornous or not that is detectable either by hardware or software that may require special processing.
		"Exception Handling"-
			The special processing that may be performed on an exception.
		"Exception Handler"-
			The code segment or unit that handles the exception handling.
		"Raised Exception"-
			the event when the Exception occurs.
		"Continuation"-
			Exception Handling that moves the program forward in a special way. (used for non-erronous cases.)
		"Termination"-
			Ending the program (used for erronous cases)
		"Resumption"-
			The program design that allows continuation to occur.
	14.2 Exception Handling in Ada - Language Specific so Wait for Park
	14.3 Exception Handling in C++ ...
	14.4 Exception Handling in Java ...
	14.5 Introduction to Event Handling
		"Event"-
			A notification that something specific has occured(ie: keyboard action or mouse action or graphics card action)
		"Event Handler"-
			A code segment that is executed in response to an event.
	14.6 Event Handling with Java - Language Specific...
	14.7 Event Handling in C#
Chapter 15 Functional Programming Languages
	15.1 Introduction
		Not much information here...
	15.2 Mathematical Functions
		"Mathematical Function"-
			A mapping of a set known as domain to another set known as range.
		A fundamental of functional programs is a use of recursion over iteration as it better illustrates 'solution' vs 'change in state'
		"Lambda Expression"-
			A specification of parameters and mapping of a function.
			The lambda expression is the function itself, nameless.
			For example...
				(lambda)(x)x*x*x
			would map x to x^3
		"Lambda Calculus"-
			A computational model based on lambda expressions.
			Lambda calculus can be typed or untyped.
		Untyped Lambda Calculus is the inspiration for Functional Programming
		
		"Higher-order function"/"functional form"-
			A function that takes one or more functions as parameters and yields a function as the result.
		"Function Composition"-
			A kind of functional form which has two function parameters and uses the first function as a parameter in the second.
			The result is a new function.
		"Apply-To-All"-
			Takes a single function of a parameter and applies it to a list of arguments.
	15.3 Fundamentals of Functional Programming Languages
		"Referential Transparency"-
			The tendency for lower level details related to most of program states to be hidden.
	15.4 The First Functional Programming Language: LISP - Language Specific...
	15.5 An Introduction to Scheme	...
	15.6 Common LISP	...
	15.7 ML	....
	15.8 Haskell ...
	15.9 F# ...
	15.10 Support for Functional Programming in Primarily Imperative Languages
		Essentially covers the introduction of Lambdas in certain imperative languages.
	15.11 A comparison of Functional and Imperative Languages - If Park does a comparison in class I'll put the notes in here.
Chapter 16 Logic Programming Languages
	16.1 Introduction
		"Logic Programming" / "Logic Programming Languages" / "Declarative Languages"-
			Programming languages that use symbolic logic
	16.2 A Brief Introduction to Predicate Calculus
		"proposition"-
			a logical statement that may or may not be true.
		Symbolic Logic can be used to...
			Express Propositions, 
			Express the relationship between propositions, 
			and to describe how new propositions can be inferred from other propositions assumed to be true.
		"Atomic Proposition"-
			The simplest proposition possible consisting of compound terms.
		"compound terms"-
			an element of a mathematical relation
			It is composed of two parts. a 'functor' which is the symbol naming the relation and an ordered list of parameters.
		Recall the logic symbols of CSCI 60.
	16.3 Predicate Calculus and Proving Theorems  -- I'm not going any further than this unless Park does, he avoided predicate calculus for a reason.
	16.4 An Overview of Logic Programming
	16.5 The Origins of Prolog
	16.6 The Basic Elements of Prolog
	16.7 Deficiencies of Prolog
	16.8 Applications of Logic Programming
Extra - Expression Notation, Syntatic Ambiguity
		There are 4 types of Expression Notation
		Prefix
			IE: sqrt*+-a b c d
			The form of prefix(or polish notation)
			is to have the operator before the operands.
			The calculations can be traced using parenthesis.
			I used a simple example to get the idea across..
				sqrt*+-a b c d
				sqrt*+(-a b) c d
				sqrt*(+(-a b) c) d
				sqrt(*(+(-a b) c) d)
				(sqrt(*(+(-a b) c) d))
				Note that sqrt is a unary operator so it only needs one value to work on.
			Here is a more complex example..
				+ * 3 / * pow 2 4 sqrt 3 4 1
				+ * 3 / * (pow 2 4) (sqrt 3) 4 1
				+ * 3 / (* (pow 2 4) (sqrt 3)) 4 1
				+ * 3 (/ (* (pow 2 4) (sqrt 3)) 4) 1
				+ (* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 1
				(+ (* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 1)		
		Postfix
			IE: a b c d -+*sqrt
			The form of postfix(or reverse polish notation)
			is to have the operaor after the operands.
			Like prefix the calculation can be traced with parenthesis.
			Simple example...
				a b (c d -)+*sqrt
				a (b (c d -)+)*sqrt
				(a (b (c d -)+)*)sqrt
				((a (b (c d -)+)*)sqrt)
			For the most part you may have noticed that they can just be flipped..
			BUT BE CAREFUL, If an operation is associativity sensitive (exponentiation, division, modulus)
			then you need to be careful about flipping. You need to retain assoiativity to prevent confusion.
			You can trace a complex example just like prefix.
		Infix
			Infix is how we normally do math IE.
			1 + 2 * 3 / 2
			And we can trace this with parenthesis as well..
			(1 + ((2 * 3) / 2))
		Misfix
			Misfix are expressions which do not fit in the prior 3 types.
			An example is an if else statement.
			if condition {statement} else {statement}
		Our fixes can be unravelled into a parse tree..
			Take for example our complex prefix...
				(+ (* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 1)	
			We can trace the tree by looking at the operators
			and utilizing a recursive algorithm...
				1. Pop off parenthesis.
					+ (* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 1
				2. Make popped operator parent node.. 
					(* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 1
				3. It's left and right child are the remaining closures.
				
				CONTINUING TRACE
					Left Child : 	(* 3 (/ (* (pow 2 4) (sqrt 3)) 4)) 
									* 3 (/ (* (pow 2 4) (sqrt 3)) 4)
									* becomes parent node
									Left Child: 3 (done)
									Right Child: (/ (* (pow 2 4) (sqrt 3)) 4)
										/ (* (pow 2 4) (sqrt 3)) 4
										/ becomes parent node
										Left Child: (* (pow 2 4) (sqrt 3)) 
											* (pow 2 4) (sqrt 3)
											* becomes parent node
											Left Child: (pow 2 4)
												pow 2 4
												pow becomes parent node
												Left Child: 2 (done)
												Right Child: 4 (done)
											Right Child:(sqrt 3)
												sqrt 3
												sqrt become parent node
												Left Child: 3 (done)
												Right Child: empty (done)
										Right Child: 4 (done)
										
					Right Child: 1 (done)
			We can make a very similar algorithm for postfix.
			By practicing putting together these trees we can gain the intuition
			to put together an infix tree.
		Syntatic Ambiguity
			As defined earlier we hate left recursion,
			left recursion is a cause of ambiguity
			repeated productions also cause ambiguity.(consider dangling else.)