Exam 1 Notes
	Introduction-
		Process Design Migration-
			Started from Scalar CPU...
			to ILP(Instruction Level Parallelism)...
				Scalar Pipelined...
					Instructions are Executed in a Pipeline ie:
						IF 	DE	RE	CO	WR
						i1
						i2	i1
						i3	i2	i1
						i4	i3	i2	i1
						i5	i4	i3	i2	i1
							i5	i4	i3	i2
								i5	i4	i3
									i5	i4
										i5
					
					Assuming each stage takes 1 clock and there are 0 hazards
					total_clock_time = pipeline_size + number_of_instructions - 1
				To Multiple-Issue Processors...
					Multiple Instructions are performed in parallel using different functional units. (such as an ALU)
					"Speculation": The ability of a processor/compiler to make predictive 'guesses' about whether or not instructions can be performed in parallel.
					
					A processor(HW) capable of speculation at runtime is said to be "dynamic-multiple-issue" OR "superscalar"...
						The guessed results are loaded into a buffer, if it is incorrect it throws away that result.
						Examples of superscalar processors include...
							http://user.engineering.uiowa.edu/~hpca/LectureNotes/Lecture4Spr10.pdf
							parallel pipelines... 
								Forking Pipelines
								Can Move Down Different Pipeline if one is stalled(hazard) while another instruction is unaffected by that hazard.
							diversified pipelines...
								Forking Pipelines
								Pipeline Travelled Depends on Instruction Type (Specialized Pipelines, Differing Sizes)
							out_of_order_execution (dynamic)...
								dispatch buffer pushes intructions through(possibly out of order) so that they can properly be performed in parallel.
								redorder buffer corrects instruction order where it matters.
					A compiler(SW) capable of speculation is said to be "static-multiple-issue"...
						VLIW(Very Long Instruction Word) is the process of breaking down a program into units that can be performed in parallel.
						Test Code is inserted to assert it's guess. If the guess fails, then it takes corrective measures.
				Issues with ILP...
					1. Circuit Complexity Increases Greatly as performance is increased.
					2. Power Consumption and Heat Generation Increases Greatly as performance is increased.
			to TLP(Thread Level Parallelism)...
				Multithreading...
					A process can have multiple 'threads' with their own PC(for execution state) and Call Stack(for functions). They share memory with their parent process.
					The OS/Processor can switch between threads even in single processor systems.(time slices/time sharing)
				SMT(Simultanious Multi-Threading)...
					Exploiting Multiple-Issue in order to run operations on multiple threads simultaniously.
				to Multicore Processors...
					Independant cores
					cores have their own functional units
					cores have their own cache(L1)
					cores can share cache (L2,...)
					cores share main memory
		Prallel Machines-
			SISD...
				Single Instruction, Single Datapath
				THE Von Neumann Model
			SIMD...
				Single Instruction, Multiple Datapath
				Vector/Array Processors...
					Vector Registers: Carries contiguous data
					Reading from same data has delay. However reading from contiguous arrays is quick.
					Instructions are mostly simple.
					Instructions operate on entire arrays.
					Large Amounts of Basic Functional Units
					Example...
						Vector Register Size is 16 Words						
						for(int i = 0; i < 16; i++)
							a[i] += x[i]
						
						All of these additions can be performed in parallel. 
						Instantly computed.
					DOWNSIDES...
						Terrible at dealing with smaller data.
						Has to commit fully to actions. (ALUs are either idle or executing common instruction)
						Scales terribly
				GPU(SIMD + MIMD)
					Utilizes specialized pipeline to generate pixel arrays. (SIMD)
					Also makes liberal use of multi-threading for I/O. (MIMD)
					Programmable Sections of Pipeline can be located on OS.(Shader Functions)
			MIMD...
				Multiple Instruction, Multiple Datapath
				Shared-Memory...
					Communicates through Shared Data Structures
					Each Processor shares a Common Memory
				Distributed-Memory...
					Communicates through Message Passing
					Each Processor has It's Own Memory, and its own cache.
					Processors Can Utilize Eachothers' Memory(but this is typically a bad idea due to False Sharing)
	Chapter 1-
		Global Sum Computation Example-
			Two Approaches-
				1. Master Thread Sums Output from Many Serial Threads. Master thread consolidates the indidual sums into a final sum. (Prog2)
				2. Tree-Like Computation (parallelsum.cpp)
		Parallel Programs-
			Task Parallel: Actions in a program are being partitioned. ie: One thread handles GUI, antoher handles computation.
			Data Parallel: Data in a program is being partitioned. ie: Perform partial sums on sections of an array to compute a final global sum.
		Issues-
			Communication: Sending/Recieving Messages, Sharing Information
			Synchronization: Protection of time sensitive code so that result becomes deterministic.
			Load Balancing: How to actually partition the data intelligently.
		Parallel Programming Paradigms-
			Explicit Parallelism: Performed by Hand, more efficient.
			Implicit Parallelism: Performed Automaticly, less efficient.
			Auto Conversion: Typically difficult/impossible at current tech level
	Chapter 2-
		Parallel HW and SW
			Von Neumann Bottleneck-
				Memory and CPU are separated. Mem is much slower but most data is in Mem. 
				This separation creates a bottleneck where Mem cannot transfer as fast as the CPU handles it.
				Thankfully There are Some Solutions...
					1. Cache...
						Level 1 Cache/CPU Cache: Owned by CPU, Small, Very Fast
						Level 2 Cache/Shared Cache: Used by Multiple CPU, Larger, Not as Fast
						.... and so on.
						The idea is to store pieces of data in a faster to access area that can be accessed first.
						Terminology-
							Fully-Associative: Data is crammed in, entire cache has to be checked.
							Direct-Mapped: Data is hashed in, accessed through hashed value.
							Set-Associative: Data is hashed in to buckets. If there is no room, the least recently used item is replaced.
							Write-Through: When writing to the cache, also write to main memory.
							Write-Back: When updating the cache line entry, mark it as dirty. Only when the cache entry is removed should the main memory entry be updated.
							Write-Allocate: On write-miss Load the Block into the Cache, then write-hit.
							No-Write Allocate: On write-miss Write the entry into memory.
						Cache Entries are Placed In According to...
							Temporal Locality: Recently Accessed Data, Handled by caching as data is needed.
							Spatial Locality: Nearby Data, Handled by caching entire lines of data instead of individual units.
						x-Major...
							A technique where two-dimensional array is placed and accessed contiguously in memory.
							Row-Major: arr[5][7] ....
								Laid out in memory as...
								[00,01,02,03,04,05,06] , [10,11,12,13,14,15,16] , ... , [40,41,42,43,44,45,46]
							Column-Major: arr[5][7] ....
								Laid out in memory as...
								[00,10,20,30,40] , [01,11,21,31,41] , ... , [06,16,26,36,46]
							These will behave differently in nested loops...
								Given arr[i][j]
								for i
								 for j
								 is row-major friendly
								 
								for j
								 for i
								 is column-major friendly
								 
								The cache hits/misses can differ greatly depending on the style of iteration.
								Typically matching the wrong major accesses to the arr will result in a cache miss on every access.
								Whereas if you use the correct one you will only suffer a cache miss when the cache line runs out.
					2. Virtual Memory...
						Very Big Data cannot fit in Mem as a Single Unit
						Sections of Secondary Storage are used as a cache for Memory

						Page Entries are Stored in the Page Table
						Page Entries are Indexed by "Virtual Addresses" which can be translated into physical addresses to find a relevant page file in the page table.
						Page Entries are typically large because disk access is slow.
						There are two ways of translating a virtual address...
							1. Through Cached Translation in a TLB(Translation Lookaside Buffer)
							2. Through Computing The Translation...
								Page Files are of some size 2^n bytes.
								Architectures allow some precision for memory values. We can just assume it's a 32^bit system.
								We can use n of these 32 lower order bits to refer to a specific byte.
								Thus we can use the remaining 32-n bits to refer to individual page table entries.						
							QUICK COMPUTATION EXAMPLE-
								Suppose a page table entry is 4096 bytes in size and it exists in a 32-bit architecture.
								How many page table entries does the page table support?
								ANSWER: 2^(32-log2(4096)) = 1048576 entries
					3. ILP/Low Level Parallelism	- fine-grained...
						Already Covered
					4. TLP/HW Multithreading		- coarse-grained...
						Fine Grained SMT: Switches after every instruction
						Coarse Grained SMT: Switches during I/O interruption
						Typically switching schemes fall between these extremes.
	Reference Books-
		Kai Hwang's Classification of MIMD-
			PVP(Parallel Vector Processor)(UMA)...
				[VP] ...     [VP]
				[Crossbar Switch]
				 |	 ...	  |
				[SM]		[SM]
			SMP(Symmetric Multiprocessor)(UMA)...
				[P/C] ... [P/C]
				[Bus or Xbar  ]
				[SM]  [SM] [SM]
			MPP(Massively Prallel Processor)(NORMA)...
				[P/C]	[P/C]
				[LM]	[LM]
				[NIC]	[NIC]
				|	..	|
				[Network]
			DSM(Dstributed Shared Memory Machine)(NUMA)...
				[P/C]	[P/C]
				[LM]	[LM]
				[NIC]	[NIC]
				[DIR]	[DIR]
				|	..	|
				[Network]				
			COW(Cluster of Work Stations)(NORMA)...
				[Computer]	[Computer]
				|			|
				[NIC]		[NIC]
				|	..		|
				[	NETWORK   ]
		Architecture of Multicore Processors-
			Heiarchial Design...
				[CORE 1]		[CORE 2]		[CORE 3]		[CORE 4]
					|				|				|				|
					[L1 Cache]		[L1 Cache]		[L1 Cache]		[L1 Cache]
						|				|				|				|
					[		L2 Cache		]		[		L2 Cache		]
								|							|
							[			L3 Cache/Memory			]
							
				"Shared Memory"
			Pipelined Design...
				[							CACHE/MEM						]
				[CORE 1]  ---> [CORE 2] ---> ..................--> [CORE N]
				
				"Systolic Array of Cores"
			Network-Based Design...
				[CACHE/MEM]			[CACHE/MEM]						[CACHE/MEM]
				[CORE 1   ]			[CORE 2   ]			.....		[CORE N]
				_____|___________________|____________________________|_____
				|				Interconnect Network					   | <--->
				|__________________________________________________________|
				
				"Message Passing"
		Multicore Processor Design Issues-
			Data Transfer Between Cores- 
				Onchip interconnection provides enough bandwidth
			Scalable interconnection network-
				Increase number of Cores
			Fault Tolerancy of Entire System-
				Can continue working in the face of error
			Low Power (Desired through Interconnect Network)-
				Reduced complexity of IN
			Efficient Mem/IO Systems for fast data transfer (avoid idle cores) (L1,L2,L2 Caches)- 
				Reduced Blocking of Communication => Less Idling
				More Cores -> More Cache Level to fulfill bandwidth requirements
	Chapter 2(Cont)
		Multicore Structures-
			UMA...
				[CORE CORE]	[CORE CORE]
					|			|
					[	IN		]
							|
						[MEMORY]
			NUMA...
				[CORE CORE]<->[CORE CORE]
					|			|
					[IN]		[IN]
					|			|
					[MEM]		[MEM]
		Skillicorn's Taxonomy-
			SIMD-
				Distr-Mem...
							[DM]
							  |
						/<->[DP]<-\
					[SW]<->[DP]<-[SW]-[IP]<->[IM]
						\<->[DP]<-/
							 |
							[DM]
				Shared-Mem...							
					[DM]<->\   /<->[DP]<-\
					[DM]<->[SW]<->[DP]<-[SW]-[IP]<->[IM]
					[DM]<->/   \<->[DP]<-/
			MIMD-
				Shared-Mem...
					[DM]<->\  /<->[DP]<-[IP]<->[IM]
					[DM]<->[SW]<->[DP]<-[IP]<->[IM]
					[DM]<->/  \<->[DP]<-[IP]<->[IM]
				Distr-Mem...
							[DM]
							|
					  /<->[DP]<-[IP]<->[IM]
					[SW]<->[DP]<-[IP]<->[IM]
					  \<->[DP]<-[IP]<->[IM]
							|
							[DM]
		Example SIMD System(Cell Processor)-
				[Processor]
					  |  |
			 <->[I/O]-|IN|-[Mem]<->RAM
			 <->[I/O]-|IN|-[Mem]<->RAM
					  |  |
			   [SPE]--|  |--[SPE]
			   [SPE]--|  |--[SPE]
			   [SPE]--|  |--[SPE]
			   [SPE]--|__|--[SPE]			   
			 Generic SIMD Structure-
				[IM] <-> [IP] -> [DP1] ... [DPn]
									|		|
									[DM]	[DM]
		IN-
			Terminology-
				Netowrk Size(N): number of nodes in IN
				Node Degree(d): Number of links per node
				Network Diameter(D): any node can reach any other node within D (worst case hops)
				Bisesction Width: Number of simultanious communications between two halves of the network. (worst case)
			Shared-Mem-
				Bus...
					Shared connected components.
				Xbar...
					Switched Network
			Distr-Mem-
				Static/Direct IN...
					Each Switch Connected Directly to Processor/Memory Pair
					Examples...
						Linear...
							Node Degree: 2
							Network Diameter: n-1
							Routing Scheme: source_tag = dest_id - source_id
							Trace until tag = 0, East is negative movement, West is positive movement.
						Ring...
							Node Degree: 2
							Network Diameter: n/2
							Routing Scheme: sourcetag = destid -courseid
							new tag = (tag (+/-) 1) mod n		, + for counterclockwise (decreasing), - for clockwise movement (increasing)
							trace until tag = 0
						Fully Connected...
							Node Degree: n-1
							Network Diameter: 1
						K-Level Binary Tree...
							Network Size for M Children is: (m^k - 1) / (m-1) 
							Node Degree: 3
							Network Diameter: 2(K-1)
						K-Dimensional Mesh...
							Node Degree:2*K
							Network Diameter: K(n-1)
							Routing Scheme: source tag = dest_id - source_id
							Tags have parts based on dimensionality ie... XYZ for 3D
							Trace until all tags are 0. East/South is negative movement, North/West is positive movement.
						K-Dimensional Toroidal Mesh...
							Node Degree: 2*K
							Network Diameter:floor(K*Kth_root_of(n)/2)
						K-Dimensional Hypercube...
							Network Size: 2^K
							Node Degree: K
							Network Diameter: K
							Gray Coding: Refers to the semantics of node positions where adjacent nodes only differ by one bit. 
							Routing Scheme...
								avail_links = source xor dest
								Start at 010
								Goal is  101

								010 xor 101 = 111 -> 011 xor 101 = 110 -> 110 xor 101 = 101
								
				Dynamic/Indirect IN...
					NOTE: Practice Perfect and Inverted Shuffle
					Switches may not be directly connected to a node.
					Examples...
						Bus...
							Connection of Wires: MIMD Shared-Mem Systems
						X-Bar...
							Single Stage
							Expensive
							Node Degree: 3 < d < 4
						Omega Network...
							Omega Network Switch...
								2x2 X-Bar with two outputs, two inputs.
								Four States it can be in:
									Pass(straight)
									Cross Over(X)
									Upper Broadcast(Upper input feeds to both outputs)
									Lower Broadcast(Lower input feeds to both outputs)
							Number of Stages: Log2(N)
							Routing...
								routing based on dest_id only
								ie: 101
								    Follow low path
									10X
									Follow high path
									1XX
									Follow low path
									XXX
									DONE
								If the path is blocked, then the communication is buffered in the switch and waits.
						Benes Network...
							Number of Stages: 2*Log2(N)-1
							Routing Scheme...
								Begin at Start
								Take Any Path you Want until middle of CLOS
								Then follow dest_id
								Possible Paths: 2^(num_stages/2)
							Drawing Network...
								Source -> Inverted Shuffle -> CLOSE Network -> Perfect Shuffle -> Dest
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
Last Shoehorned In Materials-
	Dynamic Thread: The master thread creates new threads to solve the problem as needed.
	Static Thread: The master thread initializes all the threads and then solves the problem.
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