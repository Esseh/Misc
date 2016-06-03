pages 699-788 Appendix A - Assemblers, Linkers, and the SPIM Simulator
	A.1 Introduction- p.699-709
			machine language-
				binary representation for computer communication
			assembler-
				a program that translates symbolic versions of instructions into binary versions.
			macro-
				pattern match and replacement for often used instruction set.
			unresolved reference-
				a reference that requires more information from an outside source to be completed.
			linker/link editor-
				Systems program that combines independant machine language programs and resolves the labels producing one executable.
			LINKER MODEL-
				[source file]->[Assembler]->[Object File]\
														  \
				[source file]->[Assembler]->[Object File]-->Linker-------------> Executable File
														  /    /|\
				[source file]->[Assembler]->[Object File]/   [program library]
			assembler directive-
				an operation that tells the assembler how to translate a program but does not produce machine instructions. Always begins with a period.
				ie:
					.data
					.globl
			source language-
				the high level language that a program is originally written in before being translated.
			compilation model-
												   /----------\
				[program]->(high level)->[Compiler]\           \--->[Linker]----> Computer
				   |------>(assembly)----->-------->-[Assembler]--->[      ]
			reasons to use assembly language-
				space or speed is absolutely critical or certain hardware aspects need to be exploited.
				another reasons is that certain computers may not have a compiler,
				in those computers assembly language is the only choice.
			embedded computers-
				small computers placed in machines that are usually space/speed critical.
			reasons not to use assembly language-
				they are typically tied to a specific architecture and thus must be rewritten when being moved around.
				assembly programs are typically a lot longer as well which harms productivity. (regardless of language programmers tend to about the same lines of code per day.)
			Some compilers can produce machine language directly...
				These compilers must perform the job of the assembler in resolving addresses and encoding instructions.
			Some embedded computers use high level languages...
				this is because it is easier to verify their correctness. In this aspect when reliability is important
				high level languages should be used especially as applications get very complex.
	A.2 Assemblers- p. 709-718
		Translation by the assembler has two major steps-
			1. 
				find memory locations with labels so that the relationship between 
				symbolic labels and addresses are known when instructions are translated.
			2. 
				translate each assembly statement by combining numeric equivalents of opcodes, register specifics, and labels into a legal instruction.
		"Object File"-
			the output of the assembler
		"External Label"/"Global Label"-
			label referring to an object that can be referenced in other files where it's not defined.
		"Local Label"-
			label referring to an object that can only be reference within where it's defined.
			The label action in assembly languages can be seen as a Local Label as it's only known to the file where it is defined.
		"Forward Reference"-
			A label that is used before it is defined.
			A result of this is that assemblers must find all labels before producing instructions.
		An example assembly with parsing...
			ble $t0, 100, loop
			These are broken into the following lexemes...
				ble  (opcode)
				$t0  (register specifier)
				, 	 (comma)
				100  (number literal)
				,	 (comma) 
				loop (symbol)
			the loop symbol is placed in the symbol table, it's address can be determined later.
			Next a second pass is formed and the machine code instructions are formed with the addresses now known.
		"Symbol Table"-
			A table that matches names of labels to the address of memory that the instructions occupy.
		"Backpatching"-
			a method for translating assembly to machine instructions in one pass by holding the entire
			program in the symbol table. This way when the address is resolved the instruction is already ready.
			However as the entire program needs to be held in memory this limits the size of assembly programs that can be made.
		Object Files Hold six distinct sections-
			1. 
				Object File Header: describes size and position of the other pieces of the file.
			2. 
				text segment: contains the machine language code for routines, the routines may not be executable because of unresolved references.
			3. 
				data semgnet: a binary representation of the data in the source file, may be incomplete due to unresolved references.
			4. 
				relocation information: identifies instruction and data that depends on absolute addresses (a variables actual location in memory)
			5. 
				symbol table: associates addresses with external labels and lists unresolved references.
			6. 
				debugging information: caontains concise information of how it was compiled
		Assemblers assume each file starts at the same address (such as location 0) with the expectation that the linker will relocate the code/data
		when they are assigned locations in memory. This is the purpose of the relocation information.
		
		Assembler String Directive-
			.asciiz "these words are convertedf without needing to know the numeric representations, yay for assembler convienence!"
	A.3 Linkers- p. 718-720
		Separate Compilation-
			splitting a program across many files each of which can be compiled without knowledge 
			of what is in the other files.
			The tool that merges these is the "linker"
		The linker at this point...
			Will be able to resolve the references between files..
			One file sees an unresolves symbol and places it in the symbol table,
			in another file it sees the symbol being defined so it is able to associate an address and it is no longer unresolved.
	A.4 Loading- p. 720-721
		The operating systems follows these steps to start a program-
			1.
				Reads the executable's header to determine size and data segments
			2.
				creates new address space for the program, enough to hold text/data segments and an additional stack segment.
			3.
				copies instructions from the file into the new address space.
			4.
				copies arguments passed to the program onto the stack.
			5.
				initializes machine registers, most registers are cleared stack pointer is assigned to the position of first free stack location.
			6.
				jumps to a start up routine that copies program arguments from stack to registers and calls the main routine.
				if the main 'returns' the start up routine terminates with an exit call.
	A.5 Memory Usage- p. 721-724
		MIPS MEMORY LAYOUT-
			[STACK SEGMENT]--				  STARTS AT 7FFFFFFF.hex
			[DYNAMIC DATA ]-- Data Segment
			[STATIC DATA  ]-- Data Segment -- STARTS AT 10000000.hex
			[TEXT SEGMENT ]
			[RESERVED-TEXT]-- STARTS AT 400000.hex
		Text Segment-
			holds program instructions
		Data Segment-
			Static Data-
				size known at compile time, lifetime is the program
			Dynamic Data-
				size known only at runtime and may change, allocated by need and builds upward.
		$gp-
			For static data this is a global pointer that refers to satic data location: 10008000.hex
			this makes it easier to access variables in the range 10000000.hex to 10010000.hex
			global variables are usually stored in this area.
		Stack Segment-
			holds procedure call frames
			the size is only known as runtime and can change.
			as it is added to the relative address goes down unlike dynamic memory which goes upward.
	A.6 Procedure Call Convention- p.721-735
		"Procedure Call Convention"/"Register Use Convention"-
			A software protocal governing the use of registers by procedures.
		MIPS Compiler Register Use-
			MIPS CPU contains 32 general-purpose registers numbers 0-31, 0 contains the hardwired value 0.
			Registers $at(1),$k0(26),and $k1(27)...
				are reserved for the assembler and operating system and should not be used by programs or compilers
			Registers $a0-$a3 (4-7)...
				are used to pass the first four arguments to routines (remaining arguments passed to stack)
			Registers $v0 and $v1 (2,3)...
				are used to return values from functions
			Registers $t0-$t9...
				are "caller-saved registers" that hold temporary values that need not be preserved across calls
			Registers $s0-$s9...
				are "callee-saved registers" that hold long-lived values that should be preserved across calls.
			Register $gp...
				points to the middle of a 64K block of memory in the static data segment.
			Register $sp...
				is the stack pointer which points to the last location in the stack
			Register $fp...
				is the frame pointer, when calling a procedure points to the end of the block associated with the stack frame.
			Register $ra...
				the jal instruction writes to this register, it is the return address from a procedure call.
		Register naming convention-
			zero: constant 0
			at: reserved from assembler
			v: expression evaluation/result
			a: argument
			t: temporary
			s: saved temporary
			k: reserved for kernal
			gp: global pointer
			sp: stack pointer
			fp: frame pointer
			ra: return address
		"Procedure Call Frame"-
			block of memory holding values passed to procedure as arguments, 
			saving registers that may be modified so they can be restored,
			and provide space for local values
		Building The Stack Frame-
			1. Pass Arguments (first 4 in $a0-$a3 registers, remaining onto the stack)
			2. Save caller-saved registers
			3. Execute a jal instruction (saves the return address in $ra then jump to calee's first instruction.)
			4. subtract frame's size from stack pointer (explicit)
			5. save calee-saved registers (if the calee makes a call then $ra need to be saved)
			6. Establish frame pointer by adding stack's frame size minus 4 to $sp and storing the sum in $fp.
		Tearing Down the Stack Frame-
			Just work in reverse.
	A.7 Exceptions and Interrupts- p.735-740
		ALREADY COVERED IN 117
	A.8 Input and Output- p.740-742
		IGNORING BECAUSE ZERO RELEVANCE
	A.9 SPIM- p.742-747
		IGNORING BECAUSE ZERO RELEVANCE
	A.10 MIPS R2000 Assembly Language p.747-788
		Addressing Modes for Load/Store Instructions-
			format 		:	Address computation
			
			(register)  : contents of register
			imm			: immediate
			imm (register) : immediate + contents of register
			label 			: address of label
			label +/- imm   : address of label + or - immediate
			label +/- imm (register) : address of label + or - (immediate + contents of register)
		Assembler Syntax-
			label:
			_identifier
			.alsoandidentifier
			123 (base 10)
			0x123 (hex)
			"this is a string"
			.directive_name
		Encoding MIPS Instructions-	
			R-Type-
				31-26[op] 25-21[reg s] 20-16[reg t] 15-11[reg d] 10-6[shift amount] 5-0[function]
			I-Type-
				31-26[op] 25-21[reg s] 20-15[reg t] 15-0[immediate]
			J-Type-
				31-26[op] 25-0[target]
		MIPS Instructions- 
			Addition-
				add rd, rs, rt
				[0][rs][rt][rd][0][0x20/0x21]
			Addition Immediate-
				(overflow)
				addi rt, rs, imm
				[8][rs][rt][imm]
				
				(without overflow)
				addiu rt, rs, imm
				[9][rs][rt][imm]
			And-
				and rd, rs, rt
				[0][rs][rt][rd][0x24]
			And Immediate-
				andi rt,rs,imm
				[0xC][rs][rt][imm]
			Count Leading Ones-
				clo rd, rs
				[0x1C][rs][0][rd][0][0x21]
			Count Leading Zeroes-
				clz rd, rs
				[0x1C][rs][0][rd][0][0x20]
			Divide-
				(overflow)
				div rs,rt
				[0][rs][rt][0][0x1A]
				(no overflow)
				divu rs, rt
				[0][rs][rt][0][0x1B]
			Multiply-
				mult rs,rt
				[0][rs][rt][0][0x18]
			Unsigned Multiply-
				multu rs,rt
				[0][rs][rt][0][0x19]
			Multiply(without overflow)-
				mul rd, rs, rt
				[0x1C][rs][rt][rd][0][2]
			Multiply Add-
				madd rs , rt
				[0x1C][rs][rt][0][0]
			Unsigned Multiply Add-
				maddu rs, rt
				[0x1C][rs][rt][0][1]
			Multply Subtract-
				msub rs,rt
				[0x1C][rs][rt][0][4]
			Unsigned Multiply Subtract-
				[0x1C][rs][rt][0][5]
			NOR-
				nor rd, rs, rt
				[0][rs][rt][rd][0][0x27]
			OR-
				or rd, rs, rt 
				[0][rs][rt][rd][0][0x25]
			OR Immediate-
				ori rt,rs imm
				[0xD][rs][rt][imm]
			SLL-
				sll rd, rt, shamt
				[0][rs][rt][rd][shamt][0]
			SLL Variable-
				sllv rd, rt, rs
				[0][rs][rt][rd][0][4]
			SR Arithmatic-
				sra rd, rt, shamt
				[0][rs][rt][rd][shamt][3]
			SRAV ARtihmatic Variable-
				srav rd, rt, rs
				[0][rs][rt][rd][0][7]
			SRL-
				srl rd, rt, shamt
				[0][rs][rt][rd][shmt][2]
			SRL Variable-
				srlv rd, rt, rs 
				[0][rs][rt][rd][0][6]
			sub-
				sub rd, rs, rt
				[0][rs][rt][rd][0x22]
			subu-
				subu rd, rs, rt
				[0][rs][rt][rd][0x23]
			xor-
				xor rd, rs, rt
				[0][rs][rt][rd][0][0x26]
			xori-
				xor rt, rs, imm
				[0xE][rt][rs][imm]
			load upper immediate-
				lui rt, imm
				[0xF][0][rt][imm]
			set less than-
				slt rd, rs, rt
				[0][rs][rt][rd][0][0x2A]
			set less than unsigned-
				sltu rd, rs, rt
				[0][rs][rt][rd][0][0x2B]
			set less than immediate-
				slti rt, rs, imm
				[0xA][rs][rt][imm]
			set less than unisgned immediate
				sltiu rt, rs, imm
				[0xB][rs][rt][imm]
			jump 
				j target
				[2][target]
			jump and link
				jal target
				[3][target]
			jump and linked register
				jalr rs, rd
				[0][rs][0][rd][0][9]
			jump register-
				jr 
				[0][rs][0][9]
			load byte-
				lb rt, address
				[0x20][rs][rt][offset]
			load unsigned byte-
				lbu rt, address
				[0x24][rs][rt][offset]
			load halfword-
				lh rt, address
				[0x21][rs][rt][offset]
			load unsigned halfword-
				lhu rt, address
				[0x25][rs][rt][offset]
			load word
				lw rt, address
				[0x23][rs][rs][offset]
			store byte-
				sb rt, address
				[0x28][rs][rt][offset]
			store halfword-
				sh rt, address 
				[0x29][rs][rt][offset]
			store word-
				sw rt, address
				[0x2B][rs][rt][offset]
			FLOATING POINTS ON 774		
pages 788-884 Appendix B - The Basics of Logic Design 
	B.1		Introduction p. 789 - 791
		Nothing to See Here
	B.2		Gates, Truth Tables, Logic Equations p. 791-797
		"asserted signal"-
			logically true or 1
		"deserted signal"-
			logically false or 0
		"combinational logic"-
			given the same input computes the same output
			based on some combination of logic.
		"sequential logic"-
			a group of elements that contain memory, thus a 
			combination of logic may produce different results
			based off of what is already present.
		"truth tables"-
			a representation of a combinational system 
			where every combination of I/O signals are explored
			and represented in a table with variable names, 0/1
		Boolean Algebra-
			Mathematics Related to asserted/deserted signals.
		Boolean Laws-
			Identity Law:			A + 0 = A, A * 1  = A
			Zero and One Laws:		A + 1 = 1, A * 0  = 0
			Inverse Laws:     		A + 1 = 1, A * -A = 0
			Communitive Laws:		A + B =  B + A , A * B = B * A
			Associative Laws:		A + (B + C) = (A + B) + C , A * (B * C) = (A * B) * C
			Dstributive Laws:		A * (B + C) = (A*B)+(A*C) , A + (B * C) = (A+B)*(A+C)
			DeMorgan's Laws: 		-(A*B) = -A + -B , -(A+B) = -A * -B
		"logic gates"-
			structures that physically represent boolean functions 
	B.3		Combinational Logic p. 797-809
		Decoders-
			N-bit decoders, takes in N inputs and sends out 2^n outputs, only one of which are true.
		Multiplexors-
			NxM MUX, takes in N inputs and a control signal, outputs M values
		Two-Level Logic-
			Can be represented with a 'map' with only one additional operation.
			ie: (a+b) * (c + d) * (e + f)
			This is 'sum of product form'
			alternatively there is 'product of sum form'
			which would just have the ands/ors swapped.
		PLA's-
			Physical implementations of Two-Level Logics
		ROMs(read only memories)-
			A memory whose contents are designated at creation time 
			after which the contents can only be read.
		programmable ROM-
			A form of read-only memory that can be programmed when a designer knows it's contents.
		In roms...
			The number of addressable entries in the ROM determines that number of address lines.
			if a ROM contains 2*m addressable entries (also called the height)
			then there are m input lines. the number of bits in each addressable spot is also called the width.
			The total amount of space in the ROM is the height * the width otherwise known as the 'shape'
			A ROM instead of containing the ability to gain different results based on circumstance (different inputs)
			simply has all the outputs decoded already.
		Don't Cares-
			Situations where we don't care what some inputs/outputs are, (theyre not relevant to the functionality of the system.)
			Finding these situations is useful in optimization.
		"Bus"-
			An array of signals treated symbolically as one whole.
			(think of multi-bit input)			
	B.4		Using a Hardware Description Language p.809-816
		DON'T CARE
	B.5		Constructing a Basic ALU p.816-829
		Already Know... HOWEVER
		Symbol for ALU
		
		   |\
		   | \
		a->|  \
		   |   |->ZERO
		   |ALU|->RESULT
		b->|   |->OF
		   |  /
		   | / |
		   |/ \./
			   .
			  cout
	B.6		Faster Addition: Carry Lookahead p. 816-839
		Carry Out Formula "infinite hardware"-
			(a*b)+(cin*(a xor b))
	B.7		Clocks p.839-843
		"edge-triggered clocking"-
			A clocking scheme in which all state changes occur on a clock edge.
			When the clock is at its 'top' or 'bottom' a state change can occur.
		"clock"-
			A free-running signal with a fixed cycle time.
			This time is referred to as the 'clock time'
		"clock frequency"-
			inverse of clock time
		"clocking methodology"-
			the approach used to determine when data is valid and stable relative to the clock
		"state element"-
			also known as 'memory element'
		"synchronous system"-
			a memory system that employs clocks and where data signals are read only when the clock
			indicates that the signal values are stable.
			in this systems signals that are written into state elements 'must be valid'
			combinatorial circuits do not have feedback so if they continue to run with the same input they will eventually become valid.
		CLOCK CYCLE vs ACTIONS
		     ___________
			|comb. logic|
		 ___|           |___
		 state			  state
		element 1       element 2
		"register file"-
			a state element that consists of a set of registers that can be read and written by supplying a register number to be accessed.
	B.8		Memory Elements: Flip-Flops, Latches, Registers p. 843-851
		Memory Elements	
			"logic blocks"-
				contain state and are sequential
			NOR Latch-
					 ___
				R---|   |
					|NOR|---*----Q
				 ---|___|  /
				 \-------\/
						  *
				  -------/\
				 /	 ___   \
				 ---|   |   \
					|NOR|----*---Q
				S---|___|	
					These can oscillate possibly.
					And have incorrect behavior.
			"Flip-Flops"-
				a memory element for which the output is equal to the value of the stored state inside
				the element and for which the internal state is changed only on a clock edge.
			"Latch"-
				a memory element in which the output is equal to the value of the stored state inside 
				the element and the state is changed whenever the appropriate unputs change and the 
				clock is asserted.
			"D Flip-Flop"/"D Latch"-
				a flip flop with one data input that stores the value of that input signal in the internal 
				memory when the the clock edge occurs.
			"D Latch" Implementation-
			 C*---->[AND]---->[NOR LATCH]---> Q
			  |	 (-)[   ]     [         ]
			  ---/--[AND]---->[         ]--->-Q
			 D--*-->[   ]
					Where C is the clock input
					D replaces Q if C is on.
			"D Flip-Flop" Implementation- (falling-edge trigger)
				D---->[D	D	Q]--------->[D   D       Q]-------> Q
				   .->[C	Latch]		 .->[C   Latch  -Q]------->-Q
				   |					 |
				C--*--(-)----------------.
				
				When the clock rises (C is true), the value is stored in the first latch.
				When the clock falls (C is false), the value in the latch is then stored in the second latch.
				Moving the location of the (not) would change it into a rising-edge trigger.
			"Setup Time"-
				The minimum time that the input to a memory device must be valid before the clock edge.
			"Hold Time"-
				The minimum time that the input must be valid after the clock edge.
			Using an array of D Flip-Flops we can store multi-bit data.
		Register Files-
			"Register File"-
				a set of registers that can be read and written to by supplying a register number to access it.
				A register file can be implemented with a decoder for each read/write port and an array of registers
				built from D Flip-Flops
			
				A register store needs 3 inputs-
					1. Register Number
					2. data to write
					3. clock controlling writing.
				Reading can be implemented with a pair of multiplexors.
		p.848,849 for implementation.
	B.9		Memory Elements: SRAMs and DRAMs p. 851-860
		"SRAM"-
			Static Random Access Memory
			Memory where data is stored statically (flip-flops)
			SRAMS are faster than DRAMS but less dense and more expensive per bit.
			
			Usually integrated circuits with memory arrays and a single access port for either Read / Write
			A 4M x 8 (8 btis wide and 4M entries) will have 2^22(4M) address lines and an 8 bit single input line.
			
			Diagram on p.851,854,855
		"DRAM"-
			Stores the signals in capacitors, can hold for extended periods so long as it gets refreshed.
			More dense but cheaper than SRAM.
			
			Diagram on p.856,857
		ERROR DETECTION-
			Will do if it's on test.	
	B.10	Finite-State Machines p. 860-866
		"Finite-State Machine"-
			A sequential logic function consisting of a set of inputs/outputs
			a next-state function that maps the current state and the inputs to a new state.
			The new state being an output function that maps the current state and possibly the
			inputs to a set of asserted outputs.
		"Next State Function"-
			A combinational function that given the inputs and current state, produces 
			the next state of a finite-state machine.
		These can be represented as state-diagrams, alternatively they can be actually realized as structures
		such as our 'system clock'
	B.11	Timing Methodologies p.866-872
		"Clock Skew"-
			The difference in absolute time between the times when two state elements
			see a clock edge.
		"Level-Sensitive Clocking"-
			A timing methodology in which state changes occur at neither high or low clock levels
			but are not instantaneous
		"Metastability"-
			A situation that occurs if a signal is samples when it is not stable for the requires setup/hold times.
			Indeterminate form between high and low.
		"Synchronizer Failure"-
			Flip flop in metastable state causes some logic blocks to see a 0 and others a 1.
	B.12	Field Programmable Devices p.872-884
		"Field Programming Device (FPD)"-
			An integrated circuit containing combinational logic and possibly memory devices
			that are configurable by the end user.
		"Programmable Logic Device (PLD)"-
			An integrated circuit containing combinational logic whose function is configured by
			the end user.
		"Field Programming Gate Array (FPGA)"-
			A configurable integrated circuit containing both combinational logic blocks and flip-flops.
		"Simple Programmable Logic Device (SPLD)"-
			Programmable Logic Device, usually containing either a single PAL or PLA
		"Programmable Array Logic"-
			Contains a programmable and-plane followed by a fixed or-plane.
		"Antifuse"-
			A structure in an integrated circuit that when programmed makes a permanent
			connection between two wires.
		"Lookup Tables (LUTs)"-
			In a field of programmable device the name given to cells because they consist of a small amount of logic and RAM.
pages 33-110  Chapter 1 - Computer Abstractions and Technology
	1.1 Introduction - p.33 - 42
		Classes Of Computing Applications and their Characteristics-
			Personal Computer(PC)-
				A computer designed for use by an individual , usually incorporating a graphics display,
				a keyboard, and a mouse.
			Servers-
				A computer used for running larger programs for multiple users, often simultaniously, 
				and typically accessed only via a network.
			Supercomputer-
				A class of computers with the highest performance and cost; they are configured as
				servers and typically costs tens to hundreds of millions of dollars.
			Embedded Computer-
				A computer inside another device used for running one predetermined application or 
				collection of software.
			Personal Mobile Device(PMD)-
					Small Wireless Devices to connect to the internet; they rely on batteries for power,
					and software is installed by downloading aps. Conventional examples are smart phones
					and tablets.
		"Terabyte"-
			Originally 2^40 bytes , this quanitity is now a "Tebibyte (TiB)"
			TB is 10^12 bytes
		Cloud Computing-
			Large collections of servers that provide services over the Internet; some 
			providers rent dynamically varying number of servers as a utility.
		Software as a Service (SaaS)-
			delivering software/data over the internet as a service.
			(websearch/social networking)
		"Multicore Microprocessor"-
			A microprocessor unit containing multiple processors(cores) in a single integrated circuit.
	1.2 Eight Great Ideas in Computer Architecture - p.42-46
			Moore's Law-
				The tendency for integrated resources to double every 18-24 months.
			Abstraction-
				Hiding the small details to increase productivity.
			Common Fast Case-
				Speeding up common problems will yield greater overall performance increase.
			Parallelism-
				Performing actions simultaniously to increase performance.
			Pipelining-
				successive operations handled by successive modules working concurrently
			Prediction-
				Guess and start working instead of waiting until you know for sure.
			Heiarchy of Memories-
				The collections of memory and abuse of the system to get the best of both worlds.(storage AND speed)
			Dependability via Redundancy-
				Being able to have rudundant parts that can help correct the program when things go awry.
	1.3 Below Your Program - p.46-52
		"Systems Software"-
			Software that provides services that are commonly useful, including operating
			systems, compilers, loaders, and assemblers.
		Hardware/Software Heiarchial Layers-
			(applications (SYSTEMS (Hardware) SOFTWARE) software)
		"operating system"-
			Supervising program that manages the resources on a computer for the benefit of the 
			programs that run on the computer.
		"compiler"-
			A program that translates high-level language into assembly language statements or machine code.
		"binary digit"-
			base 2 numbering
		"instruction"-
			a command the computer hardware understands and obeys.
		"assembler"-
			a program that translates symbolic statements into binary
		"assembly language"-
			symbolic representation of machine instructions
		"machine language"-
			binary representation of machine instructions
		"high level programming language"-
			portable language such as C++ that can...
	1.4 Under the Covers - p.52-65
		unimportant stuff-
			"input device"-
				ie: the mouse and keyboard
			"output device"-
				ie: the screen and speakers
			"liquid crystal display LCD"-
			"active matrix display"-
			"pixel"-
		"integrated circuit"-
			Also called a 'chip'. A device combining dozens to millions of transistors.
		"central processing unit (CPU)"-
			Also called processor. The active part of the computer, which contains the datapath
			and control and which adds numbers, tests numbers, signals I/O devices to activate, and so on.
		"datapath" /"ALU"-
			The component of the processor that performs arithmatic operations.
		"control"-
			The component of the processor that commands the datapath, memory, and I/O devices.
			(Essentially controls the Von Neumann Architecture)
		"memory"-
			The storage area where programs are kept when they are running which contains the data needed by the program.
		"dynamic random access memory (DRAM)"-
			Memory Built as an integrated circuit, it provides random acccess to any location.
		"cache memory"-
			A small, fast memory that acts as a buffer for slower, larger memory.
		"static random access memory (SRAM)"-
			Also memory built as an integrated circuit, but faster and less dense than DRAM.
		"instruction set architecture"-
			An abstract interface between the hardware and the lowest-level software that encompasses everything neccessary to 
			write a machine language program that will run correctly including registers, instructions, memory access, I/O...
		"application binary interface (ABI)"-
			User portion of binary instruction set.
		"implementation"-
			Hardware that obeys the architecture abstraction.
		"volatile memory"-
			memory that only retains data when it has power
		"non-volatile memory"-
			memory that retains data without power
		"main memory"-
			memory to hold programs.. typically DRAM.
		"secondary memory"-
			used to hold data between runs ie: magnetic disks or flash memory
		magnetic disk-
			hard disk
		flash memory-
			inbetween hard disk and DRAM in heiarchy.
		"LAN"-
		"WAN"-
	1.5 Technologies for Building Processors and Memory - p.65-71
		"transistor"-
			on/off switch controlled by signal
	1.6 Performance - p.71-86
		"Response Time"/"Execution Time"-
			The time requires for a computer to complete a task.
		"Thoughput"/"Bandwidth"-
			Number of tasks completed per unit time.
		"CPU Execution Time"-
			Actual time CPU spends computing a specific task.
		"User CPU Time"-
			The CPU time spent in a program itself.
		"System CPU time"-
			The CPU time spent in the OS performing tasks on behalf of the program.
		"Clock Cycle"-
			Time for one block period.
		"Clock Period"-
			Length of a clock cycle
		"Clock Cycles Per Instruction"-
			Average number of clock cycles per instruction for a program or program fragment.
		"instruction count"-
			The number of instructions executed by the program
		"instruction mix"-
			A measure of the dynamic frequency of instructions across one or many programs.
		Equations-
			Performance.x = 1/ Execution_Time.x
			Val1 / Val2 = n, x is n times faster/better than y.
			CPU.exe = CPU.clocks for a program  / clock rate
			CPU.time = IC*CPI/ClockRate
			CPI = sum(CPI.i * C.i) / IC
		Equations(concise)-
			MIPS = ClockRate(MHz)/(CPI*10^6)
			CPI = sum(CPI.i * C.i)/IC
			CPU.time = IC * CPI * ClockCycleTime
	1.7 The Power Wall- p.86-89
		Not Important
	1.8 The Sea Change: The Switch from Uniprocessors to Multiprocessors- p.89-94
		Not Important
	1.9 Real Stuff: Benchmarking the Intel Core i7- p.94-98
		Nothing Important
	1.10 Fallacies and Pitfalls- p.98-102
		Amdahl's Law-
			Execution Time After Improvement = Execution Time Affected by Improvement / Amount of Improvement  + Execution time Unaffected
	1.11 Concluding Remarks- p.102-110
		nothing important
pages 110-241 Chapter 2 - Instructions
	2.1 Introduction- p.112-115
		"instruction set"-
			The vocabulary of commands understood by a given architecture.
		"stored-program concept"-
			The idea that instructions and data of many types can be stored in memory as
			numbers, leading to the stored program computers.
		32 Registers-
			$s0-$s7 - used to pass information that needs to be remembered.
			$t0-$t9 - used to hold temporary values
			$zero - holds constant value 0
			$a0-$a3 - passes first four values to a procedure
			$v0-$v1 - return 'v'alues from functions.
			$gp -- Points 8000.hex above bottom of stack area.
			$fp -- 'Frame Pointer' - Used in conjunction with stack pointer to make an activation frame.
			$sp -- 'Stack Pointer' - Points to the the current top of the stack. (The top is on the bottom)
			$ra -- 'Return Address'
			$at -- Used by assembler to handle large constants.
		2^30 Memory Words-
			Memory[0],Memory[1],Memory[4294967292] -- Accessed in data instructions.
		MIPS Instructions-
			LINE 196 Has more information...
	2.2 Operations of the Computer Hardware- p.115-118
		Not Important, Covvered in the MIPS Appendix Sections. Line 196 onwards...
	2.3 Operands of the Computer Hardware- p.118-126
		"Word"-
			A group of 32 bits.
		"Data Transfer Instruction"/"load instruction"-
			A command that moves data between memory and registers.
		"Address"- 
			A value used to determine the position of a specific elements in a memory array.
			For byte arrays. a[0],a[1],a[2]...
			For word arrays. a[0],a[4],a[8]...
			This spacing is referred to as "alignment restriction"
		Computers divide into two addressing catagories-
			GIVEN SOME VALUE LET'S SAY.. 90AB12CD.hex
			It can be stored one of two different ways for representing an array.
			Big Endian-
				[1000][90]
				[1001][AB]
				[1002][12]
				[1003][CD]
			Little Endian-
				[1000][CD]
				[1001][12]
				[1002][AB]
				[1003][90]
		Breaking Down a MIPS Expresson From C-
		A[12] = h + A[8];
		Assuming, h is in $s2 and base address of the array is in $s3
		lw $t0 , 32($s3)
		add $t0 , $t0 , $s2
		sw $t0, 48($s3)
	2.4 Signed and Unsigned Numbers- p.126-135
		"least significant bit"-
			rightmost bit in MIPS word.
		"most significant bit"-
			leftmost bit in MIPS word.
		EVERYTHING ELSE IS JUST BASE2 / BASE16.. Can ignore.
	2.5 Representing Instructions in the Computer- p.135-144
		Register Instructions-
			[opcode][source1][source2][destination][offset][function_code]
			so for example, add $t0, $s1, $s2
			add's op code is 0 and function code is 32. $t0 is register 8, $s1 is register 17
			thus as a binary representation...
				[0][17][18][8][0][32] in base 10... and then just convert to binary.
		"instruction format"-
			A form of representation of an instruction composed of fields of binary numbers.
		"machine language"-
			binary representation of an instruction
		MIPS FIELD SYMBOLIC REGISTER MEANINGS-
			rs: source 1
			rt: source 2
			rd: result destination
		LINE 196 For more general information about the format..
	2.6 Logical Operations- p.144-148
		Appendix A handles this as well...
	2.7 Instructions for Making Decisions- p.148-156
		Appendix A handles this as well...
	2.8 Supporting Procedures in Computer Hardware- p.156-170
		"procedure"-
			A stored subroutine that performs a specific task based on the parameters with which it is provided.
		Procedure Execution Steps-
			1. Put parameters in place where proc can access them.
			2. Transfer control to proc
			3. acquire storage resources needed for proc
			4. perform the task
			5. put the result value in a place the caller can access it.
			6. return control and undo the collected resources leaving no trace.
		More in Line 142 (covers rest of the section)
	2.9 Communicating with People- p.170-176
		Goes Over ASCII/Strings
	2.10 MIPS Addressing for 32-bit Immediates and Addresses- p.176-186
		lui allows to load a value into the upper 16 bits of a register based on a constant.
		Doing this we can construct 32 bit constants stored in temporary registers.
		Line 196 has information on the different addressing types.
		
		Line Offset-
			Instructions are separated by value of 4.
		Adressing Types-
			1. Immediate Addressing-
				[op][rs][rt][imm]
			2. Register Addressing-
				[op][rs][rt][rd][...][func]
			3. Base Adressing-
				[op][rs][rt][address]
			4. PC-relative addressing-
				[op][rs][rt][address]
			5. Psuedodirect Addressing-
				[op][Address]
	2.11 Parallelism and Instructions: Synchronization- p.186-189
		"Parallel Execution"-
			when two instructions operate in parallel
		"Synchronization"-
			Getting everything working together by making everything consistant.
			One scheme is the lock/unlock mechanism.
		
		"data race"-
			Two memory accesses form a data race if they are from different threads to same location.
			Atleast one is a write and they occur one after another.
	2.12 Translating and Starting a Program- p.189-200
		Covered in appendix, ignore.
	2.13 A C-Sort Example to Put it All Together- p.200-208
		Uneeded Ignore.
	2.14 Array versus Pointers-	p. 208-228
		Cover if On Exam / Park Says So
	...
		...
	2.19 Fallacies and Pitfalls- p.228-241
		...
pages 241-321 Chapter 3 - Artihmetic for Computers
	3.1 Introduction- p.241-244
		Nothing Important.
	3.2 Addition and Subtraction- p.244-251
		Done Normally..
		1000101010101010101010
	   +1010000010101010101010
	   _______________________
	    0010101101010101010100
		
		For subtraction just remember two's complement and that a-b is the same as a+(not(b)+1)
		Overflow Condition-
			If a carry in occurs and a carry out does not occur , overflow may occur.
			If so then if it doesn't match the corresponding sign, overflow occured.			
	3.3 Multiplication- p.251-258
		Unsigned Multiplication-
			Multiplication Algorithm in Longhand-
					1000
					1001
					____
					1000
				   0000  
				  0000  
				 1000   
				 ____   
				 1001000
				 The top is the mutiplicand
				 the bottom is the multiplier.
				Multiplication Algorithm in Structure-
					Page 252
				Multiplication Algorithm in FlowChart-
					Page 253
		Signed Multiplication-
			The Previous Algorithm should still work in binary. 
		Pipelined Multiplication-
			Instead of looping N times we can just use N adders!
			Pipelining like this will make use of parallelism to give very fast results.
		Overflow and Multiplication-
			It is not immediately detected by the hardware, it's the softwares responsibility.
	3.4 Division- p.258-268
		Dividend = Quotient * Divisor + Remainder
		"Dividend"-
			A number being divided.
		"Divisor"-
			A number that is being divided by.
		"quotient"-
			primary result of division
		"remainder"-
			secondary result of division
		Division Algorithm and Hardware-
			Diagram-
				page 260
			Algorithm-
				count = 1
				Start:
				Subtract Divisor register from Remainder Register and place result in Remainder Register
					If Remainder < 0 then... 
						restore original value by adding Divisor Register to Remainder Register and placing the sum in the Remainder Register. 
						Shift Quotient Register to left setting new rightmost to 0.
					Else Shit the Quotient Register to the left setting new rightmost to 1.
				Shift the Divisor Register right 1 bit
				if count < 33 then goto Start
		Signed Division-
			Simple Solution-
				Remember Signs, convert values to positive. Run, then negate the quotient if the signs disagree.
	3.5 Floating Point- p.268-300
		"scientific notation"-
			a notation that renders numbers with a single digit to the left or right of a decimal point.
		"normalize"-
			a number in floating-point notation that has no leading 0s
		"floating point"-
			Computer arithmatic that represents numbers in which the binary point is not fixed.
		"fraction"/"mantissa"-
			The value generally between 0 and 1 placed in the fraction field.
		"exponent"-
			in floating point arithmatic the portion in the exponent field.
		"overflow(floating point)"-
			A situation in which a positive exponent becomes too large to fit in the exponent field.
		"underflow(floating point)"-
			A fraction so small it can't be detected by the precision.
		"double precision"-
			Floating point composed of two 32 bit words (DWORD)
			[s][11 exponent][20 fraction][32 continued fraction]
		"single precision"-
			Floating point composed of a 32 bit word.
			[s][11 exponent][20 fraction]
	3.6 Parallelism and Computer Arithmatic: Subword Parallelism- p.300-302
		Ignore
	3.7 Real Stuff: Streaming SIMD... P.300-304
		Ignore.
	3.8 Going Faster: Subword Parallelism and Matrix Multiply- P.304-308
		Nothing Here Important
	3.9 Fallacies and Pitfalls- P.308-312
		Funny read, but nothing important.
	3.10-3.12 Concluding Remarks- P.308-321
		Ignore.
pages 321-469 Chapter 4 - The Processor
	4.1 Introduction- p.323-328
		For Every Instruction the first two steps are identical-
			1. Send the program counter (PC) to the memory that contains the code and fetch the instruction from that memory.
			2. Read one or two registers, using fields of the instruction to select the registers to read. IE-
				For LW we need to read only one register, but for most instructions we need to read two.
		For Each of the three instruction classes (memory-reference, arithmatic-logical, and branches)... 
			the actions are largely the same independant of the exact instruction...
				1. For example all instruction classes except jump use the ALU for an address calculation, the arithmatic-logical instructions,
				and branches for comparison.
				
				2. After the ALU the instruction classes differ, ie: a memory reference instruction will need to access the memory either to read
				or to write to store it.
				Arithmatic-logical instruction must write information from the ALU or memory back into a register.
				Lastly for a branch instruction we may need to change the next instruction address based on the comparison.
				Otherwise the PC will be incremented by 4 to get the next instruction.
		MIPS SUBSET DIAGRAM-
			p.325
		MIPS SUBSET DETAILED DIAGRAM-
			p.326
	4.2 Logic Design Conventions- p.328-333
		"Clocking Methodology"-
			The approach used to determine when data is valid and stable relative to the clock.
	4.3 Building a Datapath- p.333-343
		"Program Counter(PC)"-
			Register containing the address of the current instruction in the program being executed.
		Basic PC Cycle-
			--->[Instruction Address        ]	          [PC]     ___________
				[                instruction]-----> ...-->[  ]---> |ADDER, +4|--->
				[Instruction Memory         ]	          [  ]     -----------
		IMPORTANT DIAGRAMS-
			pages-
				334-336
				338
				341
		"Register File"-
			A state element that consists of a set of registers that can be read/written to by accessing it via a number.
	4.4 A Simple Implementation Scheme- p.343-357
		ALU CONTROL BITS- p.344
		Instruction Fields- p.346
		Good Diagram- p.348
		Datapath Operation p.349
		Single Cycle Implementation p.353
		Why single cycle isn't used today p.355
	4.5 An Overview of Pipelining- p.357-374
		"Pipelining"-
			An implementation technique in which multiple instructions are overlapped in exeuction(parallel)
			much like an assembly line.
		Single-Cycle vs Pipelined-
			p.358(laundry as example)
			p.359
		Pipelining...
			Does not neccessarily increase speed of exuction, what it increases is throughput.
			So while everything takes the same amount of speed more is able to be processed.
		Under Ideal Situations if instructions are balanced perfectly...
			Time.pipelined = Time.nonpipelined/pipe stages
		"Structural Hazard"-
			When a planned instruction cannot execute in the proper clock cycle because the hardware does not support the 
			combination of instructions set to execute.
		"Pipeline Data Hazard"-
			A slowdown caused by something not being available.
		"Forwarding"/"Bypassing"-
			Resolving data hazard by retrieving the missing data from internal buffers rather than waiting for it.
		"Bubble"/"Pipeline Stall"-
			A stall initiated to resolve a hazard.
		"Load-Use Data Hazard"-
			A specific form of data hazard in which the data being loaded by a load instruction has not yet
			become available when another isntruction needs it.
	4.6 Pipelined Datapath and Control- p.374-390
		INSTRUCTION EXECUTION-
			1. IF: Instruction Fetch
			2. ID: Instruction Decode and Register File Read
			3. EX: Execution or address calculation
			4. MEM: Data memory access
			5. WB: Write Back
		(Early Diagrams are Helpful but the Pipelined aren't)
	4.7 Data Hazards: Forwarding versus Stalling- p.390-415
		Still refers to pipelining, can be skipped.
	4.8 ... Lost?
		????
	4.9 Exceptions- p.415-423
		"Exception"/"Interrupt"-
			Unscheduled event that disrupts program execuction,
			used to detect overflow.
		"Interrupt"-
			An execution coming from outside the processor.
		"Vectored Interrupt"-
			An interrupt for which the address to which control is transferred is determined by the cause of the exception.
	4.10 Parallelism via Instructions- p.423-441
		All about pipelining, don't need it. 
	4.11 Real Stuff: The ARM Cortext-A8 and Intel Core i7 Pipelines- p.441-449
		...
	4.12 Going Faster: Instruction-Level parallelism and Matrix Multiply- p.449-454
		...
	4.14 Fallacies and Pitfalls- p.454-469
		...
pages 966-1002 Appendix D - Mapping Control to Hardware
	D.1 Introduction- p.968-969
		...
	D.2 Implementing Combinational Control Units- p.969-975
		...
	D.3 Implementing Finite-State Machine Control- p.975-988
		Finite-State Machine- p.975
	D.4 Implementing the NextState Function with a Sequencer- p.988-995
		...
	D.5 Translating a Microprogram to Hardware- p.995-1002
		...
pages 469-611 Chapter 5 - Large and Fast: Exploiting Memory Heiarchy
	5.1 Introduction p.469-477
		"The Principle of Locality"-
			Programs access a relatively small amount of their address space at any given time.
		"Temporal Locality"-
			If a data location is referenced it will likely be referenced again soon.
		"Spatial Locality"-
			If a data location is referenced, nearby locations will likely be referenced as well.
		"Memory Hierarchy"-
			Multiple levels of memory with the more expensive faster memory at the top and the less 
			expensive slower  memory at the bottom.
			[Processsor] -> [Registers] -> [SRAM] -> [DRAM] -> [Drive]
		"Block"/"Line"-
			The minimum unit of information that can be either present of not present in a cache.
			Diagram on p.474
		"Hit"-
			Finding the data in the cache.
		"Miss"-
			Not finding the data in the cache and so must be found at a lower level.
		"Hit Rate"-
			The fraction of memory accesses found in a level of the memory heiarchy.
		"Miss Rate"-
			The fraction of memory accesses not found in a level of the memory heiarchy.
		"Hit Time"-
			The time required to access a level of the memory heiarchy, including the time
			needed to determine wether the access was a hit or miss.
		"Miss Penalty"-
			The time required to fetch a block from a lower level(including time to access the block) and pass
			it to a higher level and then to the requestor.
	5.2 Memory Technologies p.477-484
		SRAM-
			Usually used for Cache
			Integrated Circuits that are memory arrays with (usually)a single port for access.
			Close to the Processor and don't need to refresh, so mostly match processor time.
			Due to Moore's Law it is usually integrated onto the processor chip.
		DRAM-
			Usually used for Main Memory
			The values in DRAM are stored on a capacitor. A sinle transistor can access this stored charge.
			DRAM must periodically be refreshed since it can't hold the charge forever.
			To refresh you just have to read the contents then write it back.
			DRAM uses a two level decoding structure allowing an entire row to be refreshed at a time.
		Flash/Magnetic Disk-
			Usually Used for Storage
			Flash has limited rewrites whereas Disk does not.
			A disk is dvided into concentric circles called "tracks"
			each track is divided into "sectors" which contain information.
			
			To access Disk data first step is to "seek" which is positioning the head over the proper track of a disk.
			Second the disk head must rotate until it lands on the proper sector. This time is called "rotational latency"/"rotational delay"
			Lastly it must transfer the information from the sector which varies depending on sector size, rotation speed, and recording density.	
	5.3 The Basics of Caches p.484-500
		"Direct Mapped Cache"-
			A cache structure in which each memory location is mapped to exactly one location in the cache.
			(Address) % (Number of Blocks)
			This can be represented with the diagram on page 485, note that only the 3 lowest bits are used to map in 
			the specific example because it only has 8 locations. (2^3)
		"Tag"- 
			A field in the table used for a memory heiarchy that contains the address information required to idenitfy
			wether the associated block in the heiarchy corresponds to a specific word.
			
			In the direct map example only the 3 lowest bits were used. The upper bits can be what are stored in the tag
			to verify the identity of the stored wordsize address.
		"Valid Bit"-
			A field in the table of a memory heiarchy that indicates that the associated block in 
			the heiarchy contains valid data. 
			If it is set then it is valid, if not then it is not valid.
		Accessing a Cache-
			p.487
		Diagram with Tag Field and Cache Index-
			p.489
		Handling Cache Misses-
			1. Send Original PC (PC-4) Value to Memory
			2. Instruct main memory to read and wait for memory to complete it's access.
			3. Write the cache entry, putting the data from memory in the data portion of the entry. Upper bits into tag field. Valid bit is on.
			4. Restart the instruction execution.
		Handling Writes-
			"Write Through"-
				A scheme in which writes always update both the cache and the next lower level of the memory heiarchy.
				Ensuring that the data between the two are consistant.
			"Write Buffer"-
				A queue that holds data while the data is waiting to be written to memory.
			"Write Back"-
				A scheme that handles writes by updating the values only to the block in the cache, then 
				writing the modified block to the lower level of the heiarchy when the block is replaced.
		Example Cache-
			p.496(may be relevant to homework)
		"Split Cache"-
			A scheme in which a level of the memory heiarchy is composed of two independant caches that operate in parallel 
			with each other, with one handling instructions and one handling data.
	5.4 Measuring and Improving Cache Performance p.500-522
		CPU Time-
			CPU Time = (CPU.execution clock cycles + Memory-stall block cycle * Clock cycle time)
			Memory Stall Clock cycle = (Read-stall cycles + Write-stall cycles)
			Read-stall cycles = Reads/Program  * Read miss rate * Read miss penalty
			Write-stall cycles = Writes/Program * Write miss rate * write miss penalty + write buffer stalls
		AMAT-
			AMAT = Time for a hit + Miss Rate * Miss Penalty
		More Efficient Placement of Blocks-
			"Fully Associative Cache"-
				A cache structure in which a block can be placed in any location in the cache.
				Every location has to be searched so this is typically handled in parallel.. although it is expensive to implement.
			"Set Asscoiative Cache"-
				A cache that uses a fixed number of locations (atleast 2) where each block can be placed.
				Multiple locations for the same data. In these the data can be passed into any of the possible block sections.
				(Address) % Numbers of Sets
		EXERCISE Mapping the Cache-
			p.507
			Can go a bit further for some more stuff.
		Choosing Which Block to Replace-
			"Least Recently Used"-
				A replacement scheme in which the block replaced is the one that has been unused for the longest time.
		"Multilevel Cache"-
			A memory heiarchy with multiple levels of caches, rather than just a cache and main memory.
	5.5 Dependable Memory Heiarchy p.522-529
		Error Detection...
		Redundancy for Reliability...
	5.6 Virtual Machines p.529-533
		...
	5.7 Virtual Memory p.533-564
		"Virtual Memory"-
			A technique that uses main memory as a "cache" for secondary storage.
		"Physical Address"-
			An address in main memory.
		"Protection"-
			A set of mechanisms for making sure that multiple processes utilizing the same memory that they 
			wont interfere with eachother's data.
		"Page Fault"-
			An event that occurs when an accessed page is not present in main memory.
		"Virtual Address"-
			An address that corresponds to a location in virtual space and is translated by address mapping to a physical address
			when memory is accessed.
		"Address Translation"/"Address Mapping"-
			The process in which a virtual address is mapped to a physical one.
			IE: p.535
		Page files...
		"Segmentation"-
			A variable-size address mapping scheme in which an address consists of two parts: a segment number, which is mapped
			to a physical address, and a segment offset.
		"Page Table"-
			The table containing the virtual to physical address translations in a virtual memory system.
			The table, which is stored in memory, is typically indexed by the virtual page number; each entry
			in the table contains the physical page number for that virtual page if the page is currently in
			memory.
		Page Table Example- 
			p.540
		Page Fault-
			If the valid bit for a virtual page is off, a page fault occurs. 
		"Swap Space"-
			The space on the disk reserved for the full virtual memory space of a process.
		Swap Space Example-
			p.541
		LRU More In depth-
			p.542
		Making Address Translation Fast: The TLP...
		...
	5.8 A common framework for memory heiarchy p.564-571
		In depth explanation on each factor of the cache.
	5.9 Using a finite-state machine to control a simple cache p.571-576
		...
	5.10 Parallelism and Memory Heiarchy: Cache Coherence p.576-581
		...
	Useless Chapters... p.581-611
		...
pages 611-699 Chapter 6 - Parallel Processors from Client to Cloud
	6.1 Introduction p.611-616
		"multiprocessor"-
			A computer system with at least two processors. This computer is in contrast to a uniprocessor.
			which has one and is increasingly hard to find today.
		"task-level parallelism"-
			utilizing multiple processors by running indepednant programs simultaniously.
		"parallel processing program"-
			A single program that runs on multiple processors simultaniously.
		"cluster"-
			A set of computers connected over a local area network that functions as a single large multiprocessor.
		"multicore microprocessor"-
			A microprocessor containing multiple processors ("cores") in a single integrated
			circuit. Virtually all microprocessors today in desktops and servers are multicore.
		"Shared Memory MultiProcessor(SMP)"-
			A parallel processor with a single physical address space.
	6.2 The Difficulty of Creating Parallel Processing Programs- p.616-624
		"strong scaling"-
			Speedup achieved on a multiprocessor without increasing the size of the problem.
		"weak scaling"-
			Speedup achieved on a multiprocessor while increasing the size of the problem proportionally to the increase in the
			number of processors.
	6.3 SISD, MIMD, SIMD, SPMD, and Vector p.624-633
		"SISD"-
			Single Instruction Stream (Data) using A uniprocessor.
		"MIMD"-
			Multiple Instruction Stream(Data) using A multiprocessor.
		"SPMD"-
			Single Program Multiple Streams
		"SIMD"-
			Single Instruction Stream using Multiple Processors
		"data-level parallelism"-
			Parallelism achieved through performing the same operation on independant data.
		vector...
	6.4 Hardware Mutlithreading p.633-638
		"Hardware Multithreading"-
			Increasing utilization of a processor by switching to another thread when one thread is stalled.
		"Thread"-
			A thread includes the program counter, the register s tate, and the stack. It is a lightweight process,
			whereas threads commonly share a single address space, processes don't.
		"Process"-
			A process includes one or more threads, the address space, the operating system state.
			Hence a process switch usually invokes the OS, but not a thread switch.
		"Fine-grained Multithreading"-
			A version of hardware multithreading that implies switching between threads after every instruction.
		"Coarse-grained Multithreading"-
			A version of hardware multithreading that implies switching between threads only after significant
			events such as a last-level cache miss.
		"Simultaneous Multithreading(SMT)"-
			A version of multithreading that lowers the cost of multithreading by utilizing the resources
			needed for multiple issue, dynamically schedule architecture.
	6.5 Multicore and Other Shared Memory Multiprocessors- p.638-644
		...
	6.6 Introduction to GPU- p.644-652
		Appendix C also has more on this...
	6.7 Clusters, Warehouse Scale Computers, and Other Message-Passing Multiprocessors- p.652-659
		...
	6.8 Introduction to Multiprocessor Network Topologies- p.659-664
		...
	6.10 MultiProcessor Benchmarks and Performance Models- p.665-677
		...