Cohesion-
	Module-
		Definition-
			A lexically contiguous sequence of program statements with an identifier.
		Example-
			MODULE: Add
			f(a,b) begin
				t = a
				t + b
				return t
			end
	Goals of Good Design-
		Maximal Interaction Within Module
		Minimal Interaction Between Modules
	Functionally Equivalent-
		Perform the same task despite differing forms.
	Module Cohesion-
		Interaction within a module.
	Module Coupling-
		Interaction between modules.
	Classical Paradigm Naming-
		this_is_an_example
	Control Constructs-
		IE: For and DO, in the 1960's provided some degree of cohesion.
	Structured Programming-
		IE: Functions, stronger cohesion/coupling patters could arise as instructions become encapsulated.
	Modular Programming-
		Utilizing Structured Programming to represent collectives. Similarily named function ie: draw_pixel(), draw_sprite() are both parts of the draw module.
	Object-Oriented Programming-
		IE: Classes and Such, provides access control and separation of concerns. In addition true data encapsulation becomes possible.
	Aspect Oriented Programming-
		Crosscutting of concerns. Encapsulate "aspects" of a program ie: logging and parsing
	Categories of Cohesion-
		7. Informational Cohesion (Good)
			Performed all on the same data structure.
		6. Functional Cohesion
			Performs Exactly One Action
			Contributes to a single welldefined step.
			Is good for many reasons.
		5. Sequential Cohesion
			Output from One Line is Input for Next and So On
			Still not Reusable
		5. Communicational Cohesion
			Performs a series of actions but all operate on the same data.
			Still not very reusable
		4. Procedural Cohesion
			Related by execution order, but not time.
			Actions are weakly connected and so are not reusable.
		3. Temporal Cohesion
			Actions are related by time.
			Weak interaction within module, but strongly related to toher modules.
		2. Logical Cohesion
			An action of the callee is performed by the caller.
			Hard to Understand or Data is Entertwined
		1. Coincidental Cohesion (Bad)
			Completely Unrelated Actions are Performed
			ie...
				print_next_line
				reverse_string_of_characters_comprising_second_parameter
				add_7_to_fifth_parameter
				convert_fourth_parameter_to_floating_point
			These are caused by rules such as...
				Every module will consist of between 35-50 statements.
			Why Bad?...
				Degrades Matainability
				Not Reusable
			Fixing...
				Separate each task into it's own module.
	Cohesiveness in a Class-
		Small Number of Instance Variables
		Methods of class should munipulate those isntance variables.
		Munipulating them all is "maximally cohesive"
		Cohesion/Coupling is important at all data levels.
	Utility Cohesion-
		Inbetween Logical and Temporal Cohesion
		When related utilities which cannot be logically placed in cohesive units are kept together. ie: Math Packages
	Layer Cohesion-
		Inbetween Functional and Communicational Cohesion
		All facilities for providing and accessing a set of related services are kept together and everything else is kept out. ie: API
		Heiarchial
		Layers can be replaced without affecting other layers.
Coupling-
	Categories of Coupling-
		5. Data Coupling	(Good)
			The caller module actually uses every part of the callee, or all members are simple data structures.
			This helps avoid problems found in other forms of coupling.
		4. Stamp Coupling
			Two modules are stamp coupled if a data structure is passed as a parameter but the called module operates on some but not all of the
			individual component of the data structure.
			
			To solve it use more primitive types instead of the object itself (or polymorphic interfaces)
			
			More data than necessary is passed. Difficult to understand. Unlikely to be reusable.
		3. Control Coupling
			Two modules are control coupled if one passes an element of control to the other.
			p needs to know the inner workings of q to work properly. Thus both have to be included when reused.
			
			How to reduce...
				a. have the caller to the modules handle the work instead. (only the caller needs to know the control flow)
				b. using polymorphic operations between the classes.
				c. use look-up table to hash commands. (independant and extensible structure as middleman.)
		2. Common Coupling
			Two modules are common coupled if they both have write access to a global variable
			
			Common Coupled modules can be unreadable and have unintended side effects.
			The entire module has to be known to understand what it is doing. (Hard to understand what even small functions are doing)
			To reuse the module the globals have to come along with it as well.
			There are also security flaws as there are many weakpoints to the same data.
			
			INFORMATION HIDING-
				Usage of Module Depends Only on Information at the Interface
				An Interface should reveal as little as possible about the inner workings.
				An Interface hides design decisions.
		1. Content Coupling (Bad)
			Two Modules are Content Coupled if one directly references the contents of another.
			ie: two separate classes q,p
			p has an instance of q
			p then directly modifies a value of the local of q directly (instead of through say.. a method call of q.)
		
			Changing q means that p has to be changed as well. Additionally it is impossible to reuse p unless you also reuse q.
			
			To solve the issue ensure immutability through setters and getters OR utilizing const/final so they cannot be changed.
			Also do not modify instance variables of objects stored in instance variables of objects.
	Additional Types of Coupling-
		Type Use Coupling(unavoidable)-
			Module uses data type defined in another module.
			Occurs when instance variables are declared.
			If that type definition changes then the caller needs to adjust.
			
			Can Be Reduced-
				Always declare a type to be the most general possible definition that has the required operations.
		Routine Call Coupling-
			One Routine Calls Another
			Present in every system
			Ironically to reduce Routine Call Coupling you encapsulate the routines in routines to call.
		Import Coupling-
			Occurs when an imported component includes another.
			Can be reduced by not importing what you don't use and namespacing.
		External Coupling-
			When a module has a dependancy on things like shared libraries, the os, the hardware.
			It is best to avoid this where possible so that code can be portable.
		Temporal Coupling-
			Can guess from name.