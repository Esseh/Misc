Chapter 1 Why Parallel Computing	
	0.0 Introduction
		From 1986-2002 microprocessor performance increased 50% a year.
		Afterward the increase dropped to 20% a year.
		Design Shifted Towards Parallelism Utilizing Multiple Processors on an integrated chip.
		Questions Arise...
			1. 20% is still a significant improvement. So why do we care?
			2. Why can't microprocessor manafacturers just keep making faster single processor systems?
			3. Why can't we build programs that automatically convert serial programs into parallel ones?
	1.1 Why We Need Ever-Increasing Performance
		Increase In Computational Power Has Allowed Certain Problems to be Solved... ie:
			1. Climate Modeling
			2. Protein Folding 
			3. Drug Discovery 
			4. Energy Research 
			5. Data Analysis
	1.2 Why We're Building Parallel Systems
		Decreasing the Size of Transistors (and increasing their density) increases their speed, but also increases power usage.
		In addition the increased power usage results in more dissipated heat.
		In order to combat the issues with increased density, the number of processors can be scaled up on integrated chips.
		A "Multi-Core CPU"
	1.3 Why We Need to Write Parallel Programs
		Consider a Video Game
		An OS can run multiple copies of that video game at once. Is this what we want?
		No, more than one video game is redundant. However we would like everything within the game to run better.
		In this case we would like coordination between a multi-CPU in order to improve performance in a way that makes sense.
		
		An example with summations(pythonesque example with pyroutines)...
			Serial Program-
				# Initialize Sum
				sum = 0
				# Sum Each Value
				for i in arr: sum += i
			Parallel Program-
				# Initialize Sum
				sum = 0
				# Initialize an Output Buffer to Capture Parallel Output
				output_buffer = OutputBuffer(runtime.NumCPU)
				# Compute the array partition size.
				part_size = len(arr) / runtime.NumCPU
				# Create a Function That Uses Shared Data to perform partial sums(Static Scope Rule)
				def partialSum(arr):
					# Base Case, no more array then no more sum
					if arr == []: return
					# Otherwise Run Next Partition in Parallel
					else: py partialSum(arr[part_size:])
					
					# Initialize Partial Sum
					partial_sum = 0
					# Compute partial sum
					for i in arr[:part_size]:
						partial_sum += i
					# Send partial sum into output buffer.
					output_buffer.put(partial_sum)
				# Begin Running the Routine in Parallel
				py partialSum(arr)
				# Sum Each value from the output buffer.
				for i in range(len(output_buffer)):
					sum += output_buffer.get()
		The parallel program is much larger (13 lines) versus the serial program (2 lines) and so there is definately a difference in overhead.
		With a smaller summation < 100000 elements the serial will probably be faster.
		But an advantage of the parallel program is splitting work.
		Imagine if you were running a 100 core processor performing a summation across 1000000000000 (1 trillion elements)
		The serial program would run through 1 trillion sums, on the otherhand operating in parallel it will be done as quickly as it would with only 10 billion elements.
		
		However not all prallel programs are created equal. Imagine if instead of the output buffer we had a guarded random access array where each core waits for an input.
		This bypasses the need for consolidation by a master-core. Core 100 sends its output to arr[99] for core 99. It sends its output to arr[98] for core 98 and so on.
		This minimizes some of the work done by utilizing pipelining.
	1.4 How Do We Write Parallel Programs
		The previous example as an example of "Data-Parallelism". This is to say the data was partitioned across multiple cores to be operated on.
		There is also "Task-Parallelism" which as you may expected involved partitioning actions out to be performed across multiple cores.
		As an example of the latter in game-dev imagine a function Listener(), that reads I/O from the User and updates internal keyboard state.
		On a separate core we can run a different function UpdateWorldState() which has it's own set of routines.
		
		In the sum example data was coordinated utilizing "communication" (in this case the output_buffer), the work was evenly distributed, a process referred to as "load balancing"
		Some for of "synchronization" is needed in order for things such as the master core in the sum example to wait for the others to finish.
		In this case the output_buffer is the means of sycnhronization (getting from it stalls the core until it sees something.)
	1.5 What We'll be Doing
		We'll be focusing on programs that are explicitly parallel.
		Shared Memory Systems: Share Access to Computer Memory
		Distribted Memory Systems: Cores Must Communicate Explicitly
	1.6 Concurrent, Parallel, Distributed
		Concurrent Computing: Multiple Tasks Can be in Progress
		Parallel Computing: Multiple Tasks Cooperate Closely to Solve a Problem
		Distributed Computing: Program may need to cooperate with other programs
HW 1
	1...
		problem size of n
		p processors
		
		for (my_i = my_first_i; my_i < my_last_i; my_i++){
			my_x = compute_next_value(..);
			my_sum += my_x;
		}
		Devise formulas for the function that calculate my_first_i and my_last_i
		
		Hint: you may use “my_rank” to get the process_id, and start from considering the case that
		n is evenly divisible by p.
		
		Answer-
			I came up with my own answer, but Park's answer is genius.
			Annotated with Python Comments
			
			Q = n/p	# Quotient, partition size
			R = n%p	# Remainder, how many extra elements need to be handled with care.
			if my_rank < R			# So long as we need to deal with leftovers...
				my_count = Q+1 		# Have that processor deal with '1' extra element. This way each extra will be taken care of.
				my_first_i = my_rank * my_count # Figure out the offset.
			else
				my_count = Q		# Deal with the normal problem size.
				my_first_i = my_rank * my_count + R		# When dealing normal problem size remember to take into account the offset from the extras earlier.
			my_last_i = my_first_i + my_count			# If I recall park included a -1, however the code uses a < symbol. So omitting -1 should be correct.
			
			Example-
				n = 107
				p = 5
				Q = 21
				R = 2
				
								p0						p1					p2				p3				p4
				my_count		21+1					21+1				21				21				21
				my_fist_i		0*(21+1)				1*(21+1)			2*21+2			3*21+2			4*21+2
				my_last_i		0*(21+1)+(21+1)			1*(21+1)+(21+1)		(2*21+2)+21		(3*21+2)+21		(4*21+2)+21
				
								p0	p1	p2	p3	p4
				my_count		22	22	21	21	21
				my_fist_i		0	22	44	65	86
				my_last_i		22	44	65	86	107
	2...
		Consider 1
		my_x is computed from compute_next_value(..)
		Assume the computation time of compute_next_value(..) depends on the data elelment
		i=0 requires T clocks
		i=k requires (k+1)*T clocks
		
		One idea of achieving the load balancing under the given assumption is using the cyclic
		assignment of the work to processors.
		
		with p=4 processors, 
		i=0 is assigned to p0,
		i=1 to p1
		i=2 to p2
		i=3 to p3
		then i=4 to p0
		i=5 to p1, ...
		Write a formula to compute the total computation time in clocks on each processor with
		the given assumptions.
		
		example... 
			p0		p1		p2		p3
			1T		2T		3T		4T
			5T		6T		7T		8T
			9T		10T		11T		12T	...
		
		answer...
			# Begin from our given processor_id
			# iterate through our entire input...
			# ... only considering the inputs that are handled by our processor.
			for(i=my_rank; i < n; i+=p)			 
				# Add to the load according to the formula.
				my_rank += T*(i+1)
	5...
		I would say that it is an example of task parallelism as you are partitioning actions (send/recieve) and not partitioning data.
		Pipelining the data doesn't transform it into partitioned data.
		
		Park's Answer: It is a hybrid
Chapter 1 Missed Topics
	Parallel Programming Paradigms-
		Explicit: using explicit constructs such as PThreads
		Implicit: done automatically, auto-conversion from serial to parallel code. Less efficient.
Chapter 2 Parallel Hardware and Parallel Software p.78 - p.92
	2.1 Some Background
		2.1.1 The Von Neumann Architecture
			Main Memory		CPU		I/O
				|			 |		 |
				|====================|

			Each memory location has an address that references it. By using that address the contents of that location can be accessed.
			The CPU is separate into two potions...
				Control Unit: Determins What Action to Perform
				ALU(Arithmatic Logic Unit): Performs Computation
			Data in the CPU are stored in 'registers'
			The Control Unit has its own register known as the "Program Counter" which helps it figure out which part of the loaded program to run.
			Instructions and Data are passed between the interconnected portion.
			read/fetch: Moving from memory to CPU
			write: Moving from CPU to memory
			Von Neumann Bottleneck: The separation of CPU and Memory. (Memory being slower) The CPU can execute instructions hundreds of times faster than instructions can be fetched from memory.
		2.1.2 Processes, Multitasking, and Threads
			The OS handles multiple processes and how data is allocated to those processes.
			A process contains...	
				1. Machine Language Program
				2. A block of memory, call stack, and memory heap
				3. Descriptors of resources allocated from the OS
				4. Security Information
				5. Information about the state of the process.
			Multitasking: A technique where a processor(even a single core one) can run multiple programs at once by giving them a certain 'time slice' to operate.
			If a process needs to wait for a resource it will 'block' allowing other processes to run instead.
			Threading: A technique where a process can be split into tasks(sub-processes) which run independantly. Thus even if one thread blocks, the other can run.
			Switching between threads is often faster than switching between processes.
			Threads need their own call stack and program counters.
			
			When a child-thread is created it is referred to as a "fork"
			When a child-thread terminates it is referred to as a "join"
	2.2 Modification to the Von Neumann Model
		2.2.1 The Basics of Caching
			CPU Cache/Cache: A collection of data that can be accessed quicker than main-memory.
			Caches Utilize Two Principles...
				Temporal Locality: Recently accessed data is likely to be accessed again.
				Spatial Locality: If data is accessed, then nearby data is also likely to be accessed.
			Data is moved into the Cache in blocks on an on-need basis to take advantage of these properties.
			
			Cache are typically separated into levels 
			L1 at the top is the smallest and quickest, L2 is bigger but slower than L1 and so on...
			
			When data is going to be retrieved it will check the L1 cache, if it 'misses' then the L2 all the way until main-memory until it 'hits'.
			
			Often data will be written to a cache directly which creates a data inconsistency.
			This is solved through write-policies...
				Write-Through: When writing to the cache, also write to main memory.
				Write-Back: When updating the cache line entry, mark it as dirty. Only when the cache entry is removed should the main memory entry be updated.
		2.2.2 Cache Mappings
			Fully-Associative Cache: Can be placed anywhere in the cache.
			Direct-Mapped Cache: Cache Entries are Hashed In
			n-Way-Set-Associative Cache: Cache Entries can be Hashed in any of the n sections.
			"Eviction Policy: Least Recently Used"...
				A policy such that when hashing to an entry in n-Way-Set-Associative 
				in which each section is occupied it evicts whichever one was least recently used.(temporal locality)
		2.2.3 Caches and Programs: An Example
			Row-Major: A scheme in which multiple dimensional arrays are stored as a single large array. Given A[i][j][k] for i for j for k is most efficient.
			Column-Major: A scheme in whcih multiple dimensional arrays are stored as a single large array. Given A[i][j][k] for k for j for i is most efficient.
		2.2.4 Virtual Memory
			Virtual Memory: A technique that allows main memory to act as a cache for secondary storage. (alleviating another bottleneck)
			Only the currently executing parts are kept in main memory.
			Inactive portions are stored in a section of secondary storage referred to as a "swap space"
			Pages: The unit in which Virtual Memory Operates On
			Pages are assigned 'Virtual Page Numbers' in case multiple programs need to access a single page.
			Page Table: The means that a virtual address is translated into a physical address for a page.
			EXAMPLE-
				Suppose are Addresses are 32-bit
				Our pages are 4kilobytes = 4096 bytes
				Each byte in the page can be identified with 12 bits, 2^12 = 4096
				
				The remaining 20 bits can be used for identifying a specific page.
				
				If the page isn't found in this virtual cache then it must be loaded into main memory.
			Translation can be expensive, processors help aleviate this issue by caching addresses through a 'translation-lookaside-buffer'(TLB)
			
			Because direct-disk access is utilized the penalty for a TLB miss can be large. In the result of such a 'page fault' it will be loaded in(slowly.)
			Because of this slow disk access a write-back policy is used.
		2.2.5 Instruction-Level Parallelism
			Instruction-Level Parallelism: A technique in which components are utilized in such a way that instructions can be initiated simultaniously and executed simultaniously.
			Pipelining-
				A concept inspired by the assembly line. Imagine a dirty clothes bin, a washer, a dryer, and a clean clothes bin.
				Instead of waiting for all the dity clothes to get into the bin it can be loaded into the washer. While washing more clothes can be loaded into the bin.
				When they can be moved to the dryer, the waiting clothes can be added to the washer, freeing up the bin again... and so on...
				
				In the processor if each action of a pipeline stage were to take 1 clock we could see the execution time of an instruction to be		
				n + i - 1 clocks
				n is the number of pipeline stages.
				i is the number of instructions.
				
				Of course this isn't the true speed, the effective speed of a pipeline is usually that of the slowest stage.
				In addition 'data hazards' can occur. Essentially garuntees about the validity of data in the pipeline are broken, and so there must be stalling.
				EXAMPLE-
					i1: set reg2 to reg3
					i2: load into reg1, reg2
					Instruction Fetch, Decode, Read, Compute, Write
					IF	D	R	C	W
					i1
					i1	i2
						i1	i2	
							i1 i2
							i1		i2
								i1
									i1
					In this case the hazard caused only a delay of 1 clock. But in practice it may be even hundreds of clocks of slowdown, and there may be dozens of hazards at once.
				Data Hazards Can be Separated into 5 General Categories-
					Read After Write: i2 needs to read data i1 is writing to. (read before write in pipeline)
					Write after Read: i2 needs to write to data that i2 needs to read from. (write before read in pipeline)
					Write after Write: i2 needs to write to data that i1 is writing to.
					Structural Hazard: i1 needs hardware device, i2 needs same hardware device.
					Branch Hazard: i1 is executing, but i2's existance depends on result of i1. 
			Multiple-Issue-
				This is a technique where separate functional units of the CPU (such as adders) perform actions in parallel to increase computation time.
				for example...
					for(i = 0; i < 1000; i++)
						z[i] = x[i] + y[i]
				The work can be divided, if we have for example two-adders.
				z[0] and z[1] can be computed at the same time.
				
				If the functional units are scheduled at compile time then it is "static multiple issue"
				If the functional units are scheduled at run time then it is "dynamic multiple issue"
				A processor that supports dynamic multiple issue is said to be "superscaler"
				
				Speculation: a technique where the processor/compiler makes a guess about an instruction and executes the instruction on the basis of the guess.
				For example it may predict a branch and go ahead and perform the computation, alternatively it may see that adjacent instructions do not pertain to eachother, as such they 
				can be executed in parallel.
				
				If the speculation is false, then it must retract it's action and then perform the correct action.
				In a compiler's case it will likely generate additional code to handle the case where the guess was incorrect.
				In the processor case it would store the guessed result in a buffer, then determine if it should use it or not.
		2.2.6 Hardware Multithreading
			Thread-Level Parallism: Providing parallelism through simultaniously executing threads.
			Threads are 'coarser grained' or larger units
			Individual Instructions would be 'finer grained' or smaller units
			Hardware Multithreading: A technique where the hardware switches from a thread that cannot proceed to another thread that can do work. Needs very fast thread switching.
			Fine-Grained Multithreading: Threads are switched after every instruction.
			Coarse-Grained Multithreading: Only switching threads when a thread is very busy(such as loading from main memory)
			Simultanious Multithreading: Exploting superscaler processors to utilize multiple functional units across multiple threads.
	2.3 Parallel Hardware
		2.3.1 SIMD Systems
			Terminology-
				Flynn's Taxonomy: A classification scheme to describe computer architectures based on the number of data strings and number of instruction streams.
				SISD: Single Instruction, Single Data Stream. Classic Von Neumann Can fetch a single instruction and single piece of data at a time.
				SIMD: Single Instruction, Multiple Data. 
			SIMD operates on multiple pieces of data with the same operation...
				Suppose we wanted to add to n elements of an array the respective element of another array and there are n datapaths.
				The computation can be performed instantly across each of the n ALUs.
				However the ALU in such a system has to be idle or run the data.
				Lookahead becomes impractical, so spare functional units can't just perform future operations.
				
				SIMD can easily deal with large loops of data simultaniously with simple operations.
				This is an excellent example of "data parallelism"						
			A "Vector Processor"...
				is a processor that utilizes SIMD principles to perform efficient actions across arrays.
				Vector Registers can hold many contiguous values, and so long as the data can fit in vector registers can typically be computed near instantly.
				Their Memory is interleaved with a delay before accessed memory can be reaccessed.. however if contiguous blocks needs to be accessed then access is still quick.
				Additionally they can perform "strided memory access", essentially elements can be accessed in abnormal sequences ie: 1,3,5,7...
				Unforutnantly because they deal with fixed linear units they have low scalability.			
			A "Graphics Processing Unit"(GPU)... 
				translates an internal representation of it's computation into an array of pixels through 
				a "graphics processing pipeline". Programmable stages of the pipeline are referred to as "Shader Functions", these are typically simple and ran in parallel.
				Most GPU utilize SIMD.
				GPUs also make heavy use of thread multi-threading. While this makes it great at dealing with large throughput problems, it cannot perform small problems very well.
		2.3.2 MIMD Systems
			MIMD: Multiple Instruction, Multiple Data Path, typically "asynchronous"
			There are typically two types of MIMD Systems...
				1. Shared Memory: Each shares memory, communicates through shared data structures.
				2. Distributed Memory: Each has independant memory and communicates through messaging.
			Shared Memory Systems Are Further Broken Down...
				1. UMA(unform memory access)...
					Each Integrated Chip(possibly multiprocessors) access the same global memory through an interconnect.
					Typically easier to program for.
				2. NUMA(non-uniform memory access)...
					Each Integrated Chip(possibly multiprocessors) access different blocks of memory. When needing to communicate with eachother uses special hardware to access the other.
					Can potentially access more memory.
					Access to non-owned memory can be slower, however access to own memory is much faster than with UMA.
			Distributed Memory Systems-
				Clusters: systems connected by some network (ie: PCs connected through Ethernet)
				Shared memory systems usually connect the computational units together across these networks.
				They are typically referred to as "hybrid systems"
				A "grid" provides the infrastructure to turn a large amount of nodes into a unified distributed-memory system.
		2.3.3 Interconnection Networks
			Slow Interconnects will cause a Slow Network
			Shared-Memory Interconnects-
				"Bus": a collection of parallel communication wires with some hardware that controls access across the bus.
				While they are cheap, as more and more things are connected to a bus, contention for use of the bus increases which causes degredation of performance.
				
				"Switched Interconnects": Utilizes switches to route the flow of data between devices.
				A "crossbar switch"(page 57) demonstrates the concept.
				They are typically faster than bus's, but that much more expensive.
			Distributed-Memory Interconnects-
				"Direct Interconnect": each switch is directly connected to a processor-memory pair. The Switches are connected to eachother.
				Ring and Toroidal Mesh Example(page 58)...
					The mesh allows more connections, but more expensive overall.
				"Bisection Width": A measure of the number of simultanious communications.
				It can be seen as the number of connections that need to be removed to create two perfect communication halves.
				the Bisection Width of a toroidal mesh is 2*sqrt(p), where p is the amount of nodes we're connecting.

				"Bandwidth" of a link is the rate that it can transmit data. (given typically in megabit or megabyte per second)
				"Bisection Bandwidth": A measure of the qualuty of a network. Typically the bandwidth of the communication channel * the bisection width.
				
				The ideal interconnect is a "fully connected network" where every node can reach every other node. It's bisection width is p^2 / 4
				It can be impractical for larger system though. It requires p^2/2 + p/2 links and each switch must be connecting to p links.
				(Visible on page 60)
				
				Hypecubes-
					They are built inductively.
					A one dimensional hypercube is a fully connected network with two nodes.
					A two dimensional hypercube are two one dimensional hypercubes connected by their common switches.
					A three dimensional hypercube are two two dimensional hypercbes connected by their common switches..
					and so on...
					
					A hypercube of dimension d has p = 2^d nodes.
					A switch in a d-dimensional hypernode is connected to a processor and d switches.
					The bisection width is p/2
					
					The switches have to support more wires though, 1 + log2(p) wires
				Inderect Interconnects-
					(page 61)
					In these cases. Typically the links are undirectional between the switching network and the processor.
					The switching network can then be seen as what actually routes the 'unidirectional' access into the other processors.
					
					A "unidirectional crossbar" is one type of switching network. (best seen on page 62)
					So long as the processor isn't being spoken to, then any processor can initiate conversation with any other processor.
					Requires p^2 switches.
					
					An "omega network" is anotehr type of switching network. (best seen on page 62)
					A distadvantage of them is that sometimes otherwise open conversation can be blocked. But they are much cheaper.
					Requires 2*p*log2(p) switches
					
					The bisection width of a crossbar and omega network are p and p/2 respectively.
				Latency and Bandwidth-
					Latency: the time taking between having sent the data, and for the first byte of that sent data to be read.
					Bandwidth: the rate at which that destination recieves data after that first byte.
					So if latency is l seconds, and bandwidth is b bytes per second, then the transmission time of n bytes is 
					l + n/b
		2.3.4 Cache Coherence
			Consider multiple cores sharing data.
			Both contain the value of x = 3 in the cache.
			Core 1 performs x++
			Core 2 performs z = x afterward.
			What is the value of z? Is it 3 or 4?
			What's to say that their caches are coherent?
			
			Cache were designed for single processors, this is the cache coherence problem.
			
			Snooping Cache Coherence-
				When a core updates an entry, it can broadcat the cache line that may be invalid for other processors.
				Another core that is 'snooping' along the network can then mark it's own cache line as invalid so that it can update to the proper value.
			Directory Based Cache Coherence-
				A central 'directory' data structure keeps information on the cache-lines.
				When data is updated by a core, this metadata is stored in the directory. 
				Thus instead of broadcasting, one can just 'snoop' the directory.
				This is much more scalable than traditional snooping.
			False Sharing-
				A situation in distributed data systems where different processors with their own local caches are operating on the same data.
				Each time one operates on the data, the other processor's cache entry is invalidated and it must re-update.
				This can have disatorous consequences for performance.
		2.3.5 Shared-Memory Versus Distributed Memory
			Shared Memory doesn't scale as well as message passing as the rate of conflicts increases across parallel actions.
	2.4 Parallel Software
		2.4.1 Caveats
			The book will focus primarily on MIMD.
			The focus will mostly be on "SPMD"(single program, multiple data)
		2.4.2 Coordinating The Processes/Threads
			Parallelization: The Process of Converting a Serial Program Into a Parallel One
			Embarassingly Parallel: Problems that can be parallelized simply by dividing the work.
		2.4.3 Shared-Memory
			Communication is Implicit
			Terminology-
				Dynamic Thread: The master thread creates new threads to solve the problem as needed.
				Static Thread: The master thread initializes all the threads and then solves the problem.
				Nondeterminism: An value is nodeterministic if the interleaving of parallel actions influences the final result.
				Race Condition: The condition that causes Nondeterminism
				Critical Section: A section of code that should only be executed by one thread at a time. The programmer should provide "mutually exclusive" access to it.(mutex)
				Serialization: The process of turning parallel code serial. Occurences should be minimized, critical sections likewise should be as small as possible.
				"busy-waiting": A technique where a thread waits by testing a condition in a while loop. (yielding the thread can help some)
				Semaphore: a syncrhonization variable that works like a mutex but allows a group of exclusive users.
				Monitor: A high level mutex object whose methods can only be accessed by one thread at a time.
				Transactional Memory: A technique where things are set up as atomic transactions. Either the entire transaction can complete, or changes are rolled back.
			Thread Safety-
				Thread Safe: Can be used in multiple threads without unwanted consequences.
		2.4.4 Distributed-Memory
			Message-Passing-
				Think of Pipes
				Some Message Passing APIs have additional functions...
					1. broadcast: a single process transmits it's message to all the processes
					2. reduction: where consolidated messages are piped into a collective computation
				The most popular is MPI(Message Passing Interface)
			One-Sided Communication-
				In "one-sided communication" or "remote memory access" one process modifies the data of another process.
				Two Problems Must Be Solved...
					1. The sender needs to know that the data is safe to copy to: Solved by Synchronizing Processes
					2. The reciever needs to know that data is available: Solved by referring to a flag that the sender can check. ("polling")
			Partitioned Global Address Space Languages-
				In a PGAS language, the location os distributed data is known by the programmer. So they can avoid false-sharing or condition data
				such that false-sharing doesn't occur.
		2.4.5 Programming Hybrid Systems
			Hybrid system APIs tend to be very performant, though hard to use.
	2.5 Input and Output
		I/O Through Multiple processes tends to be nondeterministic.
		Assumptions Made in Book Towards I/O...
			1. in distributed-memory, only p0 will use stdin
			2. all p can access stdout and stderr
			3. typically only p0 will use stdout, but other p can use it for debugging
			4. multiple processes will not open the same file
			5. debug output will always include the process/thread id
	TODO: Finish Taking Notes on This After Midterm
	2.6 Performance
	2.7 Parallel Program Design
	2.8 Writing and Running Parallel Programs
	2.9 Assumptions
Reference Books 1
	Kai Hwang's Classification of MIMD + Section Diagrams
		UMA-
			PVP
			SMP
		NUMA-
			DSM
		ELSE-
			MPP
			COW
	Architecture of Multicore Processors + Diagrams
		1. Heiarchial Design
		2. Pipelined Design
		3. Network-Based Design
	Multicore Processor Design Issues-
		Data Transfer Between Cores-
		Scalable interconnection network - to increase number of Cores
		Fault Tolerancy of Entire System
		Low Power (Desired through Interconnect Network)
		Efficient Mem/IO Systems for fast data transfer (avoid idle cores) (L1,L2,L2 Caches)
Prog 1 Notes
	Pipe Usage
		Pipe is a Message Passing Interface(MPI) for distributed services.
		Normally it is only used on unix based systems (Linux/Apple systems)
		The usage is simple, a communication channel is opened and data can be sent or recieved.
		It is a bounded blocking buffer, that is to say that while reading from it if there is nothing to read the current thread will wait.
	Pipe API
		fork() // Creates a copy of the current process returning the process_id of the created process. (From the child process context it will see it as having returned 0.)

		wait(&int) // Waits for a child process to terminate, which the child process terminates it's return code is stored in &int.
		
		pipe(arr[2]) //utilizes a two element array as the pipe which can pass messages between threads.
					 //arr[0] is for reading 
					 //arr[1] is for writing
					 
		write(&int,&source_data,int data_size) // writes to the &int (implied to be arr[1])
											   // the source data as bytes
											   // with knowledge of the data size.
											   
		read(&int,&output_data,int data_size)  // reads from the &int (implied to be arr[0])
											   // into the data structure &output_data
											   // with knowledge of the data size.
		
		close(&int)	// closes the read or write communication channel. &int is implied to be part of the pipe.
Prog 2 Notes
	Pthread Usage
		Pthreads are ways of sharing data across processes. Useful for Shared Memory
		Data that needs to be protected from race conditions are thus protected with 'synchronization variables' most commonly a mutex.
	Pthread API
		pthread_t example	// pthread type
		pthread_mutex_t	example // pthread mutex type
		
		pthread_create(&pthread_t, NULL, (void*)(*)(void*), (void*))
		// It takes in the address of a thread to initialize
		// a pthread_att_t(assume it's NULL)
		// A function pointer for a function of the following form... void* foo(void* arg)
		// data to be passed into the argument of void* foo(void* arg)
		
		pthread_join(pthread_t, (void*)*)
		// Waits for the pthread specified to finish.
		// When it finishes the value sent by pthread_exit((void*)*) will be stored in the other argument.
		
		pthread_exit((void*)*) 
		// terminates the current thread and passes it's argument to the parent thread.
		
		pthread_yield()
		// yields the current thread's turn so that the OS can decide where to place its resources.
		
		lock(&pthread_mutex_t)
		// Tries to lock the shared mutex.
		// If it is already locked the thread waits until it can lock the shared mutex.
		
		unlock(&pthread_mutex_t)
		// Unlocks the shared mutex
