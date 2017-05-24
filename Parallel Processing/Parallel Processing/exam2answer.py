1. Write three issues of coordinating processes or threads...
	Load Balancing
	Minimizing Communication
	Synchronization
2. List the four steps to parallelize something...
	1. Partition		: Separate the work into parts.
	2. Communication	: Determine what communications are needed.
	3. Aggregation		: Combine tasks from previous steps into larger steps.
	4. Mapping			: Assign these tasks to threads, dividing their work.
3. List the three sources of cache incoherence and provide a solution for each...
	1. Sharing of Writable Data - Solve with a common cache
	2. Process Migration - Solve with a snoopy bus (write update, write invalidation)
	3. I/O bypass cache - Solve with DSM
4. Name the two types of communication methods...
	Broadcast: Send a message to every thread.
	Reduction: Collect messages for some purpose.
5. List the four states of the MESI Protocal...
	(M)odified: dirty cache line in current cache
	(E)xclusive: clean cache line in current cache
	(S)hared: clean cache line present in other cache
	(I)nvalid: Cache line is no good
6. Explain sharing data among threads in Java Threads...
	In Java shared data is stored in objects known as monitors.
	With monitors shared memory can be declared as such, and so by
	using that shared data the object knows it is a critical section.
7. Read-Write Locks are an example of CREW, explain how they work...
	Concurrent Read, Exclusive Write
	This is to say that so long as no one as writing then any amount of readers can read.
	A writer can only write so long as no one else is doing any work.
8. Provide definitions to or explain the following concepts...
	a. Cache Coherence...
		This refers to ensuring that shared data is correct regardless 
		of if it's accessed in separate locations.
	b. Snooping...
		This refers to a technique where the processor can 
		peek at a part of the system where other parts broadcast
		special infomation. For example it can verify whether or not a variable was
		modified in another cache by checking if that cpu broadcasted the change.
	c. DSM...
		This refers to Distributed Shared Memory
		tl;dr separate machines are treated as one large computer.
	d. MESI Protocal...
		A protocal useful for systems that require WB such as DSM.
		By expanding the definition of cache entries to encompass four different states
		WB can be efficiently implemented.
	e. SI-Protocal...
		Refers to the SI in MESI. With only those two parts it's possible to support WT.
	f. Shared and Private Variables...
		Shared Variables refers to variables global between threads.
		Private Variables refers to variable local to a thread.
	g. Nondeterminism...
		This refers to the prediction of a result whenever there is a race condition.
	h. PGAS...
		Partitioned Global Address Space Languages
		This refers to keeping private variables on the local machine.
		Shared variables can be distributed. This allows explicit control
		for the programmer in determining how they are distributing their data.
	i. False Sharing...
		This refers to a situations where two threads are writing to data shared between current cache lines.
		As a result they repeatedly invalidate eachothers cache lines.
	j. Busy-Waiting...
		A technique where sycnrhonization occurs by waiting in an infinite while loop until a codnition is met.
		Typically very poor performance.
	k. Mutexes...
		A data structure that allows mutually exclusive access to critical sections.
	l. Producer-Consumer Synchronization...
		This is a sycnrhonization technique where the output of one thread is the input for the next and so on.
		While possible on shared memory systems it is typically a message passing technique.
	m. Barriers...
		A data structure that does not allow continuing execution until every single thread has
		reached it.
	o. Condition Variables...
		A data structure that reclaims a mutex (used with a mutex) and then yields control to another thread
		until a condition is fulfilled.
	p. Temporal Locality and Spatial Locality...
		Temporal Locality refers to the idea that something that was accessed recently will likely be accessed again.
		Spatial Locality refers to the idea that something that was near something that was accessed will like be accessed itself.
	q. Home Nodes, Local Nodes, and Remote Nodes...
		Home Nodes: In DSM this is where the 'directory' is located. It mediates access to data and if it needs to will provide data itself.
		Local Node: In DSM this is the origin of a memory request. First it will consult the home node's directory, and if needed it will request the memory from home.
		Remote Nodes: In DSM this is what holds distributed memory blocks.
9. Compare and Contrast. What does a process contain? What does a thread contain?...
	A process contains an allocated heap/stack, the executable code, security information,an instruction pointer, and metadata about it's current state.
	A thread contains a heap/stack and an instruction pointer.
10. Write a sample SPMD code for message-passing API. In the example process_0 sends message to process_1 which displays the recieved message...
	if(my_rank == 0){
		send("Hello",msg_char,100);
	} else if (my_rank == 1) {
		recieve(msg,msg_char,100);
		cout << msg << endl;
	}
11. Implement a functionally equivalent program to the previous but using shared-memory instead...
	msg := "";
	if(my_rank == 0){
		while(msg != "");
		msg = "Hello";
	} else if (my_rank == 1) {
		while(msg == "");
		inner_msg = msg;
		msg = "";
		cout << msg << endl;
	}
12. Let Ts, Tp, To, P be serial_time, parallel_time, time_overhead, and the number of processors respectively...
	a. Show the formula for ideal speedup using only the above terms...
		S = Ts/Tp
	b. Show the formula for ideal efficiency using only the above terms...
		E = S/p
	c. Show the formula for effective speedup using only the above terms...
		S' = Ts/p + p*To
	d. Show the formula for effective efficiency using only the above terms...
		E' = S'/p
13. Write Amdahl's Law...
	S = 1/((1-Fe)+(Fe/p))
14. Using Amdahl's Law Solve the Following Problem...
	In a serial program a for-loop consumes 60% of the entire program time(40 seconds)
	the for loop is parallelized with 4 threads and efficiency 1.
	What is the speedup of parallelizing it?...
		S = 1/((1-Fe)+(Fe/p))
		S = 1/((1-0.6)+(0.6/4))
		S = 1/(0.4+0.15)
		S = 1/0.55
		S = 1.82
15. Suppose Ts = n and Tp = n/P + 2P. If we increase P by a factor of k, find a formula for how much we'll need to increase n in order to maintain constant (same) efficiency...
	E = n / (n/p + 2p)
	Scale p by k, scale n by x
	E = n*x / (n*x/p*k + 2*k*p)	
	find x such that E = n / (n/p + 2p) is non-trivial though doable through normal algebra at this point.
	But the problem only asked for the formula, not finding x.
16. Describe "strongly scalable program"...
	If p and n AND k*p and n are the same efficiency, then it is strongly scalable.
17. Describe "weakly scalable program"...
	If k*p and n AND p and x*n are the same efficiency, then it is weakly scalable.
18. Consider the Following Code...
	factor = 1.0
	sum = 0.0
	for(i = 0;i<n;i++,factor *= -1)
		sum += factor(2 * i + 1)
	pi = 4.0 * sum
	
	Write a code segment parallelizing the summation...
		Observe that it can be broken up into 'even' and 'odd'
		We can create the following slave function to compute sum. Assume both threads have access to the shared sum variable.
		One is positive and one is negative. Let thread0 handle even and thread1 handle odd.

		local_sum = 0.0
		factor = my_rank == 1 ? -1.0 : 1.0
		i = my_rank == 0 ? 0 : 1
		for(i = 0; i < n; i+= 2) local_sum += factor*(2 * i + 1);
		pthread_mutex_lock(&lock);
		shared_sum += local_sum;
		pthread_mutex_unlock(&lock);
		
		If so desired the loop can be further parallelized as partial sums.		
19. Utilizing Pthreads, provide a semaphore solution to producer consumer synchronization...
	void write(string s,int id){
		semaphore_wait(&sem[id+1])
		shared_message[id] = s;
		sem_post(&sem[id+1]); 
	}
	string read(int id){
		semaphore_wait(&sem[id])
		output = shared_message[id+1]
		sem_post(&sem[id+1]); 
		return output;
	}
20. Demonstrate a code segment implementing Barrier with Busy-Waiting and a Mutex...
	pthread_mutex_lock(&lock);
	count++;
	pthread_mutex_unlock(&lock);
	while(count < num_thread);
	count = 0;
21. Demonstrate a code segment implementing Barrier with a Semaphore...
	if(count != num_thread){
		sem_wait(&count_sem);
		count++;
		sem_post(&count_sem);
		sem_wait(&barrier_sem);
	} else if(count == num_thread) {
		count = 0;
		sem_post(&barrier_sem);
	}
22. Demonstrate a code segment implementing Barrier with a Condition Variable...
	pthread_mutex_lock(&lock);
	counter++;
	if (counter >= num_thread) {
		counter = 0
		pthread_cond_broadcat(&cond_var)
	} else while(pthread_cond_wait(&cond_var,&lock));
	pthread_mutex_unlock(&lock);