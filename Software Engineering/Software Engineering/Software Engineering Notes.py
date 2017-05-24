Software Engineering: Chapter 8
	8.0.0 Introduction
		Purpose of Testing-
			1. Demonstrate to developer and customer that requirements are met. (validation testing)
			2. Find input(s) where behavior is incorrect. (verification testing)
		"Testing can only show the occurence of errors, not their absence." -Dijkstra
		What Affects Needed Confidence...
			1. Software Purpose
			2. User Expectations
			3. Marketing Environment
		Inspections/Reviews Analyze Documents and Source Code. This holds some advantages...
			1. Errors cannot be masked.
			2. Incomplete versions of a system can be analyzed
			3. Qualitative Analysis can be performed.
		There are Three Stages of Testing
			1. Development Testing: Check for bugs/defects
			2. Release Testing: Check if program meets requirements.
			3. User Testing: Potential Users test the program in their own environment.
	8.1.0 Development Testing
		There are Three Stages of Development Testing-
			1. Unit Testing: Testing functionality of smallest programmable units.
			2. Component Testing: Test integrated unit interfaces.
			3. System Testing: Test integrated component interactions.
	8.1.1 Unit Testing
		In a Unit Test One Must...
			1. Test all possible code paths (each line is executed)
			2. Test all possible states (all possible combination of code paths, including identical paths with different fulfilled conditions.)
		Unit Testing is Easily Automated, Which can be split into three parts...
			1. Setup: load expected I/O
			2. Call: run the function
			3. Assert: make sure what the function generates from exepected I matches the expected O.
	8.1.2 Choosing Unit Test Cases
		Effective Test Cases Should...
			1. show when used as expected that it does what it is supposed to do.
			2. show defects if they exist.
		Two Strategies to Help Choose Test Cases Are...
			1. Partition Testing: Identifying groups of inputs that share common characteristics...
				Thus by identifying all these 'equivalence partitions' one can limit their testing to only a group of inputs where each input
				represents one of the equivalence partitions.
			2. Guideline-Based Testing: Use guidelines that reflect previous defect experiences....
	8.1.3 Component Testing
		Different Types of Interfaces-
			1. Parameter Interface: Data is passed from one object to another.
			2. Shared-Memory Interface: A block of memory is shared between objects.
			3. Procedural Interface: Encapsulates Procedures Called by Another Object
			4. Message-Passing Interface: Object requests service from another objects and waits to be served.
		Different Types of Interface Errors-
			1. Interface Misuse: Component makes an error in the use of an interface.
			2. Interface Misunderstanding: Certain assumptions may be made and so the use of an interface is incorrect, ie: passing an unsorted array into binary search.
			3. Timing Errors: Producer/Consumer operate at different speeds which may cause issues with data consistency.
		Guidelines for Interface Testing-
			1. Test extreme values
			2. Test with null pointers if pointers are expected
			3. Try to cause procedural interfaces to fail
			4. Use stress testing in message passing.
			5. With shared memory vary the order of operations.
	8.1.4 System Testing
		Use case based testing is useful for System Testing, as such use case(sequence) diagrams can help find test cases.
	8.2.0 Test-Driven Development
		Steps...
			1. Identifying Increment of Functionality
			2. Write Test, implement as automated test.
			3. Run incomplete function against test, should fail.
			4. Implement functionality and re-run test until done.
			5. Once all tests run successfully implement next chunk of functionality.
		Benefits of TDD...
			1. Code Coverage: All code in the system has been executed.
			2. Regression Testing: A Test suite to perform regression tests are formed.
			3. Simplified Debugging: When something goes wrong it is obvious where it goes wrong.
			4. System Documentation
	8.3.0 Release Testing...
		...
	8.3.1 Requirements-Based Testing
		Requirements should be testable.
	8.3.2 Scenario Testing
		Devise Scenarios(similar to stories) on how a requirement is utilized. 
		This allows easy manual testing where emergent issues may be seen.
	8.3.3 Performance Testing
		...
	8.4.0 User Testing
		Three Different type of User Testing...
			1. Alpha Testing: group of software users work closely with development
			2. Beta Testing: release of software made available with larger group.
			3. Acceptance Testing: Customers test decision to dercide whether or not it is ready to be accepted from the system developers.
		Six Stages of Acceptance Testing...
			1. Define Acceptance Criteria
			2. Plan Acceptance Testing
			3. Derive Acceptance Tests
			4. Run Acceptancs Tests
			5. Negotiate Results
			6. Accept/Reject System
Software Testing: Chapter 1
	1.1: Humans, Errors, and Testing
		1.1.1 Errors,faults,and failures
			Error: Incorrectly Writing a Program
			Fault/Defects: A manifestation of an error in the program
			Failure: Behavior that does not match expected behavior.
			Fault and Defect are often treated as synonyms.
		1.1.2 Test Automation
			covered already...
		1.1.3 Develop and Tester as Two Roles...
			While the same individual may do both, each may be done exclusively. For this reason the roles need to be separated.
	1.2: Software Quality
		1.2.1 Quality Attributes
			Two Types of Quality Attributes...
				1. Static: Quality of code and documentation.
				2. Dynamic: Quality of behavior while program is in use. These include...
					* Reliability: Probability of failure-free operation
					* Correctness: Correct Execution
					* Completeness:Availability of all Features Listed in Requirements
					* Consistency: Adherence to a common set of conventions and assumptions
					* Usability:   Ease with which application can be used.
					* Performance: Time application takes to perform a task.
	1.3: Requirements,Behavior,and Correctness
		1.3.0 Completeness of Requirements
			Some requirements may be incomplete ie: "Sort a List" would be ambiguous without "Sort a List in Ascending Order", on the otherhand conflicts can occur
			ie: "Use the Sort Algorithm to sort it in descending order..." would provide a contradiction.
		1.3.1 Input Domain
			Exhaustive Testing: Testing by checking against every possible input. Not very feasible outside of enumerated types.
			Input Domain: Set of all possible inputs to a program P
			Correctness: A program is correct if it behaves as expected on each input of it's input domain.
			Input Domain Example...
				Consider a function 'MAX' that returns the max between an integer passed in through a tuple (a,b)
				How many possible inputs are there if we assume 32 bit numbers?...
					(2^32-1)*(2^32-1) which is approximately 1.8 x 10 ^ 19 possible inputs.
					Even for a simple max program exhaustive testing isn't very feasible.
		1.3.2 Specifying Program Behavior
			Using a state diagram one can determine the path of program behavior.
			We can represent this abstractly with a state vector...
			[line,var1,...,var n]
			Given the same state, the same execution should occur.
			We can use the knowledge of the input-partitions to create state diagrams to trace execution.
			This state based approach is also useful for capturing behavioral information.
		1.3.3 Valid and Invalid Inputs
			Sometimes unexpected inputs may enter the function. Robustness deals with correcting these incorrect states.
			The invalid inputs can just as easily be seen as part of the input domain.
	1.4: Correctness Versus Reliability
		1.4.1 Correctness
			Formal Proof can be utilized to show correctness.
			Correctness does not mean that it is error free.
			Proofs and Testing together however can increase 'confidence' of error free execution.
		1.4.2 Reliability
			Reliability: "Probability of successful execution on a random element of it's input domain."
		1.4.3 Operational Profiles
			A detailed list of expect input behavior.
			ie for a sort:
				Sequence				Probability
				Numbers Only					0.1
				Alphanumeric Strings			0.9
			Would imply how it is used.
	1.5: Testing and Debugging
		1.5.0 Introduction
			Testing: Techniques to Find an Error
			Debugging: Process to Remove an Error
		1.5.1 Preparing a Test Plan
			Test Plan: A planned approach to performing testing.
		1.5.2 Constructing Test Data
			Test Case: Pair of Input and Expected Output
			Test Set/Test Data:  Collection of Test Cases
		1.5.3 Executing the Program
			...
		1.5.4 Assessing Program Correctness
			Oracle: What determines if the expected output matches the output. This can be many things, automated or a person.
			Human Oracles are prone to Human Error as well though, so automated oracles are preferred.
		1.5.5 Constructing an Oracle
			...
	1.6: Test Metrics
		1.6.1 Organizational Metrics
			ie: Numbers of Defects Reported Per Release
			ie: Defects Per Thousand Lines of Codes D/KLOK
		1.6.2 Project Metrics
			ie: Ratio of Actual to Planned Test Effort
			ie: Test Effort as tester-man-months
			ie: Total Number of Successful Tests to Total Number of Tests
		1.6.3 Process Metrics
			ie: defects found per phase
		1.6.4 Product Metrics: Gemeroc
			Given a Program with N nodes, E edges, and p connected procedures reachable from a procedure G,
			the cyclomatic complexity V(G) is computed as follows...
				V(G)=E-N+2p
		1.6.5 Product Metrics: OO Software
			...
		1.6.6 Progress Monitoring and Trends
			Keeping track of metrics over time can provide an idea of other things about a project.
		1.6.7 Static and Dynamic Metrics
			Static: Computed without execution
			Dynamic:Computed with execution
		1.6.8 Testability
			Degree to which tests can be made for components/requirements and the degree to which testing can show that they have been met.
	1.7: Software and Hardware Testing
		Test Set Efficiency/Effectiveness: faults_detected/faults
	1.8: Testing and Verification
		Verification such as through proofs is a useful complementary technique especially in safety critical applications.
	1.9: Defect Management
		Defect Prevention: Take measure to prevent them
		Defect Discovery: Find the ones that get through the measure
		Defect Recording: Record them
		Defect Reporting: Report them
		Defect Classification: Classify their severity
		Defect Resolution: Deal with it.
		Defect Prediction: Use your new knowledge to aid in prevention.
	1.10: Test Generation Strategies
		Different Formal/Informal Models, and UML can be utilized to generate test cases.
		Black Box Testing: Determine test cases from requirements (validation)
		White Box Testing: Determine test cases from the code (verification)
	1.11: Static Testing
		1.11.0 Introduction
			Static Testing: Testing Without Code Execution
		1.11.1 Walkthroughs
			Going through related documents (ie: requirements, and the source code implementing it)
			Go through and make sure that it fulfills those requirements. 
		1.11.2 Inspections
			A technique where code is inspected by a team to improve qualitative aspects of the code as well as detect defects.
		1.11.3 Software Complexity and Static Testing
			Typically more complex modules are chosen for inspection over less-complex. (refer to metrics)
	1.12: Model-Based Testing and Model Checking
		Applying UML to the Tsting
	1.13: Types of Testing
		Testing Classifiers...
			1. C1: Source of test generation
				Black Box
				White Box
				Interface
			2. C2: Life Cycle Phase in which testing takes place
				Coding -> Unit
				Integration -> Integration
				System -> System
				Maintenance -> Regression
				Post System/Pre-Release -> Beta
			3. C3: Goal of a specific testing activity
				This narrows down the purpose of some tests. ie: Performance, Security, and Robustness Testing
			4. C4: Characteristic of the artifact under test
				Design Testing
				OO Testing
				etc.
			5. C5: Test Process
				Testing in a Given Model
	1.14: The Saturation Effect
		1.14.0 Introduction
			Refers to the stability between Confidence and actual Reliability
		1.14.1 Confidence and True Reliability
			True Reliability: Actual rate of avoiding failure
			Confidence: Percieved rate
		1.14.2 Saturation Region
			...
		1.14.3 False Sense of Confidence
			As faults don't show up it may inflate the programmer confidence even though it is not warranted.
		1.14.4 Reducing Delta
			Utilizing a Combination of Techniques Will reveal more faults than using less, especially as the complexity of the program grows.
		1.14.5 Impact on Test Process
			The Goodness of Tests Must Be Able to be Measured
	1.15: Principles of Testing
		Principle 1: Definition-
			Testing is the activity of assessing how well a program behaves in relation to its expected behavior.
		Principle 2: Reliability and Confidence-
			Testing may increase one's confidence in the correctness of a program through the confidence may not match with the program reliability.
		Principle 3: Coverage- 
			A test case that tests untested portions of a program enhances or diminshes one's confidence in the program correctness depending on whether the test
			passes or fails.
		Principle 4: Orthogonality
			Statistical measurements of the reliability of an application and the code coverage obtained by the tests used for measuring the reliability are orthogonal.
		Principle 5: Test Suite Quality-
			Code Coverage is a reliable metric for the quality of a test suite.
		Principle 6: Requirements and Tests
			Tests derived manually from requirements alone are rarely complete
		Principle 7: Random Testing
			Random Testing may or may not outperform nonrandom testing.
		Principle 8: Saturation Effect-
			The saturation effect is real and can be used as an effective tool for the improvement of test generation strategies
		Principle 9: Automation-
			Test automation aids in reducing the cost of testing and making it more reliable, but not necessarily in all situations.
		Principle 10: Metrics-
			Integrating metrics into the entire test process aids in process improvement.
		Principle 11: Roles-
			Every developer is also a tester.
	1.16: Program-Dependance Graph
		Consider the Following Program
			1. begin
			2. int num,product
			3. bool done;
			4. product = 1;
			5. input(done);
			6. while(!done){
			7. 	input(num);
			8. 	product = product * num;
			9. 	input(done);
			10.}
			11.output(product);
			12. end
		We can see there are data dependencies on different lines...
			1 -> NONE
			2 -> NONE
			3 -> NONE
			4 -> NONE
			5 -> NONE
			6 -> 5,9
			7 -> NONE
			8 -> 4,7,8
			9 -> NONE
			10-> NONE
			11-> 4,8
			12-> NONE
		Filtering out only those with data dependancies...
			6 -> 5,9
			8 -> 4,7,8
			11-> 4,8
		We can also find control dependancies among these data dependancies...
			4 -> NONE
			5 -> NONE
			6 -> NONE
			7 -> 6
			8 -> 6
			9 -> 6
			11-> NONE
		These Produce Two Separate Graphs, They can be combined into one graph easily though to show all of the line dependancies.
Software Testing: Chapter 2
	2.1 Predicates and Boolean Expressions
		Boolean Expression: &&, || , >, < , etc.
		Simple Predicate: At most one comparison is made. ie: true, a != b, a < b
		Compound Predicate: A predicate where simple or compound predicates are located on either side of the boolean operator.
		When working with full boolean arithmatic product is and, addition is or. A bar above a value is not.
		
		Singular: If each expression only occurs once then an expression is singular.
		Mutually Singular: Two variables exp_i and exp_j are mutually singular if they do not share a variable.
		
		Disjunctive Normal Form: Sum of Products
		Conjunctive Normal Form: Products of Sums
		
		Expressions Can be Represented as an AST(Abstract Syntax Tree)
	2.2 Control Flow Graph
		A CFG represents the flow of control in a program.
		It consists of "Basic Blocks" and directed edges between them.
		2.2.1 Basic Blocks
			A basic block is the longest consecutive list of states such that it has a unique entry and exit point.
			For Example...
				begin
					int x,y,power;
					float z;
					input (x,y);
					if (y<0)
						power = -y;
					else
						power = y;
					z = 1;
					while (power != 0){
						x = z*x;
						power=power-1;
					}
					if (y<0)
						z = 1/z;
					output(z);
				end
			The basic blocks would be...
				if(y<0) -> if(y<0)
				
				power = -y -> power = -y
				
				power = y -> power = y
				
				z = 1 -> z = 1
				
				while(power != 0) -> while(power != 0)
				
				z = z*x -> power=power-1
				
				if(y<0) -> if(y<0)
				
				z = 1/z -> z = 1/z
				
				output(z) -> output(z)
		2.2.2 Flow Graphs
			This would be a graph of our labeled basic blocks and how they reach other parts of the program(directed edges.)
		2.2.3 Paths
			Path: A path length k is a list of k subsequent edges.
			Descendent/Ancestor: If we have a node sequence n,m, m is the descendant, n is the ancestor. In addition if n/=m then they are "proper"
			Successor Set: The set of all nodes that can be reached from a specific node.
			Predecessor Set: Going the other way, all nodes that can reach the current node is the predecessor set.
			If the start node reaches the end node then the path is said to be "complete"
			If there is atleast one logical way of entering a path it is considered "feasible", any who cannot are "infeasible"
		2.2.4 Basis Set
			Basis Path: A path through a program P, the number of basis paths is equal to the cyclomatic complexity.
			Basis Set: The set of all Basis Paths
		
			Here is an exampe notation of basis sets-
				Supposed there are 7 nodes.
				(Start,1,2,4,6,End)
				This would give us the following path vector: 1101010
		2.2.5 Path Conditions and Domains
			Path Condition: A condition that must be tree for that path to be taken. A path without a path condition is said to be "trivially true"
			Path Domain: All inputs that satisfy a condition
			Example-
				int gcd(int x1, int y1){
					int x,y;
					input(x1,y1);
					x=x1; y=y1;
					while(x!=y){
						if(x>y)
							x=x-y;
						else
							y=y-x
					}
					return x;
				}
				
				At it's most basic we have a major condition.
				while(x!=y), x and y directly depend on x1,y1. so the path domain is: x1 != y1
				Likewise within the while loop there is an if else statement. The path domain for x=x-y would be: x>y, likewise for y=y-x it is x<=y
				
				With this knowledge we can derive test cases that would cover each path through the code.
				We need to satisfy each condition and it's negation for path coverage.
				
				x != y , x == y
				x <= y , x > y
				
				x==y -> (4,4)
				x!=y ^ x >  y -> (4,2)
				x!=y ^ x <= y -> (2,4)
				
				Additionally this convers condition coverage.(Not hard since the conditions are simple.)
				
				Using paths to generate tests is a technique known as "domain testing"
		2.2.6 Domain and Computation Errors
			Domain Error: A correct input leads down an incorrect path. It can be broken down into path selection errors and missing path errors.
			Computation Error: An input goes down the correct path, but leads to an incorrect result.
		2.2.7 Static Code Analysis Tools and static Testing
			Useful Tools for Debugging, Keeps track of a lot of book keeping on definitions and such. Seems useful.
	2.3 Execution History
		Execution Trace: An organized set of data about the runtime execution of a program instance.
	2.4 Dominators and Post-Dominators
		N "dominates" M if on a Control Flow Graph G; N is on every path (Start,...,M)
		N "post-dominates" M if on a CFG G; N is on every path (M,...,End)
		The concept is easily visualized, but hard to describe. Check pages 83 and 94 to see it in action.
	2.5 Program Dependence Graph
		2.5.1 Data Dependance
			If D utilizes of variable modified by P, then D is data dependant on P.
		2.5.2 Control Dependance
			If C's path depends on a variable modified by P, then C is control dependant on P
			Utilizing Alex's Example is Probably Best for Seeing it in Action
		2.5.3 Call Graph
			A call graph connects procedure/method calls.
	2.6 Strings, Languages, Regex
		Look up Reference on Your Own, it isn't hard.
Software Testing: Chapter 3
	3.1 Introduction	
		Test Generation Techniques...
			Requirements-
				Informal
					Predicate Based
					Combinatorial
					Statistical
					Equivalence Partitioning
					Boundary Value Analyses
					Domain Testing
					Cause-Effect Graphing
					Decision Tables
					Scenario Generation
				Formal-
					Model Based Techniques
					Specification Based Techniques
	3.2 The Test Selection Problem
		The test selection is to select a subset T of test such that an execution p against each element of T will reveal all errors in p.
		Input Domain: Set of all legal inputs that a program p may recieve during execution. Typically very large.
		Exhaustive Testing: Testing the entire input domain, infeasible in most cases as often the domain may be infinite.
	3.3 Equivalence Partitioning
		This is a technique where an input domain is broken up into equivalence classes. That is to say the behavior of these sub domains is the same as other elements of the same subdomain.
		page 110 has a good diagram.
		3.3.1 Faults Targeted
			The total input domain can be spearated into two partitions: Expected and Unexpected Inputs. From there the sub-partitions can further be broken down into
			equivalence classes.
		3.3.2 Relations
			When it comes to information such as Database relations, often a program p has to consult a database, this leads to an assumption of discrete values.
			This is specification based, however we can define the equivalence partitions as the relations with something in common.
			For example with printers
			"color multifunction" and "color inkjet" would be their own categories.
			Of course there is often an equivlaence partition that represents all invalid inputs
			
			Finding Equivalence Classes Example...
				begin
					string w,f
					input(w,f)
					if !exists(f){ raise exception; return 0; }
					if length(w)==0 return 0
					if empty(f) return 0
					return(getCount(w,f))
				end
			We know that f can exist or not exist...
				f
				exist
				does not exist
			We then know that the w can be null or non-null
				f				w
				exist			null
				exist			non-null
				does not exist	null
				does not exist	non-null
			Then f can be empty or non-empty, of course it can only be so if it exists in the first place......
				f					w
				exist,empty			null
				exist,empty			non-null
				exist,non-empty		null
				exist,non-empty		non-null
				does not exist		null
				does not exist		non-null
			This gives us a total of 6 equivalence classes.
		3.3.3 Equivlance Classes for Variables
			With knowledge of constraints on the input domain, equivalence partitions can be often simplified.
			For example given some range... [30,60], we can identify 3 equivalence partitions.
			x < 30, x > 60, and 30 <= x <= 60.
		3.3.4 Unidimensional Partisioning Versus Multidimensional Partitioning
			In the w,f example we performed Multidimensional Partitioning(finding equivalence domains based on combinations of values)
			On the other hand working on only one variable at a time such as with the previous range example is unidimensional partitioning.
			One way is to imagine it geometrically. Suppose we have two ranges...
				x = [-30,30]
				y = [-30,30]
			If we plot either then we can easily see each has 3 equivalence partitions.. but what if we graph them at the same time?
			In that case 9 Equivalence partitions can be identified. 
			While this is excellent for providing high amounts of thorough coverage, the equivalence domains increase exponentially with the amount of inputs.
			In addition they may not be so trivial to detect.
		3.3.5 A systematic procedure
			1. Indentify the Input Domain
			2. Equivalence Classing (Unidimensional)
			3. Combine Equivalence Classes (Multidimensional)
			4. Identify infeasible equivalence classes
		3.3.6 Test Selection
			In situations where there are large amounts of equivalence classes, one can conver multiple equivalence classes in a single input.
			While not as thorough as a Multidimensional approach it can still cover the classes themselves.
			The weakness of this approach is that semantics are not covered, so it may not garuntee behavior that would only show up under super-specific cases.
		3.3.7 Impact of GUI Design
			The GUI can be a source of consideration for determining constraints on the input-domain.
			For example if the GUI only allows an input string 3 <= length(s) <= 7.
			Then there are only 3 equivalence domains. length(s) < 3, length(s) > 7, and the valid input.
	3.4 Boundary Value Analysis
		1. Partition input domain using unidimensional partitioning
		2. Identify the boundaries for each partition.
		3. Select test data such that each boundary values occurs in at least one input.
		IE...
			(10,100), we have the boundary values 10,100 . Around the boundary we would have 9,11,99,101 respectively. Note that 11 and 99 are in the same equivalence partition.
			While it may not be minimal, if there may be faults at the boundary values including both 11 and 99 would be prudent.
	3.5 Category-Partition Method
		3.5.1 Steps in the Category-Partition Method
			 |  Functional Specification
			\|/
			1.  Analyze Specification: Find all the testable units.
			 |	Functional Units
			\|/
			2. Identify Categories: Analyze the parameters finding all the categories.
			 | Categories
			\|/
			3. Partition Categories: Perform input partitioning.
			 | Choices
			\|/
			4. Identify Constraints: Find any constraints on the data, constrain input domain.
			 | Constraints
			\|/
			5. (Re)write test specfication: Create the specification.
			 | Test Specification(TS)
			\|/
			6. Process Specification: Document the testing process.
			 | Test Frames
			\|/
			7. Evaluate Generator Output: Examine test frames to make sure nothing is redundant or missing.
			 | Revise TS: No Test Frames
			\|/
			8. Generate test scripts
			 | Test scripts: Generate a test script, a group of test cases.
			\|/
Software Testing: Chapter 4
	4.2 Domain Testing
		4.2.1 Domain Errors
			Path Condition: A set of predicates that occur along the path of a condition/loop statement.
			Boundary: One of more "borders" that correspond to a path domain.
			Border: Corresponds to a predicate in the path condition.
			Border Shift: An error in the path of the boundary due to a problem with a border.
		4.2.2 Border Shifts
			A domain error can occur due to an unintended shift in border.
		4.2.3 ON-OFF Points
			Testing for boundary shifts is done with ON and OFF Points.
			ON Point: Must satisfy condition associated with border.
			OFF Point: Must be close as possible to ON Point. Lies outside of border, thus it doesn't fulfill the condition.
			For relations one ON and one OFF is needed.
			For comparisons such as equality 1 ON and 2 OFF are needed, one for each side of the border.
			Suppose we have the following code....
				if(y<x+1)
				if(y>0)
				if(x<=0)
				
				We can use boolean logic to denote a path. Here are all the possible paths...
					!y<x+1 ^ !y>0 ^ !x<=0
					!y<x+1 ^ !y>0 ^ x<=0
					!y<x+1 ^ y>0  ^ !x<=0
					!y<x+1 ^ y>0  ^ x<=0
					y<x+1  ^ !y>0 ^ !x<=0
					y<x+1  ^ !y>0 ^ x<=0
					y<x+1  ^ y>0  ^ !x<=0
					y<x+1  ^ y>0  ^ x<=0
				Utilizing these scheme we can easily figure out if our expected I/O will perform correctly.
		4.2.4 Undetected Errors
			Suppose we have a situation like follows...
				if(x<y)
			where the bug-free condition is actually... 
				if(x < y+1)
			We have the following...
				ON: <1,1.001>
				OFF: <1.5,0.4>
			This provides a situation where we cannot properly detect an error.
			Let us correct the OFF value so it is closer to the border...
				OFF: <1,0.999>
			Now in this situation It is not matching our expected comparison. x < y is false, but this statement should be true according to specification. x < y+1
		4.2.5 Coincidental Correctness
			Sometimes code will appear to be performing correctly(expected behavior matches actual), but this occurs by accident.
			In these cases it may not be obvious that an error is present, and these errors may manifest outside of the normal testing domains.
		4.2.6 Paths to be Tested
			Though there are many approaches, one is to test a path such that no loops execute at all (boundary condition)
			And another where they all execute. ("path coverage")
	4.3 Cause-Effect Graphing/Dependancy Graphing
		input causes result in output effects, which may be causes themselves.
		Steps in generateing tests using Cause-Effect Graphing are...
			1. Identify Causes and Effects from Requirements. Each Cause/Effect is assigned a unique identifier.
			2. Express it through a cause effect graph.
			3. Transform the graph into a decision table.
			4. Generate tests from the decision table.
		4.3.1 Notation used in cause-effect graphing
			page 161
			C implies Ef
			not C implies Ef
			Ef when C1 and C2 and C3
			Ef when C1 or C2
			Exclusive C1 or C2 or C3
			Inclusive C1 or C2
			C1 requires C2
			One and Only One of C1 and C2
		4.3.2 Creating Cause-Effect Graphs
			First the causes/effects are identified through careful examination of the requirements.
			This also helps identify special relationships. Each is given a unique identifier.
			
			In the second step, the CE graph is constructed express the relationships extracted from the requirements.
			If the number of cause/effects are very large an incremental approach may be necessary.
			Page 166-167 provide an excellent example of building a CE Graph.
		4.3.3 Decision table from cause-effect graph
			CEG.png and paes 169-171 for reference
		4.3.4 Heuristics to avoid Combinatorial Explosion
			Utilizing heuristics is useful when the number of test cases are ludicrous.
			Heuristics can reduce the amount of test cases, but at the cost of thoroughness.
			Page 173 has a good list.
			H1: Given OR, consider only inputs where the inputs are all 0. Goal: 0
			H2: Given OR, consider only inputs where it isn't 0. Goal: 1
			H3: Given AND, consider input combinations such that they occur only once and they are not all 1.
			H4: Given AND, consider only inputs where the inputs are all 1. Goal: 1
		4.3.5 Test Generation from a Decision Table
			Each column corresponds to a test case, considering relations more than 1 test case may be made from a column.
	4.4 Tests Using Predicate Syntax
		4.4.1 A Fault Model
			Boolean Operator Fault: incorrect operator used, negation missing/placed incorrectly, parenthesis placed incorrectly, incorrect boolean variable.
			Relational Operator Fault: Incorect relational operator used.
			Arithmetic Expression Fault: Result is off by e
				Off by e: |e3-e4| =  e
				Off by e*:|e3-e4| >= e
				Off by e+:|e3-e4| >  e
		4.4.2 Missing of Extra Boolean Variable Faults
			What it says on the tin
		4.4.3 Predicate Constraints
			Ways of guiding the test cases..
			Simple example...
			C:(t,=,>) applied to b ^ r < s \/ u >= v
			
			b is t
			r = s in r < s
			u is > v in u >= v
		4.4.4 Predicate Testing Criteria
			Criteria...
				BOR(Boolean Operator)...
					A test set T that satisfies BOR for a compound predicate p, garunees the detection of single or multiple boolean operator faults in p.
				BRO(Boolean and Relational Operator)...
					A test set T that satisfies BRO for a compound predicate p, is likely to detect single boolean operator and relational operator faults.
				BRE(Boolean and Relational Expression)...
					.... p, is likely to detect single boolean operator, relational expression, and arithmetic expression faults of p.
		4.4.5 BOR,BRO,BRE Adequeate Tests...
			Unless Asked...
	4.5 Tests Using Basis Paths
		Use Basis Graph, then find inputs that make given paths true. Test against expected I/O.
	4.6 Scenarios and Tests
		Essentially the testing equivalent of user stories.
Software Testing: Chapter 7
	7.1 Test Adequecy Basics
		7.1.1 What is test adequacy?
			Whether Criterion have been covered 'adequately'
		7.1.2 Measurement of Test Adequacy
			White-Box Test Adequacy: Test against the program.
			Black-Box Test Adequacy: Test against the requirements.
			For each criterion we derive a "coverage domain"
			We can say that a set of tests T coverse a coverage domain Ce
			if for each e' in Ce that there is atleast one test case that covers it.
			If the whole domain is covered then T is considered adequate with respect to C.
			given k e' of the n elements in C covered by T, if k < n then T is inadequate. 
			k/n is the "coverage"
		7.1.3 Test Enhancement Using Measurements of Adequacy
			Utilizing better and more adequate coverage is likely to test code in ways it hasn't been tested.
			So it can only be good for a project to do so.
		7.1.4 Infeasibility and Test Adequacy
			If an element of the coverage domain cannot be covered by any test case then it is infeasible.
		7.1.5 Error Detection and Test Enhancement
			Introducing new test cases that exercise a program in ways other test cases don't can show new errors.		
		7.1.6 Single and Multiple Executions...
			...
	7.2 Adequacy Criteria Based on Control Flow
		7.2.1 Statement and Block Coverage
			Statement Coverage of T with respect to (P,R)
			is |Sc|/(|Se|-|Si|) where Se are the statements covered, Sc are the reachable statements, and Si are the unreachable statements.
			
			Block Coverage of T with respect to (P,R)
			is |Bc|/(|Be|-|Bi|)
		7.2.2 Conditions and Decisions
			Condition/Predicate: any expression that evaluates to true or false
			A and B, not A, etc are conditions.
			Simple/Atomic/Elementary Condition: A,not A, A <= B
			Compound Condition: Condition made up of combinations of Simple Conditions
			A decision can have one of three results: true, false, undefined
		7.2.3 Decision Coverage
			The decision coverage of T with respect to (P,R) is computed as |Dc|/(|De|-|Di|)
			Simply put, all decisions are covered. 
			For example...
				if x < 2
					do stuff
				return 1
			The test case <x=1> would provide statement coverage, but no decision as the if branch never evaluates to false.
			<x=1>,<x=2> would provide decision coverage as each decision will have been evaluated true/false at least once per decision.
		7.2.4 Condition Coverage
			The Condition coverage of T with respect to (P,R) is computed as |Cc|/(|Ce|-|Ci|)
			Where we are referring this time to all the simple conditions coverable.
			ie:
				if x < 2 && y < 2
			This time we focus on basic conditions.
			<x=1,y=1>,<x=2,y=2>
			This checks against x<2, y<2, x>=2, y>=2 as well as both the true and false conditions for if x < 2 && y < 2
		7.2.5 Condition/Decision Coverage
			Also known as "branch condition coverage"
			Simply put... (|Cc|+|Dc|)/((|Ce|-|Ci|)+(|De|-|Di|))
		7.2.6 Multiple Condition Coverage
			Also known as "branch condition combination coverage"
			In this case the concern isn't with having made each of the decisions, but to having made all combinations of boolean values.
			For example...
				if x < 2 && y < 2
			We want <x=1,y=1>,<x=3,y=3>,<x=1,y=3>,<x=1,y=2>
			And that would provide the Multiple Condition Coverage
		7.2.8 Modified Condition/Decision Coverage
			To obtain MC adequacy tests must be enerated that show that each simple condition affects the outcome of C independently.
			For example given 3 inputs, we fix two fo them in place and vary the third, this can be scaled up as needed.	
			FOR EXAMPLE...
				C = (C1 and C2) or C3
			We can begin with 
			T	F	T = T
			so if we vary C3
			T	F	F = F	, it changed the outcome independently		
			
			so we add to our test cases...
				T	F	T = T
				T	F	F = F
			
			T	T	F = T
			so if we vary C2
			T	F	F = F
			
			so we add to our test cases...
				T	F	T = T
				T	F	F = F			
				T	T	F = T
				T	F	F = F
				
			T   T   F = T
			so we vary C1
			F	T	F = F
			
			so we add to our test cases...
				T	F	T = T
				T	F	F = F			
				T	T	F = T
				T	F	F = F
				T   T   F = T	
				F	T	F = F	

			And we have our test set. Removing duplicates...
				T	F	T = T
				T   T   F = T
				T	F	F = F
				F	T	F = F
			Which gives us our minimal set for MC/DC coverage.
		7.2.9 MC/DC Adequate Tests for Compound Conditions
			Detailed Here is the technique for generating MC/DC Tests, continued in 7.2.10
		7.2.10 Definition of MC/DC Coverage
			1. Each block in P has been covered
			2. Each simple condition in P has taken T/F values.
			3. Each decision P has taken all possible outcomes.
			4. Each simple condition as been shown to independantly affect the result.		
			In the case of coupled instances, only one occurence needs to be shown to independantly affect the result.
		7.2.12 Error Detection and MC/DC Adequacy
			MC/DC > decision/condition coverage in terms of finding errors.
		7.2.13 Short-Circuit Evaluation and Infeasibility
			It is important to consider if the programming language supports short circuit evaluation.
			If so then certain tests may be completely unnecessary or alternatively that conditions amy not be feasible. 
			A > 10 && B < 10
				A < 5 && B < 10
			would be an infeasible path...
			However...
			A > 10 && B < 10
				foo(A) && B < 10
			Would be considered feasible becasue the side effect foo(A) may generate a correct result.
		7.2.14 Basis Path Coverage
			Put simply, the coverage of basis paths.
		7.2.15 Tracing Test Cases to Requirements
			Utilizing Test Trace Back, one continues to trace back a test cases and what it tests to the requirements.
			This allows redunadnt tests to be detected as well as errors within requirements.
	7.3 Concepts From Data Flow
		7.3.0 Introduction
			In 7.2 the flow through the program itself was considered, in this section we will cover test adequecy concerning definitions of data 
			and subsequent usage of that data.
		7.3.1 Definitions and uses
			Examples of Definitions of x...
				x=y+z
				x=x+y
				int x
				scanf("%d",&x)
			Examples of uses of x...
				printf("%d",x)
				y=x
		7.3.2 C-use and p-use
			c-use stand for computational use, this refers to...
				Using a variable within an expression
				Using a variable within an output statement
				Using a variable as a function parameter
				Using variable in a subscript expression
				EXAMPLES WITH c-use OF x...
					z = z+1
					A[x-1] = B[2]
					foo(x*x)
					output(x)
			p-use stands for predicate use, this refers to...
				Used as a condition within an if statement
				Used as a condition within a while statement
				EXAMPLES WITH p-use of x...
					if(x>0){...}
					while(3>x){...}
		7.3.3 Global and Local Definitions and Uses
			Consider the following 3 statements...
				p=y+z
				x=p+1
				p=z*z
			In order it defines p, uses p, redefines p.
			The first definition of p is 'local' because it is 'killed' or 'masked' by the redefinition. 
			That redefinition survives after the blocks so it is considered 'global'
			The use of p in the second line is a 'local use' within the block. Likewise as y and z were not 
			defined in the block it is an example of 'global use'
			These terms of course relate to basic blocks.
		7.3.4 Data Flow Graph
			A DFG is a lot like a CFG except that it traces the usage of data.
			Breaking the program up into basic blocks the approach is to gather the related information...
			For each block get the definitions, c-uses, p-uses...
			Control flow is still respected when tranitioning to and from the nodes as well as the conditions that cause the change.
		7.3.5 Def-Clear Paths
			A Def-Clear Path is a path in a DFG such that it begins by declaring a definition ie: x and it is not redefined along the path.
			Thus it is 'a path that is clear of definitions after the initial one'
		7.3.6 Def-Use Pairs
			For a given definition there is a set of c-use and a set of p-use.
			These sets are 'dcu' and 'dpu' respectively.
			dcu is comprised of a set of singletons that refer to the nodes in which c-use takes place.
			dpu refers to pairs that are composed like so (<p-use node>,<node reachable>)
			An important thing to consider is that these sets are 'by definition' and not 'by variable'
			So a single variable can have multiple sets of Def-Use Pairs
		7.3.7 Def-Use Chains
			Extending on the idea that a single variable can have multiple def-use pairs, a sequence of these are referred to as a def-use chain.
			For example consider the following...
				x = 1
				y = x + 2
				...
				x = 2
				y = y + x
				...
				x = 3
				y = 11+x
			Let us label these blocks 1,7,9 respectively.
			About z we could construct a def use chain (1,7) or (1,7,9) when considering z which gives us a 3-dr chain.
		7.3.8 A Little Optimization
			Through analsysis we can determine if some c-use or some p-use implies another. By doing so we can eliminate redundant test cases.
		7.3.9 Data Context and Ordered Data Contexts
			Consider a DFG. Let n be a node in such a DFG.
			Each variable used at n is an 'input variable'
			Each variable defined at n is an 'output variable.'
			All life definitions at node n is known as the "data envrionment" of n.
			... I wont go any further since alex doesn't cover it and it's kind of confusing.				
	7.4 Adequacy Criteria Based on Data Flow
		7.4.0 Adequacy Criteria Based on Data Flow
			Let CU = Total Number of c-uses in a program
			Let PU = Total Number of p-uses in a program
		7.4.1 c-use Coverage
			The test cases for this should utilize def-clear paths in order to find minimal cases.
			Covering each def-clear path for a variable would satisfy c-use.
		7.4.2 p-use Coverage
			Use same approach, but consider p-use instead.
		7.4.3 All-Uses Coverage
			Combination of c-use and p-use coverage.
		7.4.4 k-dr chain Coverage
			This would refer to covering each of the available k-dr chains. This can of course be many chains as there are many possible def-clear path chains
			k-dr coverage also implies covering loops.
		7.4.5 Using the k-dr chain Coverage
			...
		7.4.6 Infeasible c-use and p-use
			...
	7.5 Control Flow Versus Data Flow
		tl;dr both are good in their own ways and in differing situations one may outshine the other.
	7.6 The "Subsumes" Relation
		Subsumes: Given a test set T that is adequate with respect to criterion C1, 
		what can we conclude about the adequacy of T with respect to another crterion C2...
			C1 is considered to subsume C2 if every test adequate with C1 is also adequate with C2
		Effectiveness: Given a test set T that is adequate with respect to criterion C,
		what can we expect regarding its effectiveness in revealing errors?
		
		What this comes down to is the subsumes relationship amongst test adequacy criteria.
		
		                                       /-> c-use -------------------------------------------------> Block
		Input Domain -> All Paths -> All-Uses |                                                        /
								\              \-> p-use -----------------------------------> Decision/
								 \-> Multiple Condition -> MC/DC -> condition/decision-----/
	7.7 Structual and Functional Testing
		...
	7.8 Scalability of Coverage Measurement
		...