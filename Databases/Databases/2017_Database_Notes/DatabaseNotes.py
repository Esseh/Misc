Chapter 1: The Worlds of Database Systems
		1.0
			Database Management System(DBMS)/Database Systems-
				A tool for creating and amanaging large amounts of data efficiently and allowing it to persist for long periods of time.
		1.1 The Evolution of Database Systems
			1.1.0
				Database-
					A collection of data managed by a DBMS
				Exectations of a DBMS-
					1. Create new databases and specify schemas...
						A schema is the logical structure of the language defined by a "data-definition language"
					2. Be able to query and modify data...
						utilizing a "query language" or "data-munipulation language"
					3. Store Large amounts of data but retain efficient access
					4. Enable Durability...
						Being able to recover data after failure.
					5. Control Access between users and make behavior expected(isolation) and make sure changes occur as a single action(atomicity)
			1.1.1 Early Database Management Systems
				File Systems-
					Store Data Over Long Periods of Time
					Store Large Amounts of Data
					Do not Support Efficient Access
					No Query Language
					Durability not Garuntees
					While files can be read from multiple users, multiple users cannot write to same file.
				DBMS is necessary when dealing with data made up of many small parts where each part may be modified, examples of such...
					1. Banking Systems: Durability is important so money doesn't vanish
					2. Airline Reservation Systems: Accept large volume of concurrent actions, data must not be lost.
					3. Corporate Record Keeping: Great deal of data, all of which is critical and would not be good to lose.
				Different Models
					1. Tree Based
					2. Graph Based(CODASYL), graph of pointers and hard to use
			1.1.2 Relational Database Systems
				Organizing the data view as tables called 'relations' greatly increased the efficiency for programmers utilizing a database.
				Can now be expressed in a very high level language(SQL.)
			1.1.3 Smaller and Smaller Systems
				tldr; moore's law kicked in and the physical size of a database system shrinks and shrinks.
				PCs can now support database systems.
			1.1.4 Bigger and Bigger Systems
				tldr; what was once a lot isn't a lot anymore. Now there are systems measured in terabytes or petabytes such as google.
			1.1.5 Information Integration
				As systems are acquired or become absolete it becomes necessary to join information together. 
				"data warehouses": information from databases are copied periodically over to a central unified database
				"middleman": specialized software meant to bridge differences between databases
		1.2 Overview of a Database Management System
			1.2.0
				Two Sources of Commands to DBMS...
					1. User asks for data or to modify data
					2. Schema, provided by the administrator
			1.2.1 Data-Definition Language Commands
				DDL commands alter the schema for the database
			1.2.2 Overview of Query Processing
				Answering the Query-
					Query is Parsed
					Query is Optimized by Query Compiler
					Query is now a "Query Plan" an Executable set of Actions
					Execution Engine requests small pieces of data for metainformation
					Requests for data are passed to buffer manager.
					Buffer manager brings portions of data from disk to the main memory buffers(movement measured in "disk blocks")
				Transaction Processing-
					"transaction": units which must be executed atomically and with isolation
					transaction processing is split into two parts...
						1. concurrency-control manager/scheduler: responsible for atomicity and isolation of transactions
						2. logging and recovery manager: responsible for durability of system
			1.2.3 Storage and Buffer Management
				"Storage Manager": Responsible for placement of data on disk as well as movement between disk and main memory.
				"Buffer Manager": Partitions main memory into segments in which data can be loaded into/removed from
				Information that they may need is...
					1. Data: Contents
					2. Metadata: schema descriptions, constraints descriptions, etc.
					3. Log Records: information about recent changes
					4. Statistics: information gathered about data properties
					5. Indexes: data structures that support efficient access to data
			1.2.4 Transaction Processing
				"Transaction Manager": Accepts transaction commands
				"Transaction Commands": Tells the transaction manager where transactions begin and end as well as the expectations in the transactions
				The Transaction Processor Thus Does the Following-
					1. Logging: Changes are store on disk in case something goes wrong.
					2. Concurrency Control: Actions appear atomic, but may actually have many occurring at once
					3. Deadlock Resolution
			1.2.4.5 ACID
				A: atomicity
				C: consistency
				I: isolation
				D: durability
			1.2.5 The Query Processor
				Query Compiler Separated into Three Major Units
					a. Query Parser: Builds tree structure from textual form of query
					b. Query Processor: Checks for Semantics and turns parse tree into algebraic operators
					c. Query Optimizer: Transforms initial plan into the best possible sequence
				The Execution Engine can then use that sequence to actually perform its actions, speaking with each of the modules
				to make sure nothing goes wrong and that all information is logged.
DB1: Introduction and Relational Databases
	Video 1: Introduction
		Attributes of Databases-
			Massive
			Persistent / Durable
			Safe / Consistent
			Multi-User / Concurrent
			Convienent / Physical Data Independance...
				The way the information is stored on disk is independant from the way the programs think about the data
			Efficient / Queries...
				Database Queries are 'declarative', that is to say you ask what needs to be done and don't need to know the algorithm
			Reliable
		Key Concepts-
			Data Model
				ie: graph, tree, XML, JSON
			Schema vs Data
				Schema can be seen as 'types' and Data as 'variables'
				Schema defines the structure, Data adheres to the Schema.
			Data Definition Language(DDL)
				Used to Set up a Schema
			Data Munipulation or Query Language(DML)
				Quering and Modification
		Kinds of People-
			Database Implementor: Implements the Database
			Database Designer: Establishes the Schema
			Application Developer: Creates the Software that will utilize the database for some end-user.
			Database Administrator: Loads Data and keeps things going smoothly. Tunes the database for maximal performance.
	Video 2: The Relational Model
		Database = set of named relations (or tables)
		Each relation has a set of attributes or columns which are named.
		Each tuple or row has a value for each attribute (one entry)
		Each Attribute has a Type or Domain: ie name is string, id is int
			Some domains may be enumerated for example grades: A B C D F, or states CA,NY,...
		Example Tables-
			Student Table-
				[ID ][Name][GPA][Photo]
				[123][Amy ][3.9][URI  ]
				[231][Bob ][3.3][URI  ]
				...
			College Table-
				[Name    ][State][Enrollment]
				[Stanford][CA   ][15000     ]
				[CSUF    ][CA   ][9001      ]
				...
		Schema: Structural Description of Relations in Database, includes the name of the relation/table, the attributes, and their types.
		Instance: Actual Contents at a Given Time
		NULL: A special value available for every type which denotes missing or unknown data. When queries are performed when considering NULL values the related entry should be ignored.
		Key: An attribute in a relation where every value is unique for each entry ie: ID in the student example
			In the College example we may need a combination of attributes to act as the key. This would probably be Name and State
		Why are keys important?
			Random Access by Index means fast queries, being able to find specific values is also useful
			Databases do not have pointers, so if an entry needs to refer to an entry of another relation it is best to do so by key.
			
		Creation in SQL
			"Create Table Student(ID, name, GPA, photo)"
			"Create Table College(name,state,enrollment)"
			
			or
			
			"Create Table Student(ID int, name string, GPA float, photo string)"
			"Create Table College(name string,state char[2],enrollment int)"
	Video 3: Querying Relational Databases
		Steps in Creating and Using a (relational) Database
			1. Design Schema; create with DDL
			2. Load Database with Initial Data(Bulk Load)
			3. Repeat As Much as Necessary; Execute Queries and Modifications
		Example Queries...
			1. All students with GPA > 3.7 applying to Stanford and MIT only
			2. All engineering departments in CA with < 500 applicants
			3. College with highest average accept rate over last 5 years
		Queries return Relations, Because Queries are performed on Relations this action is closed on itself.
		Example Query Langauges..
			Same Query: IDs of students with GPA > 3.7 applying to stanford
			
			Relational Algebra - Formal
				pi.(ID)sigma.(GPA>3.7) ^ cName="stanford"(Student|><|Apply)
			SQL - Implemented
				Select Student.ID
				From Student, Apply
				Where Student.ID = Apply.ID
				And GPA>3.7 and cName="stanford"
Chapter 11: The Semistructured-Data Model
	11.1 Semistructured Data
		11.1.0
			Roles of Semustructured-Data-
				1. Serves as Model for Integration of Databases (describes data in different databases with similar data but different schemas)
				2. Serves as Underlying Model for notations such as XML, used to share information on the Web
		11.1.1 Motivation fot the Semistructured-Data Model	
			Semistructured-Data is 'schemaless' and 'self-describing'
			The data carries information about what its schema is. Thus the schema can change arbitrary and over time.
			The main advantage is added flexibility, even if the parser has to work harder or efficiency has to be lost.
		11.1.2 Semistructured Data Representation
			Such a Database is a collection of nodes
			The Leaf Nodes hold data, whereas relations are held in the interior nodes.
			The root node represents the entire database, every node must be reachable from root.
			Interior nodes hold labels describing relationships or name of attributes between objects.
			p.485 has a nice diagram to trace
		11.1.3 Information Integration Via Semistructured Data
			"Legacy Database Problem": An issue that occurs where an old database must be kept around as it is because it is impossible for existing applications to work without it.
			Independant Databases can utilized Semistructured data as an interface/glue for existing similar, but not equivalent databases.
	11.2 XML(Extensible Markup Language)
		11.2.0
			XML Tags are intended to talk about the meaning of parts of a document
			XML Tags can play the same role as labels in semistructured data.
		11.2.1 Semantic Tags
			XML is formatted a lot like HTML
			<foo> bar </foo>
			A pair of amtching tags and everything inbetween is an 'element'
			a self closing tag ala <foo/> cannot have anything 'between', though it can have attributes.
		11.2.2 XML With and Without a Schema
			Modes of XML...
				1. Well-Formed-
					Invent your Own Tags such as the Semistructured Arc Labels
					Nesting Rules must be obeyed, however there is no predefined schema.
				2. Valid-
					Involves a DTD(Document Type Definition) which specifies allowable tags/grammar for how they may be nested.
					This is an in-between for semistructured and schema based data. For example while a DTD may be strict it can have optional/missing fields
		11.2.3 Well-Formed XML
			The Minimal requirement for well-formed XML is that the document begins with a declaration that it is indeed XML...
				<? xml version = "1.0" encoding = "utf-8" standalone = "yes" ?>
				<Foo>
				...
				</Foo>
			in order, i am an xml document, i'm encoding my character in utf-8, i have no DTD, then a tag representing the element for the document.
			
			A bigger example...
				<? xml version = "1.0" encoding = "utf-8" standalone = "yes" ?>
				<StarMovieData>
				 <Star>
					<Name>Carrie Fisher</Name>
					<Address>
					 <Street>123 Maple St.</Street>
					 <City>Hollywood</City>
					</Address>
					<Address
					 <Street>5 Locust Ln.</Street>
					 <City>Malibu</City>
					</Address>
				 </Star>
				 <Star>
					<Name>Mark Hamill</Name>
					<Street>456 Oak Rd.<Street>
					<City>Brentwood</City>
				 </Star>
				 <Movie>
					<Title>Star Wars</Title>
					<Year>1977</Year>
				 </Movie>
				</StarMovieData>
			Although this doesn't provide the information that they are the stars for that movie.
		11.2.4 Attributes
			In the previous example the stars-in relationship could be handled by nesting the movie element inside.
			This could be done concisely as a single tag...
				<Movie title="Star Wars" year=1977 />
		11.2.5 Attributes that Connect Elements
			Concisely, attributes can connect elements.
			By giving the movies ids such as sw, and the actors ids such as cf
			we can add elements such as...
				starredIn = "sw"		to each of the actors
				starsOf = "cf","mh"		to the movie in which they both started in
			As a result, the semistructured relationship is complete. Without nesting the elements can express their full relationship such as in the example page from before.
		11.2.6 Namespaces
			Namespaces can be used to prevent conflicting names.. ie:
				<md:StarMovieData xmlns:md="http://...">
			In this case we create a namespace md:, in this case md will refer specifically to everything linked by the URI.
			So when referring to those specific tags we prefix it with md:
		11.2.7 XML and Databases
			Flexibiltiy is Useful, To Utilize XML in Relational Databases there are two options...
				1. A specialized parser meant to deal with data in that parsed form.
				2. Store as relations understanding additional metadata that would be required.
	11.3 Document Type Definitions
		11.3.0
			A DTD(Document Type Definition) provides a means to provide a schema for shared definitions between XML files
		11.3.1 The Form of a DTD
			Basic Structure of DTD-
				<!DOCTYPE root-tag [
					<!ELEMENT element-name (components)>
					...
				]>
			The root-tag surrounds a document that conforms to the DTD.
			The element-name refers to a required element
			components can refer to sub-elements OR leaf elements.
			There are two special components...
				1. EMPTY   , basically a null element.. remember no parenthesis for EMPTY...
					ie: <!ELEMENT Foo EMPTY> can only refer to <Foo/>
				2. (#PCDATA) , a text value .. meaning it is a leaf node...
					ie: <ELEMENT Foo (#PCDATA)> could refer to <Foo> text_here </Foo>
			Regex operators can follow component names...
				1. (Foo*) , zero or more instances of Foo allowed
				2. (Foo+) , one or more instances of Foo allowed
				3. (Foo?) , one or zero instances of Foo allowed
				4. (Foo|Bar) , either Foo or Bar can fulfill the requirement.
				5. Parenthesis can be used to further group sections presenting options.
		11.3.2 Using a DTD
			<?xml version = "1.0" encoding = "utf-8" standalone = "no"?>
			<!DOCTYPE Stars SYSTEM "star.dtd">
			note: standalone is now set to no.
			SYSTEM and then the file path refers to the location of the DTD being used.
			The Stars would refer to the schema in the file being used. (Also matching the root tag)
		11.3.3 Attribute Lists
			These are ways of asserting the usage of attributes for a given element.
			ie-
				<!ELEMENT Movie EMPTY>
					<!ATTLIST Movie
						title CDATA #REQUIRED
						year  CDATA #REQUIRED
						genre (comedy | drama | csiFi | teen) #IMPLIED
					>
			in this example the Movie element has three attributes title,year,and genre. 
			title and year are required
			genre is optional.
			In addition genre is actually an enumerated type. (notice the various options made possible by the or operator and parenthesis capture group)
			also, CDATA just refers to escaped strings
		11.3.4 Identifiers and References
			by setting the attribute type to ID it then refers to the unique id of that element.
			by setting the attribute type to IDREF it then expects the ID of another element to act as a sort of pointer. IDREFS will accept a list of ID separated by whitespace.
	11.4 XML Schema
		11.4.1 The Form of an XML Schema
			XML Schema is an XML Document itself
			ie-
				<? xml version = "1.0" encoding = "utf-8" ?>
				<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
					...
				</xs:schema>
			xs in this case is the namespace. 
			Thus we can use tags to build out schema.
		11.4.2 Elements
			The form of an XML schema element is as follows...
				<xs:element name = element name type = element type>
					containts and/or structure information
				</xs:element>
			ie-
				<xs:element name = "Title" type = "xs:string" />
				<xs:element name = "Year" type = "xs:integer" />
				<xs:element name = "Attended" type = "xs:boolean" />
		11.4.3 Complex Types
			A complex type is a custom type.
			They are defined with the following form...
				<xs:complexType name = type name>
				 <xs:sequence>
					list of element definitions
				 </xs:sequence>
				</xs:complexType>
			ie-
				<xs:complexType name = "movieType">
					<xs:sequence>
						<xs:element name = "Title" type = "xs:string" />
						<xs:element name = "Year" type = "xs:integer" />
					</xs:sequence>
				</xs:complexType>
			Some additional attributes can be added to an element if there can be more than one of the same ocurrences..
				minOccurs = "some number" , There has to be atleast this many instances of this attribute.
				maxOccurs = "some number" , There can only be up to this many instances of this attribute.
				maxOccurs = "unbounded"   , There can be as many instances so long as it reaches the minimum requirement.
				
				these can take any number >= 0 for xs:choice and xs:sequence, but for xs:all max can only be "1".
			
			Instead of xs:sequence the following can be used...
				xs:all , each element must occur exactly once each
				xs:choice , exactly one of the elements between the tag must occur
		11.4.4 Attributes
			using xs:attribute instead of xs:element denotes a leaf node (cannot contain XML elements or have the properties of XML elements)
			Useful to know the context.
		11.4.5 Restricted Simple Types
			the format-
				<xs:simpleType name = type name>
					<xs:restrinction base = base type >
						upper and/or lower bounds
					</xs:restriction>
				</xs:simpleType>
			ie-
				<xs:simpleType name = "grades">
					<xs:restriction base = "xs:string">
						<xs:enumeration value = "A"/>
						<xs:enumeration value = "B"/>
						<xs:enumeration value = "C"/>
						<xs:enumeration value = "D"/>
						<xs:enumeration value = "F"/>
					</xs:restriction>
				</xs:simpleType>
				
				or
				
				<xs:simpleType name = "singleDigits">
					<xs:restriction base = "xs:integer">
						<xs:minInclusive value = "0"/>
						<xs:maxInclusive value = "9"/>
					</xs:restriction>
				</xs:simpleType>
		11.4.6 Keys in XML Schema
			Format-
				<xs:key name = key name>
					<xs:selector xpath = path description>
					<xs:field xpath = path description>
				</xs:key>
			Example-
				<xs:key name = "movieKey">
					<xs:selector xpath = "Movie"/>
					<xs:field xpath = "Title"/>
					<xs:field xpath = "Year"/>
				</xs:key>
			That is to say in the example we can find a unique 'Movie' composed of some type that has 'at the very least Title and Year elements'
		11.4.7 Foreign Keys in XML Schema
			Similar to IDREFS, format-
				<xs:keyref name = foreign-key name refer = key name>
					<xs:selector xpath = path description>
					<xs:field xpath = path description>
				</xs:keyref>
			Example-
				<xs:keyref name = "movieRef" refers = "movieKey">
					<xs:selector xpath = "Star/StarredIn" />
					<xs:field xpath = "@title" />
					<xs:field xpath = "@year" />
				</xs:keyref>
			This means in the attribute StarredIn in the Star element
			we can look at the title and year fields of that entry and use it to produce a valid movieKey, which can point to a unique movie element.
DB2: XML Data
	Video 2: DTDs, IDs, and IDREFs
		Features of DTD/XSD-
			Programs can assume structure
			Specification
			CSS/XSL
			Less Flexibility
			DTDs can be messy			
DB3: JSON Data
	Video 1: Introduction to JSON Data
	Video 2: JSON Demo
Chapter 2: The Relational Model of Data
	2.1 An Overview of Data Models
		2.1.1 What is a Data Model?
			Composed of 3 parts...
				1. Structure of the Data: How it is shaped.
				2. Operations on the Data: What can be done with the structure.
				3. Constraint on the Data: Ways of describing limitations
		2.1.2 Important Data Models
			1. Relational Model: ie- SQL
			2. Semistructured Model: ie- XML
		2.1.3 The Relational Model in Brief
			Rows of Entries, Columns of Descriptions
			ie...
			id | name | deceased
			 0 | Joe  | true
			 1 | Mary | false
		2.1.4 The Smistructured Model in Brief
			Trees/Graphs instead of Arrays ie: XML
	2.2 Basics of the Relational Model
		Columns = Attributes
		Schema  = Set of Attributes ie: Movies(title,year,length,genre)
		describes a relation Movies with the columns title, year, length, and genre.
		component= an attribute in use
		Domains = Contraint on components. ie: Movies(title:string, year:integer, length:integer, genre:string)
		The entries in a relation are expected to change, however changing the schema is expensive.
		Key = attribute/attribute combination that is unique across the relation. Useful for ensuring unique entries are found and modified.
	2.3 Defining a Relation Schema in SQL
		2.3.0 Introduction
			There are two aspects to SQL...
				1. The Data-Definition sublanguage for schemas
				2. The Data-Munipulation sublanguage for queries
		2.3.1 Relations in SQL
			SQL Makes a Distinction between three kinds of relations...
				1. Stored Relations / Tables: The physical relation in the DB
				2. Views: The part stored as computation when needed.
				3. Temproary Tables: Constructed when performing queries/data modification. When they are no longer necessary they are thrown away.
		2.3.2 Data Types
			1. Character Strings...
				a. CHAR(n)			- String of n chacters
				b. VARCHAR(n)		- Different Implementation, Same as CHAR functionally, the underlying strings are dynamic up to the max size.
			2. Bit Strings...
				a. BIT(n)
				b. BIT VARYING(n)
			3. BOOLEAN...
				includes a third value "UNKOWN"
			4. INT/INTEGER
			5. SHORTINT
			6. FLOAT(n,d)/REAL(n,d)/NUMERIC(n,d)...
				n digits
				decimal point is d points to the right.
		2.3.3 Simple Table Declaration
			CREATE TABLE...
				Creates a relation. IE
				CREATE TABLE Movies (
					title 	    CHAR(100),
					year    	INT,
					length  	INT,
					genre   	CHAR(10),
					sudioName	CHAR(30),
					producerC#	INT
				);
		2.3.4 Modifying Relation Schemas
			DROP TABLE...
				delete a relation. IE
				DROP TABLE Movies;
			ALTER TABLE...
				Changes the schema TWO EXAMPLES
				
				ALTER TABLE Movie ADD	reviewID INT;
				ALTER TABLE Movie DROP	producerC#;
				
				This added and removed a column respectively.
		2.3.5 Default Values
			EXAMPLE...
				CREATE TABLE Movies (
					title 	    CHAR(100) DEFAULT 'NEED NAME',
					year    	INT  	  DEFAULT 0,
					length  	INT		  DEFAULT 0,
					genre   	CHAR(10)  DEFAULT 'NEED GENRE',
					sudioName	CHAR(30)  DEFAULT 'NEED STUDIO',
					producerC#	INT       DEFAULT 0
				);
		2.3.6 Declaring Keys
			EXAMPLE...
				CREATE TABLE Movies (
					title 	    CHAR(100) DEFAULT 'NEED NAME',
					year    	INT  	  DEFAULT 0,
					length  	INT		  DEFAULT 0,
					genre   	CHAR(10)  DEFAULT 'NEED GENRE',
					sudioName	CHAR(30)  DEFAULT 'NEED STUDIO',
					producerC#	INT       DEFAULT 0
					PRIMARY KEY (title,year)
				);
			OR...
				CREATE TABLE Movies (
					title 	    CHAR(100) DEFAULT 'NEED NAME',
					year    	INT  	  DEFAULT 0,
					length  	INT		  DEFAULT 0,
					genre   	CHAR(10)  DEFAULT 'NEED GENRE',
					sudioName	CHAR(30)  DEFAULT 'NEED STUDIO',
					producerC#	INT       DEFAULT 0
					UNIQUE (title,year)
				);
			The difference is UNIQUE allows NULL keys.
	2.4 An Algebraic Query Language
		2.4.3 OVerview of Relational Aglebra
			a. Set Operations (union, intersection, difference)
			b. Operation that remove parts of a relation: "selection" to eliminate rows and "projection" to eliminate columns.
			c. Combining tuples in relations through Cartesian Products or "joins"
			d. "renaming", changes the name of relations/attributes without affecting the data.
		2.4.4 Set Operations on Relations
			E U S
			S n S
			R - S
			For these to work the relations must have the same types of attributes that have the same underlying type constraints.
		2.4.5 Projection
			Creates a new relation from R with only a limited amount of the original attributes.
			pi attr1, attr2, attr3 (R)
		2.4.6 Selection
			Generates a subset of R such that it only contains the entries fulfilling condition.
			sigma condition (R)
		2.4.7 Cartesian Product
			Produces all Possible Combinations of Entries Between Relations. Common attributes are made distinct through namespacing.
			R >< S
		2.4.8 Natural Join
			Produces all Possible Combinations but only so that common attributes match (and thus don't produce a new attribute.)
			If there are common attributes and they don't match then that tuple is ignored.
			R |><| S
		2.4.9 Theta-Joins
			Cross Product with a Condition C
			R |><|C S
		2.4.11 Naming and Renaming
			rename a relation R into S
			it's attributes are renamed A1,...,AN
			p S(A1,...AN)(R)
		2.4.13 Linear Notation for Algebraic Expressions
			1. the relation Answer will represent the final step.
			2. := is the assignment operator			
Chapter 5: Algebraic and Logical Query Languages
	5.1 Relational Operations on Bags
		5.1.0 Introduction
			Bags are sets that allow multiple occurences of an element...
				A | B
				1 | 2
				3 | 4
				1 | 2
				1 | 2
		5.1.1 Why Bags?
			Increased Efficiency...
				Union doesn't need to remove duplicates.
				Projection can just pass everything along. It doesn't need to make cross-comparisons.
			More Allowed Operations...
				ie: Averaging Integers, Sets lose information from duplicates.
		5.1.2 Union, Intersection, and Difference of Bags
			Union: Add the collective elements together.
			Intersect: Restrict common instances to whatever has less of them.
			Difference: Handled one by one.
		5.1.3 Projection of Bags
			Same as normal but include duplicates.
		5.1.4 Selection on Bags
			Same as normal but include duplicates.
		5.1.5 Product of Bags
			Cartesian Product is also done with the duplicates.
		5.1.6 Joins of Bags
			...
	5.2 Extended Operators of Relational Algebra
		5.2.0 Introduction
			duplicate-elimination operator: sigma
			aggregation operators: apply to grouping operators
			groupon operator: gamma
			extended projection: pi
			sorting operator: tau
			outerjoin: joins with dangling tuples initialized to null
		5.2.1 Duplicate Elimination
			Consider R...
				A | B
				1 | 2
				3 | 4
				1 | 2
				1 | 2
			sigma(R)...
				A | B
				1 | 2
				3 | 4
		5.2.2 Aggregation Operators
			1. SUM(Attr)
			2. AVG(Attr)
			3. MIN/MAX(Attr)
			4. COUNT(Attr)
		5.2.4 The Grouping Operator
			Best By Example...
				gamma Att0, Op1(Att1)->Att1Rename,..., Opn(Attn)->AttnRename (R)
		5.2.5 Extending the Projection Operator
			Examples...
				pi A,B + C -> X(R) 			: Project A and B+C renamed as X from R	
				pi A,B || C -> X (R)		: Project A and B cat C renamed as X from R
		5.2.6 The Sorting Operator
			Example..
				Tau A,B(R)  		: Sort the relation R by attribute A, breaking ties with B
		5.2.7 Outerjoins
			R |><|o S
			Perform the Natural Join R and S, however if a tuple doesn't join with another tuple include the incomplete join into the result
			with the remaining attributes as null.
	5.3 A Logic for Relations
		5.3.1 Predicates and Atoms
			R(a1,...,an)
			True if it matches a relation, otherwise false.
			ie for...
				A | B
				1 | 2
				3 | 4
				
				R(1,2) is true
				R(3,4) is true
				R(1,4) is false
				R(1,z) returns true if z == 2, otherwise false.
		5.3.2 Arithmetic Atoms
			ie: x < y would accept all values in a relation where x is less than 5.
		5.3.3 Datalog Rules and Queries
			Rd(x,y) <- R(x,y,z) AND x >= 50 AND x <= 100 AND x < y
			In this example I'm creating a project of R named Rd from its x and y attributes.
			Additionally I'm only accepting the entries where x is in the range [50,100] and that the x value in that entry is less than the y value in that entry. 
		5.3.5 Extensional and Intensional Predicates
			Extensional: Predicates whose relations are stored in a database. Cannot be the head of a rule. (immutability)
			Intesional : Relations computed by applying datalog rules.
	5.4 Relational Algebra and Datalog
		For all intents and purposes you can treat Datalog as a set comprehension language. Because of this you can construct relational algebra operations
		off of its primitives. (although this doesn't hold true for Bag Based Relational Algebra)
Chapter 6: The Database Language SQL
	6.1 Simple Queries in SQL
		6.1.0 Simple Overview
			SELECT attr1,attr2		alternatively SELECT attr1 as rename1,attr2 as rename2		,	 additionally operations can be performed on the attributes ie: SELECT attr1+attr2,attr1-3
			FROM relation
			WHERE predicates		, valid operators are =,<>(not equal),<,>,<=,>=, LIKE,AND, OR, NOT,and any operators that apply to the data such as +,-,* for numeric types and || for string types.
			ORDER BY attrList
			
			here is an example of LIKE
			WHERE title LIKE 'Star ____';
			
			This would return true for both Star Wars and Star Trek
			
			WHERE title LIKE'%' ' Wars';
			Would return true for both Star Wars and Sakura Wars.
			
			You can also register escape characters like so 
			WHERE title LIKE '50x% ___' ESCAPE 'x'
			This would return true for 50% Off
		6.1.5 Dates and Times
			Cosntants...
				DATE 'year-month-day'
				TIME 'hour:minutes:seconds.fractionsofseconds'
				time accepts addition and subtraction between time types.
				TIMESTAMP 'year-month-day hour:minutes:seconds.fractionsofseconds'
		6.1.6 Null Values and Comparisons Involving NULL
			Operators on Null produce Null
			Boolean logic on NULL produces "UNKNOWN" a third truth value.
	6.2 Queries Involving More Than One Relation
		6.2.0 Simple Overview
			Join...
				SELECT R1.Attr1, R2.Attr1
				FROM	R1, R2
			
			Natural Join...
				SELECT R1.Attr2,Attr1,Attr2
				FROM	R1, R2
				
			Renaming Cross Product...
				Suppose you wanted the cross product of an attribute with itself but with their own distinct elements...
				
				SELECT R1.Attr1, R2.Attr1
				FROM	R R1, R R2
		6.2.5 Union, Intersection, and Difference Queries
			UNION, INTERSECT, EXCEPT respectively
			You can group computed relations in parenthesis
	6.3 Subqueries
		6.3.0 Reminder
			Remember that a query returns a relation. Wrap it up in parenthesis and it can be used as part of a query.
		6.3.2 Conditions Involving Relations
			EXISTS R	true if Relation is non empty
			s IN R		true if atleast one instance of s is inside of R
			s > ALL R	true if s is > every instance inside of R, > can be replaced with any comparison operator
			s > ANY R	true if s is > atleast one instance inside of R
		6.3.6 SQL Join Expressions
			R CROSS JOIN R2
			R CROSS JOIN R2 ON AttrList		, project combined with cross product.
		6.3.7 Natural Joins
			R Natural JOIN R2
		6.3.8 Outerjoins
			R NATURAL (LEFT|RIGHT|FULL) OUTER JOIN R2
	6.4 Full-Relation Operations
		6.4.1 Eliminating Duplicates
			SELECT DISTINCT ...
		6.4.2 Duplicates in Unions, Intersections, and Differences
			If we want to retain duplicates in set operations with will follow the set operator with ALL
			R1 UNION ALL R2
		6.4.4 Aggregation Operators
			SUM, AVG, MIN, MAX, COUNT
			ie: SELECT AVG(salary)
			or 
			SELECT SUM(numberOfTimesAttended) AS totalTimesAttented
		6.4.5 Grouping
			GROUP BY attr
			will make sure that the instances with common attr will be grouped together.
		6.4.7 HAVING Clauses
			HAVING predicate
			removes grouped relations that do not fulfull the predicate
	6.5 Database Modifications
		6.5.1 Insertion
			INSERT INTO Relation(attr1,...,attr2) VALUES(v1,...,v2)	or		INSERT INTO Relation VALUES(v1,...,v2)
			In the second case you must ensure it matches the order of the relation.
		6.5.2 Deletion
			DELETE FROM R WHERE Predicate
		6.5.3 Updates
			UPDATE R 
			SET <attribute modifications>
			WHERE Predicate
	6.6 Transactions in SQL
		6.6.1 Serializability
			That they appear to not overlap.
		6.6.2 Atomicity
			Actions must appear to occur all at once.
		6.6.3 Transactions
			Isolated groups of isntructions occur together.. However their changes only appear if they complete entirely. If anything were to occur the changes are 'rolled back'
			when they finish they are 'comitted' and are considered live.
			START TRANSACTION
			COMMIT
			ROLLBACK
		6.6.4 Read-Only Transactions
			SET TRANSACTION READ ONLY;
			SET TRANSACTION READ WRITE;
			
			When read only it cannot be rewritten, but parallel reads are safe.
			
			During a transaction typically the data cannot be read, however there may be cases where reading this dirty data is okay.. if so then the following can be used.
			SET TRANSACTION READ WRITE
			ISOLATION LEVEL READ UNCOMMITTED
		6.6.6 Other Isolation Levels
			SET TRANSACTION ISOLATION LEVEL READ COMMITTED; 		Can only be read if it is comitted.
			SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;		Can read uncommitted data so long as it hasn't been modified yet.
			SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; 			Can only begin a transaction if it can begin a transaction (default)
Chapter 12: Programming Languages for XML
		12.1 XPath
			12.1.1 The XPath Data Model
				The shape of data in the relational model is a bag of tuples.
				In XPath is is a sequence of items.
				items are defined as...
					1. Primitive Type
					2. Node(Document, Element, Attribute)
			12.1.2 Document Nodes
				doc(file name)   		will make a document node from a file
			12.1.3 Path Expressions
				Starting at the root of a document follow into tags...
				/T1/T2/T2
				/T1 is the root node, and is typically the doc name.
			12.1.5 Attributes in Path Expressions
				/T1/.../@AttributeName
				will give the value of the attribute AttributeName
			12.1.6 Axes
				There are other modes of travel through a document for example...
				//City 
				would return all City elements in the order they appear in the document (linear instead of tree movement)
				Alternatively...
				/T1/T2//City
				would only look for the cities within T2.
				
				. means self
				.. means parent
			12.1.8 Wildcards
				* acts as a wildcard, it can stand for anything at a given level.
			12.1.9 Conditions in Path Expressions
				Using square brackets []
				and putting a condition [condition] on a path can be used to limit queries.
				ie: /Earth[//City = "Malibu"]/Name will return all Name elements in order relative to Earth such that they exist within cities called Malibu.
				[i] is True only if it's the ith element inside of a node
				[T] is True only if T is a subnode.
		12.2 XQuery
			12.2.1 XQuery Basics
				Every XPath Expression is an XQuery Expression
				XQuery is Functional
			12.2.2 FLWR Expressions
				for- , let- , where- ,return-
				First there are 0 or more for/let clauses interlaced
				then an optional where clause
				then exactly one return clause
				ie...
					let $.movies := doc ("movies.xml")
					for $m in $movies/Movies/Movie
					where $m/@Name != "Star Wars"
					return $m/Version/Star
			12.2.3 Replacement of Variables by Their Values
				EXAMPLE
				let $starSeq := (
					let $movies := doc("movies.xml")
					for $m in $movies/Movies/Movie
					return $m/Version/Star
				)
					return <Stars>{$starSeq}</Stars> 
			12.2.4 Joins in XQuery
				data(E)		extracts value of an element
				
				AN EXAMPLE JOIN
					let $movies:= doc("movies.xml"),
						$stars := doc("stars.xml")
						for $s1 in $movies/Movies/Movie/Version/Star, $s2 in $stars/Stars/Star
						where data($s1) = data($s2/Name)
						return $s2/Address/City 
			12.2.5 XQuery Comparison Operators
				If the value is a string, when comparing it will assume the value.
			12.2.6 Elimination of Duplicates
				EXAMPLE
				let $starSeq := distinct-values(
					let $movies := doc("movies.xml")
					for $m in $movies/Movies/Movie
					return $m/Version/Star
				)
				return <Stars>{$starSeq}</Stars> 
			12.2.7 Quantification in XQuery
				every variable in expression1 satisfies expression2
				some variable in expression1 satisfies expression2
			12.2.8 Aggregations
				The usual SQL aggregations are inside.
			12.2.9 Branching in XQuery Expressions
				if (expression1) then expression2 else expression3
			12.2.10 Ordering the Result of a Query
				specifying order before return allows ordering of lists. ie
				let $movies := doc("movies.xml")
				for $m in $movies/Movies/Movie,
				$v in $m/Version
				order $v/!Dyear
				return <Movie title = "{$m/!Dtitle}" year "{$v/!Dyear}" /> 
Chapter 3: Design Theory for Relational Databases
	3.1 Functional Dependencies
		3.1.0 Introduction
			A functional dependency is a statement of a type that generalizes the idea of a key for a relation.
		3.1.1 Definition of Functional Dependency
			A FD on R is a statement of the form...
				If two tuples of R agree on all attributes A1,...,An(for each of these tuples A has the same value
				then they must also agree on all of another list of attributes B1,...,Bn
			
				This is written A1,...,An -> B1,...,Bn
				
				What's important is this gives us a good way of reasoning about Keys.
			An Example Looking at a Relation....
				title		|		year	|	length	|	genre	|	studioName	|	starName
				Star Wars 			1977 		124 		SciFi 		Fox 			Carrie Fisher
				Star Wars 			1977 		124 		SciFi		Fox 			Mark Hamill
				Star Wars 			1977 		124 		SciFi 		Fox 			Harrison Ford
				Gone With the Wind 	1939 		231 		drama 		MGM 			Vivien Leigh
				Wayne's World 		1992 		95 			comedy 		Paramount 		Dana Carvey
				Wayne's World 1		992 9		5 			comedy 		Paramount 		Mike Meyers 
			We can see that title,year -> length,genre,studioName
			Because we can assume that the title,year combination to be a unique key.. and if it is the same then those following attributes will always be the same.
			On the otherhand title,year-> starName
			will be false, as the attribute is different for each entry.
			
			From this we can take that given A1,...,An -> B1,...,Bn
			We can actually separate the relation.
		3.1.2 Keys of Relations
			We say that a set of one or more attributes A1,...An is a key for a relation if...
				1. if they functionally determine all attributes of the tuple (produces a unique item)
				2. no proper subset of {A1,...,An} functionally determines all other attributes of R (a key is minimal)
			In that sense with the given example title,year would logically seem like a key, but that is not the case because of the starName column. 
			title,year,starName would be the actual minimal key. 
			Although if we were to pull out starName into some other relation then title,year WOULD be the minimal unique key.
		3.1.3 Superkeys
			a superset of key.
			tldr it only needs to satisfy the first property of keys.
			1. if they functionally determine all attributes of the tuple (produces a unique item)
	3.2 Rules About Functional Dependencies
		3.2.1 Reasoning About Functional Dependencies
			Suppose we have R(A,B,C) where A->B and B->C, then A->C also.
			Equivalency...
				Two sets of FD S,T are equivalent if every relation instance that satisfies S also satifies T
			Follows...
				a Set of FD S follows a Set of FD T if every relation instance in T also satisfies every relation instance in S
			Thus S and T are equivalent if they follow eachother.
		3.2.2 The Splitting/Combining Rule
			The Splitting Rule...
				A1,...,An -> B1,...,Bm => A1,...,An -> Ai, i = 1,...,m
				tldr; if you have many attributes B1,...,Bm that are related to a unique key A1,...,An you can split it up. 
				Following it backwards and you have the 'combining rule'
		3.2.3 Trivial Functional Dependencies
			A trivial FD has a right side that is a subset of it's right side.
		3.2.4 Computing the Closure of Attributes
			The closure of A1,...,An under the FD's in S is the set of attributes B such that 
			S -> A1,...,An -> B
			This continues recursively until you find some B' such that it is trivial.
		3.2.6 The Transitive Rule
			If A1,...,An -> B1,...,m and B1,...,Bm -> C1,...,Ck
			then A1,...,An -> C1,...,Ck
			
			In either direction we can cascade our relationships.
		3.2.7 Closing Sets of Functional Dependencies
			A minimal basis for a relation is a basis B that satisfies...
				1. All the FD's in B have singleton right sides.
				2. If any FD is removed from B, the result is no longer a basis
				3. If for any FD in B we remove one or more attributes from the left side of F, the result is no longer a basis.
			EXAMPLE-
				Consider a relation R(A,B,C) such that each attribute FD the other two attributes.
				Here are the full set of derived FD...
				A->B, A->C, B->A, B->C, C->A, C->B
				AB->C, AC->B, BC->A, A->BC,B->AC,C->AB,
				A->A,B->B,C->C
				
				singleton right sides
				A->B, A->C, B->A, B->C, C->A, C->B
				AB->C, AC->B
				A->A,B->B,C->C
				
				remove trivial
				A->B, A->C, B->A, B->C, C->A, C->B
				AB->C, AC->B
				
				expand complex FD
				A->B, A->C, B->A, B->C, C->A, C->B
				A->B->C, A->C->B
				
				cascade FD
				A->C, B->A, C->A
				A->B->C, A->C->B	
				(A->B) (B->C) (C->B)
				
				we can already reach A->C through A->B->C...
				B->A, C->A	
				(A->B) (B->C) (C->B)
				
				minimize further...
				B->A, A->B, B->C, C->B
		3.2.8 Projecting Functional Dependencies
			Suppose we have the following situation
			R1 = pi L (R)
			If R has some FD S, what FD hold in R1
			
			We find this by computing the projection of functional dependencies
			ALL FD That...
				a. Follow from S
				b. Involve only attributes of R1
	3.3 Design of Relational Database Schemas 
		3.3.1 Anomolies
			Problems that Occur When we Try to Shove Too Much Information into a single relation...
				1. Redundancy: Repeated information
				2. Update Anomolies: Other entries might not be properly updated when one gets updated.
				3. Deletion Anomolies: if a set of value becomes empty information may be lost for good unintentionally.
		3.3.2 Decomposing Relations
			To resolve anomolies we need to decompose the relation.
			For example information that isn't expected to change can be moved into another relation of just that information.
			This solves each anomoly.
		3.3.3 Boyce-Codd Normal Form
			BCNF is a form the data can be organizedf into to ensure that the above anomolies cannot occur.
			tldr; the left side of every relation must be a key or superkey
	3.4 Decomposition: The Good, The Bad, and The Ugly
		3.4.0 Desired Properties of Decomposition
			1. Elimination of Anomolies
			2. Recoverability of Information: Can the original relation be recovered?
			3. Preservation of Dependencies: If we rejoin the relations will they have the same FD?
		3.4.1 Recovering Information from a Decompostion
			Lossless Join-
				A situation where you can recover an original relation after decomposition
				In Short, if a Lossless Join is possible, taking the Natural Join of each relation will reconstruct the original relation.
				Thus if after natural joining each relation there is additional(bogus) information then the decomposition violates recoverability of information.
			"Chase"-
				An algorithm for testing if a projection of a relation onto a decomposition allows it to be recovered.
		3.4.2 The Chase Test for Lossless Join
			p.120 for example
			Essentially the goal is to assert the properties promised by the FD across the relation 
			and see if they're enough to get back an arbitrary original value.	
		3.4.3 Why the Chase Works
			Simply put, after the assertions if you generate the original value then it is lossless because the original relation was recovered.
			On the otherhand not being able to recover it even after applying each FD assertion would imply that the original relation can't be recovered.
		3.4.4 Dependency Preservation
			p.122 Provides examples where dependancies are not preserved when putting into BCNF.
	3.5 Third Normal Form
		3.5.1 Introduction
			Like BCNF, but all that is required is that the right hand elements are elements of 'some key'
			As long as something is a member of some key then it is referred to as 'prime'
			So the left side now must be 'some key' and the right side must be 'prime'
		3.5.2 The Synthesis Algorithm for 3NF Schemas
			Satisfies properties 2,3 but not necessarily 1.
			Steps...
				1. Find a Minimal Basis for F (G)
				2. For each FD X -> A in G use XA as the schema of one of the relationships in the decomposition.
				3. if none of the sets of relations from 2 is a superkey of R add another relation whose schema is a key for R.
		3.5.3 Why the 3NF Synthesis Algorithm Works
			For 3NF three things must be shown...
				1. Lossless Join...
					Because the relations are computed through the closure process the chase test will show a lossless join.
				2. Dependency Preservation...
					Each FD of the minimal basis has all of it's attributes in some relation of the decomposition.
				3. Third Normal Form...
					If we have to add a relation whose schema is a key then this relation is in 3NF.
	3.6 Multivalued Dependencies
		3.6.0 Introdution
			"Multivalued Dependency"-
				An assertion that two attributes or sets of attributes are independant of one another. 
		3.6.1 Attribute Independance and Its Consequent Redundancy
			MVD Holds If for each pair of tuples t,u of R that agree on the set of attributes A, we can find in R some tuple v that agrees...
				1. With both t and u on A
				2. with t on attributes B
				3. With u on all attributes of R that are not among A or B
			A MVD is represented as follows A ->> B
			One way of looking at it is given some AB -> C, A -> B
			So A->B is independant and A -> C breaking up the relation.
		3.6.3 Reasoning About Multivalued Dependancies
			MVD follows the same rules as normal dependancies expect for the splitting/combining rules
			However MVD Have their own properties...
				FD Promotion...
					Every FD is also a MVD
				Complementation Rules...
					This can be seen as independant 'sibling' MVD
					For example name -> street city title year
					by promotion
					For example name ->> street city title year
					then by complementation
					name ->> street city
					name ->> title year
		3.6.4 Fourth Normal Form
			The goal of fourth normal form is to eliminate all nontrivial MVDs and any FDs that violate BCNF.
			Essentially the BCNF condition, but applied mith MVD instead of FD
		3.6.5 Decomposition into Fourth Normal Form
			Steps Towards 4NF...
				1. Find 4NF violations in R, say A...n ->> B...m where {A1..n} is not a superkey
				2. If there is a violation break the violating schema into two schemas...
					a. R1 whose schema is in A... and B...
					b. R2 whose schema is in A... and all attributes of R that are not among A... or B...
				3. Find the FDs and MVDs that hold in R1 and R2 (recursively break them down)
		3.6.6 Relationships Among Normal Forms p.135
			4NF implies BCNF implies 3NF
	3.7 An Algorithm for Discovering MVD's
		3.7.1 MVD Closure
			Closure on MVD...
		3.7.2 Extending the Chase to MVDs
			Example on p.139
		3.7.3 Why the Chase Works for MVD's
			Essentially the Same as Normal Chase
		3.7.4 Projecting MVDs
			Example on p.141
DB8:Relational Design Theory
	... TODO BEFORE EXAM
Chapter 4: High-Level Database Models
		4.0 Introduction
			Relational Dabase Modeling and Implementation Process-
				Ideas -> High-Level Design -> Relational Database Schema -> Relational DBMS
			ODL(Object Description Language)-
				A language for representing a database as objects and classes
		4.1 The Entity/Relationship Model
			4.1.0 Introduciton
				In the ER Model the structure of data is represented graphically as an "entity-relationship diagram" using three principle elements types...
					1. Entity Sets
					2. Attributes 
					3. Relationships
			4.1.1 Entity Sets
				An entity is an abstract object of sorts. A collection of similar entities forms an "entity set"
				ie: A movie is an entity, but the set of all movies is an entity set
			4.1.2 Attributes
				Attributes are properties shared by entity sets. 
				ie: A movie has attributes title and length.
			4.1.3 Relationships
				Relationships are connections between Entity Sets.
				ie: Stars-In connects Stars and Movies.
			4.1.4 Entity-Relationship Diagram
				An E/R Diagram example is given on p.150
			4.1.5 Instances of E/R Diagrams
				tl;dr the diagram may not exactly match the relation, although a database could be built off of the graph easily.
			4.1.6 Multiplicty of E/R Relationships
				In relationships it is sometimes useful to provide restrictions on it's multiplicty.
				Instead of having many to many connections we may only desire one to many or many to one.
				In addition one-to-one and many-to-many are possible.
			4.1.7 Multiway Relationships
				A good example is provided on p.153
			4.1.8 Roles in Relationships
				We label the edges in relationships with names called "roles", for example a movie could relate to movie by being a 'sequel of' or an 'original'
				example on p.154
			4.1.9 Attributes on Relationships
				Attributes can be applied to relationships as well when necessary. A good example is the money a star has made on a specific movie.
				Star does not have this info. Movie does not have this info. Studio does not have this info. However the (Star,Movie,Studio) relationship
				can refer to the attribute "Salary"
			4.1.10 Converting Multiway Relationships to Binary
				Introducing a "connecting-relationship" can convert multiway relationships to binary ones.
				Example on p.158
			4.1.11 Subclasses in the E/R Model
				p.159 expresses isa relationships well
		4.2 Design Principles
			4.2.1 Faithfullness
				The design should be faithful to the specifications of the application.
				Entity sets and their attributes should reflect reality.
			4.2.2 Avoiding Redundancy
				See Title
			4.2.3 Simplicity Counts
				Don't introduce unnecessary elements into the design.
			4.2.4 Choosing the Right Relationships
				Choosing too many or the wrong relationships can introduce chances for error or redundancies.
			4.2.5 Picking the Right King of Element
				Similar to the previous, errors coudl be introduced.
		4.3 Constraints in the E/R Model
			4.3.1 Keys in the E/R Model
				...
			4.3.2 Representing Keys in the E/R Model
				Underline the Key Attributes
			4.3.3 Referential Integrity
				Given relationships these are a way of asserting that the connection has to be made. For example in a one-to-one relationship
				the full connection MUST exist.
				p.172 has an example of the notation
			4.3.4 Degree Cosntraints
				Easily visible in the example. p.173
		4.4 Weak Entity Sets
			4.4.0 Definition
				A weak entity set is an entity set such that some or all of it's attributes are a part of another entity set.
			4.4.1 Causes of Weak Entity Sets
				Weak entity sets need to be introduced when multiple Entity Sets determine it. (Key Based)
				Or there is a 'belongs to' kind of relationship such as species and genus where names may be shared.
			4.4.2 Requirements for Weak Entity Sets
				A key for a Weak Entity Sets Has...
					1. Zero or More of its own Attributes
					2. Key attributes from entity sets that are reached by certain many-one relationships to other entity sets.
				Best illustrated on p.176
			4.4.3 Weak Entity Set Notation
				1. If an entity set is weak it will be shown with a double rectangle border.
				2. Its supporting many-one relationships will be shown as diamonds with a double border.
				3. If an entity set supplies any attributes for its own key, then those attributes will be underlined
				Once again, Best Illustrated on p.176
		4.5 From E/R Diagrams to Relational Designs
			4.5.0 Introduction
				Simple Process..
					1. Turn each entity into a relation with same set of attributes.
					2. Turn each relationship into a relation with connecting keys
				But there are special cases...
					1. Weak entity sets cannot be translated straightforwardly.
					2. "Isa" relationships and subclasses require careful treatment.
					3. Sometimes, we do well to combine two relations especially the relation for an entity set E and 
					the relation that comes from many-one relationships from E to some other entity sets.
			4.5.1 From Entity Sets to Relations
				Straight Forward
			4.5.2 From E/R Relationships to Relations
				Also Straight Forward, Pay Attention through to Semantics of Roles and Multiplicity for Hints
			4.5.3 Combining Relations
				Suppose with of Entity set E which relates to many R, which relates to F
				We can combine them into the schema...
					1. All Attributes of E
					2. The Key Attributes of F
					3. Any Attributes Belongs to relationship R
			4.5.4 Handling Weak Entity Sets
				1. Relation for Weak Entity Set W must include not only the attributes of W but also the key attributes of supporting entity sets.
				2. If W shows up in the relation for a relationship it must use all of the key attributes of W
				3. A supporting relationship R from the weak set W to a supporting entity set need not be converted to a relation at all.
		4.6 Converting Subclass Structures to Relations
			4.6.0 Introduction
				isa-heiarchy assumptions...
					1. There is a root entity set for the heiarchy
					2. This entity set has a key that serves to identify every entity represented by the heiarchy.
					3. A given entity may have the components that belong to the entity sets of any subtree of the heiarchy, as long as that subtree includes the root.
				Principle Conversion Strategy...
					1. Follow the E/R Viewpoint: For each entity set in E in the heiarchy, create a relation that includes key attributes from root and any attributes belonging to E.
					2. Treat entities as objects belonging to a single class. For each possible subtree that includes the root, create a relation whose schema uses all the attributes of all the entity sets in the subtree.
					3. Use null values: Create one relation with all the attributes of all the entity sets in the heiarchy. Each entity is represented by one tuple, and that tuples has null values for whatever attributes the entity does not have.
			4.6.1 E/R-Style Conversion
				Straightforward, p.188 demonstrates.
			4.6.2 An Object Oriented Approach
				A kind of brute force method where each possible subtree is considered as a relation.
			4.6.3 Using NULL Values to Combine Relations
				By allowing null values one relation can exist with every possible attribute. Unused attributes are marked as NULL in an entry.
			4.6.4 Comparison of Approaches
				p.191 lists pros and cons of each approach. They are for the most part intuitive.
		4.7 Unified Modeling Language
			4.7.1 UML Classes
				UML Class <-> Entity Set
			4.7.2 Keys for UML Classes
				Keys in UML Classes are followed by PK
			4.7.3 Associations
				Association <-> Relationships/Roles
			4.7.4 Self-Associations
				Associations can be Recursive on Objects
			4.7.5 Association Classes
				This refers to UML Classes which serve as a connecting instance betweem two UML Classes
			4.7.6 Subclasses in UML
				Derived Subclasses Point to Superclasses through an arrow.
			4.7.7 Aggregations and Compositions
				White Diamond <-> Aggregation <-> Many to One with existance assertion
				Black Diamond <-> Composition <-> One to One  with existance assertion
		4.8 From UML Diagrams to Relations
			4.8.1 UML-to-Relations Basics
				...
			4.8.2 From UML Subclasses to Relations
				...
			4.8.3 From Aggregations and Compositions to Relations
				...
			4.8.4 The UML Analong of Weak Entity Sets
				Example p.204
		4.9 Object Definition Language
			4.9.1 Class Declarations
				class <name> {
					<list of properties>
				};
			4.9.2 Attributes in ODL
				class Movie{
					attribute string title;
					attribute integer year;
					attribute integer length;
					aatribute enum Genres{drama, comedy, sciFi, teen} genre;
				};
				
				enum Genres could be accessed in the future as a type Movie::Genres
			4.9.3 Relationships in ODL
				These are represented as attributes. ie: relationship Set<star> stars;
			4.9.4 Inverse Relationships
				Handled using scoping ie... 
					relationship Set<Star> stars 
						inverse Star::starredIn
			4.9.5 Multiplicity of Relationships
				Many is handled with Set
				One is handled with an instance of the class.
			4.9.6 Types in ODL
				Primitive Types
				Class Names
				Set
				Bag
				List
				Array
				Dictionary
				Structures: Struct N {T1 F1, ... , Tn Fn}
			4.9.7 Subclasses in ODL
				class Cartoon extends Movie {
					relationship Set<Star> voices;
				};
			4.9.8 Declaring Keys in ODL
				class Movie (key (title,year)) {
					...
				}
		4.10 From ODL Designs to Relational Designs
			4.10.0 Introduction
				ODL Violates to Relational Model EVERYWHERE, so ... fun....
			4.10.1 From ODL Classes to Relations
				...
			4.10.2 Complex Attributes in Classes
				...
			4.10.3 Representing Set-Values Attributes
				...
			4.10.4 Representing Other Type Constructors
				...
			4.10.5 Representing ODL Relationships
				...
Chapter 7: Constraints and Triggers
	7.0 Introduction
		Active Elements: An expressions or statement we expect to execute at appropriate times.
	7.1 Keys and Foreign Keys
		7.1.1 Declaring Foreign-Key Constraints
			A foreign-key contraint says that if an element appears in the current relation, then it must be in the primary-key section of another relation.
			When we state that an attribute/set of attributes to be a foreign-key referencing some attribute(s) of a second relation we are implying the following...
				1. The referenced attribute must be declared UNIQUE or PRIMARY KEY
				2. If the foreign-key is to be used in R1 then it must exist in R2
			There are two ways of declaring a foreign key...
				1. <LOCAL_ATTRIBUTE_NAME> REFERENCES <EXTERNAL_TABLE>(<EXTERNAL_ATTRIBUTE>)
				2. FOREIGN KEY (<LOCAL_ATTRIBUTES>) REFERENCES <EXTERNAL_TABLE>(<EXTERNAL_ATTRIBUTES>)
		7.1.2 Maintaining Referential Integrity
			When the referential integrity is violated SQL provides us 3 policies we can use...
				1. The Default Policy: Reject Violating Modifications
				2. The Cascade Policy:  If the primary key is change then mimic the changes.
				3. The Set-Null Policy: If the primary key is modified then set foreign keys to null.
			Policies can be set like so...
				ON DELETE SET NULL
				ON DELETE CASCADE
				ON UPDATE SET NULL
				ON UPDATE CASCADE
		7.1.3 Deferred Checking of Constraints
			Ocassionally there may be a circular dependance implied by foreign keys. 
			When this occurs multiple inserts would have to be made in order to make a truly new entry.
			This can be done by setting a key to be...
				1. DEFERRABLE INITIALLY DEFERRED
				2. DEFERRABLE INITIALLY IMMEDIATE
			The former will wait until a transaction is complete to check any constraints.
			The latter will check the constraint after every statement.
	7.2 Constraints on Attributes and Tuples
		7.2.0 Introduction
			In a CREATE TABLE statement we can declare two kinds of cosntraints.
				1. A constraint on a single attribute
				2. A constraint on a tuple as a whole
		7.2.1 Not-Null Constraints
			ie: presC# INT REFERENCES MovieExec(cert#) NOT NULL
			Simply, the attribute cannot be null
		7.2.2 Attribute-Based CHECK Constraints
			A CHECK constraint is some boolean condition that an attribute must follow.
			This can apply to attributes of a tuple, or tuples of a table depending on where it is declared.
			What follows CHECK can be anything that follows a WHERE statement.
	7.3 Modification of Constraints
		7.3.1 Giving Names to Constraints
			CONSTRAINT <Name> <Constraint>
			ie: name CHAR(30) CONSTRAINT NameIsKey PRIMARY KEY
		7.3.2 Altering Constraints on Tables
			SET CONSTRAINT <ConstraintName> <CONSTRAINT>
			ALTER TABLE <TableName> MODIFY <Attribute> <CONSTRAINT>
			ALTER TABLE <TableName> DROP CONSTRAINT <ConstraintName> 
			ALTER TABLE <TableName> ADD  CONSTRAINT <ConstraintName> <CONSTRAINT>
	7.4 Assertions
		7.4.1 Creation Assertions
			An assertion is a boolean-values SQL expression that must be true at all times
			A trigger is a series of actions that are associated with certain events such as insertions into a particular relation and are performed whenever such events arises.
			
			CREATE ASSERTION <assertion-name> CHECK (<Condition>)
		7.4.2 Using Assertions
			As an example suppose a president of a movie studio must have atleast $10,000,000 in net worth..
			CREATE ASSERTION RichPres CHECK (
				NOT EXISTS(
						SELECT Studio.name
						FROM Studio, MovieExec
						WHERE presC# = cert# AND netWorth < 10000000
					)
			)
	7.5 Triggers
		7.5.1 Triggers in SQL
			Features...
				1. checking of condition can be performed pre-event or post-event
				2. the condition and action can refer to old and/or new tuples updated in the triggering event
				3. it is possible to define update events that are limited to a particular attribute or set of attributes
				4. The programmer can specify if the trigger occurs once per modified tuple(row-level), or for every tuple changed(statement-level)
			Format...
				CREATE TRIGGER <TriggerName>
				(AFTER | BEFORE | INSTEAD OF) (UPDATE|INSERT|DELETE) OF <Attribute> ON <Table>
				REFERENCING
					OLD ROW AS <AliasedName1>,
					NEW ROW AS <AliasedName2>
				FOR EACH ROW
				WHEN (<Condition>)
					<SQL STATEMENT1>
					...
					<SQL STATEMENTn>
			OF is optional for UPDATE and not allowed on INSERT/DELETE
			WHEN is also optional
Chapter 9: SQL in a Server Environment and Chapter 10: Advanced Topics in Relational Databases
	Restrict these to Ruby's Lectures