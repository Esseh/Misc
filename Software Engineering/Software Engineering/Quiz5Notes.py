Design Process...
	is Wicked Problem: Only solvable by partially solving it.
	is a Sloppy Process: Many mistakes and some guesswork, but it's cheaper to revise design than code.
	about tradeoffs and priorities.
	involves restrictions: obeying, reducing, or creating
	is nondeterministic
	is a heuristic process
	emergent: they evolve over time
Design Difficulties...
	Accidental Difficulties: Clusmy Language Syntaxes, Time-sharing OS replaced batch-mode systems, IDEs assisting programming work
	Essential Difficulties: Interfacing with the real world.
Importance of Managing Complexity...
	Minimize the amount of program you have to think about at any given time
	Break complex systems down into simple pieces. The more 'independant' the sub-systems become the easier it is to manage their complexity.
	Sources of infeffective designs...
		1. Complex solutions to simple problems
		2. Simple, incorrect solutions to complex problems
		3. inappropriate complex solution to complex problems
	How to manage...
		1. Minimize the amount of essential complexity the brain has to deal with at any given time.
		2. Keep accidental difficulty from proliferating
Desirable Characteristics of Design...
	1. Minimal Complexity
	2. Ease of Maintenance
	3. Loose Coupling
	4. Extensibility
	5. Reusability
	6. High fan-in: high number of classes use a common class
	7. Low-to-medium fan-out: that common class uses a low-to-medium amount of other classes.
	8. Portability
	9. Leaness: no extra parts
	10. Stratification: heiarchial
	11. Standard Techniques: avoid exotic pieces
Level of Design...
	Make subsystems meaningful by restricting communication
	Communication only on an "on-need" basis
	Better to restrict early then relax rather than the other way around.
	Use Acyclic Graphs in the Design
Common Subsystems...
	Business Rules
	User Interface
	Database Access
	System Dependencies
Design Building Blocks (Heuristics)...
	1. Find real world objects.
	2. Form consistent abstractions
	3. Encapsulate implementation details
	4. Hide Secrets
	5. Inherit when it simplifies design
	6. Identify areas likely to change
	7. Anticipating degrees of change
	8. Keep coupling loose
	9. Look for common design patterns
	10. Others
Common Design Patterns...
	Adapter
	Decorator
	Facade
	Factory
	Observer
	Singleton
	Strategy
	