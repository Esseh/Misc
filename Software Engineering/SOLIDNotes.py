SOLID-
	Single Responsibility Responsibility-
		Exactly as it says. A single functionality should be encapsulated into a single module.
	Open-Closed Principle-
		Software Entities should be OPEN for Extension but CLOSED for Modification
		Problems-
			Modification affects everywhere it is called causing a cascade of changes.
		Solution-
			Extending upon existing behaviors instead of modifying doesn't cause cascading changes.
			So utilize "interfaces", "more general types", and "inheritance" to be able to apply the principle.
		Another Problem-
			Data may need to be modified before it is able to be closed.
		Another Solution-
			Consider the shape drawing problem. A solution could be found by allowing the most general class determine the order in a way that depends on a look-up table.
			The lookup table can be passed in so that there is no global dependance.
		Good Habits-
			All data members should be private. Any interactions should be controlled with methods.
	Liskov Substitution Principle-
		Formalism-
			for each object o1 of type S
			there is an object o2 type T
			where for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2, then S is a subtype of T
		English-
			Simply put, a program shouldn't have to behave differently for a type or the subtype. This is to say if a super-type makes certain assumptions
			then all sub-types must follow those assumptions.
			For example a super-type "bird" cannot have a method "fly" because not all birds fly, however if it did then a penguin wouldn't be a valid sub-type.
			LSP cares a lot about semantics. As such a square is not a rectangle even if they're similar.
		More Formalism-
			A precondition of a derived class must be weaker than the base class.
			A postcondition of a derived class must be stronger than the base class.
			IE: the square and rectangle example
	Interface Segregation Principle-
		The client shouldn't have to implement an interface they do not use.
		Suppose there is an interface DrawMovable that requires implementation of draw() and move()
		Instead it is better to split it into Draw which requires implementing draw() and Move which requires implementing move()
	Dependency Inversion Principle-
		Principle...
			1. High-Level Modules should not depend on low-level module "implementations." Both levels should depend on abstractions.
			2. Abstractions should not depend on details.
		Essentially...
			A Super-Type should not know Sub-Types. Additionally these Super-Types are more desirable as they should contain the identity of the module.
			Changing the high level should affect the low level, not the other way around.
			Dependencies in design should thus target interfaces or abstract classes, nothing concrete.
		DIP on Example-
			p.53 of SOLID notes.
			This demonstrates how an abstract interface is used instead of utilizing the details directly. The implementation no longer needs to know about the
			hardware "disk writer."