//// Kenneth Willeford
//// C++ version MPI merge sort
////
//// ....
//// I couldn't get get MPI to run on cygwin, I got it to recognize the header files but it still doesn't see the link libraries.
//// Another attempt I tried was using MS-MPI instead, but I also couldn't get it to run. As such I can't turn in any runtime output.
#include <cstdlib>
#include <iostream>
#include <mpi.h>
using namespace std;

int Compare(const void* a_p, const void* b_p);
void Merge(int local_A[], int local_B[], int local_n);

int main(int argc, char* argv[]){
	int my_rank, comm_sz;
	int n, local_n;
	int *local_A;
	
	MPI_Init(NULL,NULL);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	
	if(my_rank == 0){
		n = atoi(argv[1]);
		if(n % comm_sz != 0){
			cerr << "n should be evenly divisble by " << comm_sz << endl;
			MPI_Finalize();
			exit(1);
		}
		for(int dest = 1; dest < comm_sz; dest++)
			MPI_Send(&n, 1, MPI_INT, dest, 0, MPI_COMM_WORLD);
	} else {
		MPI_Recv(&n, 1,MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	}
	
	local_n = n/comm_sz; // number of elements for each process
	local_A = new int[n]; // create local list (full size n) in each process, and fill
	srandom(my_rank+1);
	for(int i = 0; i < local_n; i++)
		local_A[i] = random() % 100;
	
	cout << "Process_" << my_rank << ", local list:";
	for(int i = 0; i < local_n; i++)
		cout << " " << local_A[i];
	cout << endl;
	
	///// local list sorting in each process
	qsort(local_A, local_n, sizeof(int), Compare);
	
	//// reduction (merge) part
	int partner;
	int done = 0;
	int* local_B;
	MPI_Status status;
	
	int divisor = 2;
	int core_differ = 1;
	while(done == 0 && divisor <= comm_sz) {
		if(my_rank % divisor == 0){ 
		// receiver
			local_B = new int[n];
//=================================================================
//=================================================================
			partner = my_rank + core_differ;
			MPI_Recv(local_B, local_n, MPI_INT, partner, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
//=================================================================
//=================================================================
			Merge(local_A, local_B, local_n);
			local_n = 2*local_n; // after merge, double the local_n (size)
			delete[] local_B;
		} else {
		// sender	
//=================================================================
//=================================================================
			partner = my_rank - core_differ;
			MPI_Send(local_B,local_n,MPI_INT,partner, 0,MPI_COMM_WORLD);
//=================================================================
//=================================================================
			done = 1; // this (sender) process terminates while loop
		}
		divisor *= 2;
		core_differ *= 2;
	}
	
	// Display sorted list
	if(my_rank == 0){
//=================================================================
//=================================================================
		cout << "Sorted List: " << endl;
		for(int i = 0; i < n; i++)
			cout << local_A
		cout << endl;
//=================================================================
//=================================================================
	}
	
	delete[] local_A;
	MPI_Finalize();
	return 0;
}

int Compare(const void* a_p, const void* b_p){
	int a = *((int*)a_p);
	int b = *((int*)b_p);
	
	if (a < b) return -1;
	else if (a == b) return 0;
	else return 1;
}

void Merge(int local_A[], int local_B[], int local_n){
	int ai, bi, ci, i;
	int csize = 2*local_n;
	int* temp_C = new int[csize];
	
	ai =0; bi = 0; ci = 0;
	while((ai < local_n) && (bi < local_n)){
		if(local_A[ai] <= local_B[bi]){
			temp_C[ci] = local_A[ai];
			ci++;
			ai++;
		} else {
			temp_C[ci] = local_B[bi];
			ci++;
			bi++;
		}
	}
	
	if(ai >= local_n)
		for(int i = ci; i < csize; i++, bi++)
			temp_C[i] = local_B[bi];
	else if (bi >= local_n)
		for(int i = ci; i < csize; i++, ai++)
			temp_C[i] = local_A[ai];
		
	for(int i = 0; i < csize; i++)
		local_A[i] = temp_C[i];
	
	delete[] temp_C;
}