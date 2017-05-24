//// Kenneth Willeford
//// Prog4 - Parallel MergeSort
//// 
//// This program runs a parallel merge sort as defined 
//// in Prog4.pdf based on the options provided.
////
//// compile and run:
//// $> g++ -fopenmp -o xxx mergesort.cpp
//// $>./xxx 100 4 trace
////   //4 is the number of threads to use - any
////   //100 is the size of the array to be sorted - any
////   //trace is to show the output with tracing - optional
#include<iostream>
#include<cstdlib>
#include<ctime>
#include<omp.h>
using namespace std;

long* list;				// The Global Array that will be sorted.
long  N;				// The Length of the Global Array, first command line argument.
long  p;				// The number of threads to create, second command line argument.
bool traceOutput;		// Whether or not to trace merge sort output

// Derived from gnu.org example
// For additional information see: http://www.gnu.org/software/libc/manual/html_node/Comparison-Functions.html#Comparison-Functions
int CompareLongs (const void *a, const void *b){
  const long *da = (const long *) a;
  const long *db = (const long *) b;
  return (*da > *db) - (*da < *db);
}

// Based on rank and core_difference merges two sorted sub-arrays into a combined sorted array.
void Merge(long r,long d){
	long lbegin = r*N/p;			// Get Start of Left Array
	long lendrbegin = (r+d)*N/p;	// Get Start of Right Array / End of Left Array
	long rend = (r+2*d)*N/p;		// Get End of Right Array
	
	// Copy the subarrays into their own arrays for processing.
	long lcopyi = lbegin;
	long rcopyi = lendrbegin;
	long* leftArray  = new long[d*N/p];
	long* rightArray = new long[d*N/p];
	#pragma parallel for
	for(int i = 0; i < d*N/p; i++){
		leftArray[i]  = list[lcopyi++];
		rightArray[i] = list[rcopyi++];
	}

	// Merge the created arrays into the main array by <.
	lcopyi = 0;
	rcopyi = 0;
	for(int i = lbegin; i < rend; i++){
		// If there is nothing left in the leftArray
		if(lcopyi >= d*N/p){
			// Copy contents from the rightArray
			list[i] = rightArray[rcopyi++];
		// If there is nothing left in the rightArray
		} else if (rcopyi >= d*N/p){
			// Copy contents from the leftArray
			list[i] = leftArray[lcopyi++];
		// If the leftArray element is less than the rightArray
		} else if(leftArray[lcopyi] < rightArray[rcopyi]){
			// Copy contents from the leftArray.
			list[i] = leftArray[lcopyi++];
		}else{
			// If the right array element is equivalent or less then copy the contents from the rightArray.
			list[i] = rightArray[rcopyi++];
		}
	}
}

// Performs the merge sort in parallel
void MergeSort(){
	// Special Case, only 1 thread being made. In this case just run qsort on list and exit.
	if(p == 1){ qsort(list,N,sizeof(long),CompareLongs); return;}
	
	long MyRank = omp_get_thread_num();		// Get Thread ID
	long* LocalList = new long[N/p];	    // Create Evenly Partitioned Local List
	long Start = N/p * MyRank;				// Get the start position of the list.
	
	// Copy Relevant Global Array Contents to Local Array
	#pragma omp parallel for
	for(long i = 0; i < N/p; i++)
		LocalList[i] = list[Start++];
	
	// Print local list information if tracing.
	if(traceOutput){
		#pragma omp critical
		{	
			cout << "Thread_" << MyRank << ", local_list: ";
			for(long i = 0; i < N/p; i ++)
				cout << LocalList[i] << " ";
			cout << endl;
		}
		// Used to syncrhonize so that multiple threads wont have access to cout. (Should probably have made it its own function with critical section.)
		#pragma omp barrier
	}	
	// Sort Local Array.
	qsort(LocalList,N/p,sizeof(long),CompareLongs);
	
	// Print sorted local list information if tracing.
	if(traceOutput){
		#pragma omp critical
		{	
			cout << "Thread_" << MyRank << ", sorted local_list: ";
			for(long i = 0; i < N/p; i ++)
				cout << LocalList[i] << " ";
			cout << endl;
		}	
	}
	
	// Copy Local Array Contents to Global Array
	Start = N/p * MyRank;
	#pragma omp parallel for
	for(long i = 0; i < N/p; i++)
		list[Start++] = LocalList[i]; 

	// Determine who is sender or reciever and terminate thread / merge where necessary.
	long divisor = 2;
	long CoreDifference = 1;
	while(divisor <= p){
		#pragma omp barrier
		if(MyRank % divisor == 0) Merge(MyRank,CoreDifference);
		CoreDifference *= 2;
		divisor *= 2;
	}
}

// Retrieves the command line arguments
void GetCommandLineArguments(int argc ,char* argv[]){
	N = atoi(argv[1]);	// get size of array
	p = atoi(argv[2]);	// get number of threads to make
	// determine if a trace should occur
	if(argc > 3) traceOutput = string(argv[3]) == "trace";
}

// Creates a random array based on N.
void MakeRandomArray(){
	list = new long[N];
	srand(time(NULL));
	// rand() isn't thread safe so parallel for causes unintended behavior, on my machine elements will cycle like so [7,1,7,1,7,1,7...]
	for(long i = 0; i < N; i++){
		list[i] = rand() % N;
	}
}

// Executes the MergeSort then returns the execution time.
double BenchmarkMergeSort(){
	double time_elapsed = omp_get_wtime();		// Start Time
	#pragma omp parallel num_threads(p)
	MergeSort();								// Perform the merge sort.
	// If tracing output then print the sorted list.
	if(traceOutput){
		cout << "sorted list:" << endl;
		for(int i = 0; i < N; i++){
			cout << list[i] << " ";
		}
		cout << endl;
	}
	return omp_get_wtime() - time_elapsed;		// Final Time	
}

// Function to verify if the list is sorted.
bool ListIsSorted(){
	for(long i = 1; i < N; i++)
		if(list[i] < list[i-1]) return false;
	return true;
}

// Prints the final output. Requires the execution time.
void PrintResult(double t){
	if(ListIsSorted()){
		cout << "**verified that list is sorted." << endl;
	} else {
		cout << "**list is NOT sorted." << endl;
	}
	cout << "Using P=" << p << ", n=" << N << ", Time taken: " << t << " sec" << endl;
}

int main(int argc, char* argv[]){
	GetCommandLineArguments(argc,argv);
	MakeRandomArray();
	PrintResult(BenchmarkMergeSort());
}