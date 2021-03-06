//////////////////////////////
//// Park -- this is a C++ version of the OpenMPP Hello program
//// Slightly different version - parallel exec using tot num of threads in the system
////
//// compile and run:
//// $> g++ -fopenmp -o xxx Park-omp-hello2.cpp
//// $>./xxx
////   //system finds the total number of threads available
//////////////////////////////

#include <cstdlib> //needed for atoi
#include <iostream>
#include <omp.h>   
using namespace std;

void Hello(void); //Thread function

///////////////////////////////////
int main(int argc, char* argv[]) 
{
  //int thread_count = atoi(argv[1]);
  
  //parallel exec of Hello() with total threads in the system (1 per logical core) 
  #pragma omp parallel //num_threads(thread_count)
   Hello();

  return 0; 
}//main

//////////////////////////////////
void Hello(void) 
{
  int my_rank = omp_get_thread_num();
  int thread_count = omp_get_num_threads(); //gets tot number of threads in the system

  #pragma omp critical //protect cout statement as c.s.
   cout<<"Hello from thread_"<<my_rank<<" of "<<thread_count<<endl;
  
}//Hello
