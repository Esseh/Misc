Chapter 2
	Parallel Hardware
		Cache coherence
			This refers to a problem with sharing data between multiple processing units.
			Suppose both are executing in parallel at the same time storing a value in their own cache with x = 1
			Thread1
				x = 2
			Thread2
				y = x
			What is the final value of x? How does thread2 know that x has changed? This is the cache coherence problem.
			
			Snooping cache coherence-
				In this case in a bus based system Core1 with Thread1 can broadcast "x has been changed"
				Thread2 'snoops' the bus. Seeing that x has changed Thread2 knows it needs to update.
				This works with both write-back and write-through caches.
				In write-through one can just snoop for changes to memory, in write-back an extra communication needs to be made as the current version
				isn't in memory yet.
			Directory-based cache coherence-
				A 'directory' is a data structure that stores metadata about each cache line. The data structure is distributed,
				each machine has a directory for it's local memory.
				Whenever memory is accessed remotely the local machine will consult the directory of the target machine to check it's status.
			False Sharing-
				A situation that occurs when certain assumptions are made about ownership of data where multiple cores end up repeatadly invalidating 
				a shared cache line(or part of a cache line.)
		Shared-memory versus distributed-memory
			Interconnect Contention isn't very scalable as seen in Shared Memory, however message passing as seen in distributed memory is very scalable.
	Parallel Software
		Caveats
			The book focuses mostly on SPMD
			task parallel: obtaining parallelism by dividing tasks among the processor, "task-parallelism"
		Coordinating the Processes/threads
			Load Balancing: Fairly Dividing Work Amongst Threads
			Parallelization: Converting serial program to parallel
			Embarassingly Parallel: Programs that can be made parallel by simply dividing the work.
			
			The important steps are...
				1. Load Balancing
				2. Arranging for processes/threads to sychronize
				3. Arrange for communication among the processes/threads
		Shared Memory
			Shared Variable: Can be read and written by any thread
			Private Variable: Can be read and written by only one thread.
			Dynamic and Static Threads-
				Dynamic Thread Paradigm: A master thread produces and joins threads on a on-need basis.
				Static Thread Paradigm: All threads are forked after any needed setup by master thread. After threads all join the master thread terminates.
			Nondeterminism-
				This is a situation that occurs when the result of an operation depends on the order of parallel instructions.
				ie: 
					Thread1
						y++
						y = 2
					Thread2
						x = y
				The result is a "race condition". This can be fixed by Serialization: Turning something parallel into something serial.
				In this case these are critical sections, so if x = y needs to occur first then y++ and y=2 needs to wait. 
				Mutually exclusive access can be given through a 'mutex'/'lock'(mutual exclusion) , 
				'semaphores'(only a limited amount can access) , 
				or 'busy-waiting'(wait until flag says it's okay)
				
				Other structures include 'monitors' (a moniter's methods can only be accessed by one thread at a time)
				
				Another idea is 'transactional memory' like a database treats a collection of actions as a single unit.
			Thread Safety
				Some functions are not thread safe (such as printing to screen). In these cases they should be protected as critical sections.
		Distributed-memory
			Message-passing has at minimum a send and a recieve function.
			Typically there is an intermediate data structure (a pipe) that holds onto data.
			sender -> [data] -> reciever
			The sender will wait until there is room, likewise the reciever will wait until there is data. This is 'blocking' behavior.
			In a "broadcat" a single process sends data to every process
			In a "reduction" values recieved are computed into a single value.
			
			One-sided communication-
				There is one sender and one reciever.
				In order to synchronize for safety they also speak through a 'flag' which they can 'poll' (or syncrhonization)
			Partitioned global address space languages-
				In PGAS private variables are kept on the local machine. The programmer has explicit control of the distribution of memory that way 
				the programmer can know exactly what they are getting into.
		Programming hybrid systems
			Programming hybrid is possible.
	Input and Output
		I/O can be erratic and unsafe
	Performance
		Speedup and efficiency
			Linear Speedup(best): Tparallel = Tserial / p
			S(speedup) = Tserial / Tparallel
			E(efficiency) = S / p = Tserial / (p*TParallel)
			Tparallel = Tserial / p + Toverhead
		Amdahl's law
			S = 1 / (1-ParallelizalPortion) + (ParallelizalPortion/NumProcessors)
		Scalability
			Definition-
				Suppose we run a prallel program with all fixed resources
				Suppose now we increase the number of threads that are used by the program.
				If we can find a rate of increase such that it always has efficiency E then the program is scalable.
			Example-
				Suppose Tserial = n, where n is the problem size and Tparallel = n/p + 1
				Then
				
				E = n / (p*(n/p+1))
				E = n / (pn/p + p)
				E = n / (n + p)
				
				We want to increase the number of processors by a factor of k
				E = n / (n + p*k)
				
				In addition we want to scale the problem size by x so that the efficiency remains unchanged.
				E = n*x / (n*x + p*k)
				
				So now we must find some x, such that  E = n / (n + p)
				
				Suppose that x = k
				E = n*k / (n*k + p*k)
				E = n*k / k(n + p)
				E = n / (n + p)
				
				So the program is scalable.
			Special Cases in Scalability-
				If we increase the number of threads and we can keep the efficiency fixed without increasing the problem size then the program is said to be strongly scalable.
				If we increase the number of threads at the same rate as the problem size while efficiency remains the same, then it is said to be weakly scalable.
	Parallel Program Design
		General Steps Towards Parallelization-
			1. partitioning: divide computation to be performed and data operated on into small tasks. Identify tasks that can be executed in parallel.
			2. communication: determine what communications need to be performed by the tasks in the previous step.
			3. agglomeration or aggregation: combine tasks from previous steps into bigger tasks where makes sense. (Simplification / Reducing Communication Cost)
			4. mapping: assign these tasks to threads dividing the work fairly.
			
			p.67(physical)/p.88(e-textbook) has good example to work through
Chapter 4
	Processes, Threads, and Pthreads
		Process Contains-
			Block of Memory for Stack
			Block of Memory for Heap
			Descriptors of Resources System has Allocated
			Security Information
			Information About the State of the process
		Process data is also 'private'
		A Thread Contains much much less which gives them their other name 'light-weight process'
		Threads can share memory.
	Hello, World
		Execution
			gcc -g -Wall -o pth hello pth hello.c -lpthread
			./pth hello <number of threads>
		Preliminaries
			Global Variables are shared across threads.
			Local Variables/Function Arguments are thread specific.
		Starting the threads
			pthread_t is an 'opaque object' meaning that it's data members are not necessarily known to the programmer.
			int pthread_create(pthread_t*,const pthread_attr_t*,(void)(*)(void*),void*)
		Running the threads
			pthread_join ...
		Stopping the threads
			pthread_yield
			pthread_exit
		Error checking
			pass along the rank in the error message
		Other approaches to thread startup
			static thread example
	Matrix-Vector Multiplication
		Refer to Prog3
	Critical Sections
		Pi Estimate Example-
			We can parallelize it by splitting up the negative and positiver sections. 
			This provides a good estimate for pi atleast until values get very large.
			Because a common variable 'pi_estimate' is being modified by multiple threads a 'race condition' exists.
			This race condition can be resolved by treating the modification of 'pi_estimate' as a 'critical section'
		Block Divide Way of Load Balancing
	Busy-Waiting
		busy-waiting is the act of halting execution in an infinite loop until a flag says that it is okay to continue(flag is updated by another thread.)
		This has terrible performance and hogs resources on the computer.
		In addition optimizing compilers don't necessarily know about the intention of the loop and so by optimizing the single threaded case the busy-waiting can be undone.
	Mutexes
		"Mutex" <-> "Lock"
	Producer-Consumer Synchronization and Semaphores
		Semaphore-
			A structure with n resources.
			sem_wait has two behaviors: if 0 resources then block until resources are available, otherwise decrement the resource.
			sem_post: increments the resource
		Semaphores can be used to Implement Message Passing in Shared Memory Systems....
			Message Passing
				Thread1 -> Thread2 -> Thread3 -> Thread1 -> ...			THREAD ORDERING IS IMPORTANT
			Shared Memory(message array)
				[1|2|3|4|5|...|n]											HOW TO SYCNRHONIZE ACTION? : ANSWER- SEMAPHORE IS THE BEST
				 \/ \/ \/\/   \/
				 T1 T2 T3 T4  T(n-1)
	Barriers and Condition Variables
		Barrier-
			A syncrhonization technique where the program cannot proceed until all threads have reached the 'barrier'
			Barriers are not typically a part of the Pthread library and has to be implemented.
		Busy-waiting and a mutex
			Implementing a barrier with busy-waiting and mutex is easy.
			A lock guards the incrementing of a counter.
			Each thread then busy-waits until the counter passes the thread count.
		Semaphores
			By utilizing two semaphores a barrier can also be easily implemented.
			A counter still exists but it is protected by a semaphore.
			There are two cases.
			1. not the last thread
			2. is the last thread
			
			In case 1 the counter is incremented(book keeping to tell if it's the last thread or not)
			Next the counter semaphore's resource is freed.
			Then it will consume the resource of a second semaphore. (initially 0)
			
			In case 2 the counter is reset.
			Then it will releases the resource of the second semaphore. (increments to 1)
			Then each value is able to pass through normally.
		Condition variables
			Utilizing condition variables a barrier becomes trivial to implement.
			pthread_mutex_lock(&lock)
			counter++;
			if(counter >= thread_count ){ 
				counter = 0
				pthread_cond_broadcast(&cond_var)
			} else {
				while (pthread_cond_wait(&cond_var, &mutex));
			}
			pthread_mutex_lock(&unlock)
	Read-Write Locks
		Pthreads read-write locks
			Read-Write Locks are an example of CREW(Concurrent Read, Exclusive Write)
			The goal of a Read-Write Lock is the following.
			1. While anyone is reading, writers have to wait for their turn.
			2. While anyone is writing, readers and other writers have to wait for their turn.
			
			A parallel linked list example...
				pthread rwlock rdlock(&rwlock);
				Member(value);
				pthread rwlock unlock(&rwlock);
				
				pthread rwlock wrlock(&rwlock);
				Insert(value);
				pthread rwlock unlock(&rwlock);
				
				pthread rwlock wrlock(&rwlock);
				Delete(value);
				pthread rwlock unlock(&rwlock);
		Performance of the various implementations
			tl;dr RW Lock excels when reads are the common case.
	Caches, Cache Coherence, and False Sharing
		Cache Memory-
			Fast Memory Used to Bypass Slower Memory, Typically Small in Size
		Temporal Locality-
			If used recently, likely to be used again.
		Spatial Locality-
			If used, nearby is also likely to be used.
		Cache Line/Cache Block-
			Abusing spatial locality by loading cache entries in sequences.
		Cache Coherence Problem-
			Suppose two threads execute actions with separate caches.
			Thread1: x++;
			Thread2: y = x;
			How can Thread2 have the correct result?
		False Sharing-
			Consider the situation like in the HW with matrix multiplication.
			If a cache line spills over into another thread's territory and modifies the content then that content is dirty.
			If that thread is on another processor then false sharing will occur, possibly on multiple writes in a row each thread will keep invalidating the cache
			entry forcing both threads to constantly retrieve the cache entry again.
		Sources of Cache Incoherence and Their Solutions-
			1. Sharing of writable data : solution- have a common cache
			2. process migration        : solution- snoopy bus  (write update, write invalidate) (MESI)
			3. i/o bypass cache 		: solution- DSM(Directory Based)
		MESI-
			Supports WB
			Cache Lines Represented with four states...
				(M)odified	: Present only in current cache and is dirty.
				(E)xclusive	: Present only in current cache and is clean.
				(S)hared	: May be present in other cache and is clean.
				(I)nvalid	: Cache line is invalid.
			There are 'snoopers' on the processor/cache side and the memory controller. Both are able to 'snoop' the state of the different caches.
		S-I-Protocal(SI in MESI)-
			Supports WT
		DSM(Distributed Shared Memory)-
			home node: where memory and directory live
				When memory is requested the home node tries to provide, on a miss it will retrieve the block from a remote node and mark that node as invalid.
			local node: origin of request
				Attempts to retrieve memory from home node assuming that the directory says that the local copy is bad.
			remote node: node that has copy of block (distributed)
				Holds onto copy of memory. Gets updated on write-back