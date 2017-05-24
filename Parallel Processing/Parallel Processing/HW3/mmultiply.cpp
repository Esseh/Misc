///=====================================================================
/// CSCI 176 Program 3
/// Kenneth Willeford
///
///		This program performs parallel matrix multiplication on matrices
///		of the form specified in prog3.pdf.
///		Once compiled the program is ran as so...
///			<exe_name> <L_value> <m_value> <n_value> <number_of_thread>
///			ie our required test cases...
///			g++ mmultiply.cpp && ./a.out 1003 2000 3000 1 > output1.txt
///			g++ mmultiply.cpp && ./a.out 1003 2000 3000 2 > output2.txt
///			g++ mmultiply.cpp && ./a.out 1003 2000 3000 4 > output4.txt
///			g++ mmultiply.cpp && ./a.out 1003 2000 3000 8 > output8.txt
///			The relevant output for these test cases will be provided separately.
///		Additional Notes-
///			I thought I would also turn this program into a practice in
///			cache optimization. I create a 'matrix' class that can be built
///			'rotated', which allows for row-major access on column elements.
///			This is useful for optimizing the layout of data for the B operand.
///=====================================================================
#include<iostream>		// cout
#include<cstdlib>		// atoi
#include<vector>		// Dynamic Arrays (I prefer not to use the manual approach if I don't have to.)
#include<ctime>			// For Benchmarking
#include<pthread.h>		// pthread_t, mthread_mutex_t, _lock, _unlock, _create, _join
#include <sstream>		// for capturing output to send to the guarded cout
using namespace std;
//=====================================================================
// Object Definitions / Implementation
//=====================================================================
class matrix{
	// This bool is set when the matrix is created. It marks whether or not the matrix was created while 'rotated.' 
	// A rotated matrix's its column vectors are in row major.
	bool rotated;
	// The actual matrix as a 2D Dynamic Array
	vector<vector<long long int> > m;
	// The Number of Rows/Columns
	long long int r,c;
	public:
	// Empty Constructor
	matrix(){}
	// long long intiializes Matrix with its Dimensions.
	matrix(long long int rows, long long int columns, bool rot = false){
		rotated = rot;
		if(rotated)
			m = vector<vector<long long int> >(columns,vector<long long int>(rows,0));
		else
			m = vector<vector<long long int> >(rows,vector<long long int>(columns,0));	
		r = rows;
		c = columns;
	}
	// Provides the number of rows within the matrix.
	long long int rows(){ return r; }
	// Provides the number of columns within the matrix.
	long long int columns(){ return c; }
	// Retrieves an individual value in the matrix by row and column.
	long long int get(long long int row, long long int column){
		if(rotated)
			return m[column][row];
		else
			return m[row][column];
	}
	// Assigns an inidivdual value to the matrix by row and column.
	void assign(long long int row, long long int column, long long int val){
		if(rotated)
			m[column][row] = val;
		else
			m[row][column] = val;
	}
};
//=====================================================================
// Global Values
//=====================================================================
namespace GLOBAL {
	// Corresponds to the L,m,n values in the prog3.pdf specifications
	long long int L,m,n;
	// remainder rows that will need to be added in during cyclical assignment.
	long long int remainderRows = 0;
	// The number of threads
	long long int num_threads = 1;
	// The the input matrices and the output matrix.
	matrix A,B,C;
	// The execution time of a benchmark in seconds.
	double executionTime;
};
//=====================================================================
// Function Definitions
//=====================================================================
// Performs a cout command on a string guarded by a mutex.
void cout_semaphore(string);
// Master function for the matrix multiplication. Statically generates the needed threads and executes the matrix multiplication.
void*matrixMultiplicationMaster(void*);
// Gets four command line arguments. L,m,n,num_threads
void getCommandLineArguments(char* argv[]);
// Utilizes L,m,n and num_threads to initialize the matrices and any needed metadata.
void initializeMatrices();
// Performs the dot product between a row in A and a column in B.
long long int dotProduct(long long int rowA, long long int colB);
// Slave function for matrix multiplication. Performs part of the multiplication.
void* matrixMultiplication(void*);
// Takes in a generic function and performs benchmarking on it, stores the result globally.
void benchmark(void*(*)(void*),void*arg);
// Prints the final output.
void printResults();
//=====================================================================
// Main
//=====================================================================
int main(int argc, char* argv[]){
	getCommandLineArguments(argv);
	initializeMatrices();
	benchmark(matrixMultiplicationMaster,NULL);
	printResults();
}
//=====================================================================
// Function Implementations
//=====================================================================
void* matrixMultiplication(void* arg){
	// Get Current Thread ID
	long long int my_rank = (long long int)arg;
	// Output Data to screen
	ostringstream ss;
	ss << "Thread_" << my_rank << ": " << my_rank << " ~ " << GLOBAL::C.rows() << ", step " << GLOBAL::num_threads << endl;
	cout_semaphore(ss.str());
	// If there are 'remainderRows' remaining...
	if(my_rank < GLOBAL::remainderRows){
		// Then go ahead and account for extra rows...
		for(long long int i = my_rank; i < GLOBAL::C.rows(); i+=GLOBAL::num_threads)
			for(long long int j = 0; j < GLOBAL::C.columns(); j++)
				GLOBAL::C.assign(i,j,dotProduct(i,j));
	// Otherwise...
	} else {
		// Don't accout for extra rows. (don't hit the same rows twice.)
		for(long long int i = my_rank; i < GLOBAL::C.rows() - GLOBAL::remainderRows; i+=GLOBAL::num_threads)
			for(long long int j = 0; j < GLOBAL::C.columns(); j++)
				GLOBAL::C.assign(i,j,dotProduct(i,j));
	}
	// So the compiler doesn't return a warning.
	return NULL;
}

long long int dotProduct(long long int rowA, long long int colB){
	long long int sum = 0;
	long long int range = GLOBAL::m;
	for(long long int i = 0; i < range; i++)
		// Perform Dot Product to Build up sum
		sum += GLOBAL::A.get(rowA,i) * GLOBAL::B.get(i,colB);
	return sum;
}

void getCommandLineArguments(char* argv[]){
	GLOBAL::L = atoi(argv[1]);
	GLOBAL::m = atoi(argv[2]);
	GLOBAL::n = atoi(argv[3]);
	// If the number of threads specified are less than 1(or not specified at all) default to 1.
	GLOBAL::num_threads = atoi(argv[4]) < 1 ? 1:atoi(argv[4]);
	// Print to Screen
	cout << "L=" << GLOBAL::L << ",m=" << GLOBAL::m << ",n=" << GLOBAL::n << endl;
}

void initializeMatrices(){
	// Initialize Matrix A according to prog3.pdf Specifications
	GLOBAL::A = matrix(GLOBAL::L,GLOBAL::m);
	for(long long int i = 0; i < GLOBAL::A.rows(); i++)
		for(long long int j = 0; j < GLOBAL::A.columns(); j++)
			GLOBAL::A.assign(i,j,i+j+1);
	// Initialize Matrix B according to prog3.pdf Specifications
	GLOBAL::B = matrix(GLOBAL::m,GLOBAL::n,true);
	for(long long int i = 0; i < GLOBAL::B.rows(); i++)
		for(long long int j = 0; j < GLOBAL::B.columns(); j++)
			GLOBAL::B.assign(i,j,i+j);
	// Initialize Matrix C  dimensions according to prog3.pdf Specifications
	GLOBAL::C = matrix(GLOBAL::L,GLOBAL::n);
	// Determine the remainder rows. Guarding this statement is proabbly unnecessary.
	if(GLOBAL::num_threads > 0)
		GLOBAL::remainderRows = GLOBAL::C.rows() % GLOBAL::num_threads;
}

void benchmark(void*(*f)(void*),void*arg){
	// Begin Timing
	clock_t t = clock();
	// Run Function
	f(arg);
	// Get Timing
	GLOBAL::executionTime = ((float)(clock()-t))/CLOCKS_PER_SEC;
}

void*matrixMultiplicationMaster(void*){
	// Build up the requested number of threads and launch them with their IDs.
	vector<pthread_t> threads = vector<pthread_t>(GLOBAL::num_threads);
	for(long long int i = 0; i < GLOBAL::num_threads; i++)
		pthread_create(&threads[i], NULL, matrixMultiplication, (void*)i);	
	// Wait for each thread to finish before continuing.
	for(long long int i = 0; i < GLOBAL::num_threads; i++)
		pthread_join(threads[i],NULL);
}

void printResults(){
	// Print the related sub-matrix
	cout << "===C:first_20*first_10===" << endl;
	for(long long int i = 0; i < 20 && i < GLOBAL::C.rows(); i++){
		for(long long int j = 0; j < 10 && j < GLOBAL::C.columns(); j++){
			cout << GLOBAL::C.get(i,j) << " ";
		}
		cout << endl;
	}
	// Print the related sub-matrix
	cout << "===C:last_20*last_10===" << endl;
	for(long long int i = GLOBAL::C.rows() - 20; i > 0 && i < GLOBAL::C.rows(); i++){
		for(long long int j = GLOBAL::C.columns() - 10; j > 0 && j < GLOBAL::C.columns(); j++){
			cout << GLOBAL::C.get(i,j) << " ";
		}
		cout << endl;
	}
	// Print benchmark information
	cout << "Time taken (sec) = " << GLOBAL::executionTime << endl;
}

void cout_semaphore(string s){
	// Shared lock between function calls. Protects cout.
	static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
	pthread_mutex_lock(&lock);
	cout << s << endl;
	pthread_mutex_unlock(&lock);
}