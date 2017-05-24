//////////////////////////////
//// Park -- this is a C++ version of the OpenMPP Hello program
////
//// compile and run: 
//// $> g++ -fopenmp -o xxx Park-omp-hello1.cpp
//// $>./xxx 4
////   //4 is the number of threads to use - any
//////////////////////////////

#include <cstdlib> //for aoti()
#include <iostream>
#include <omp.h>
using namespace std;

void Hello(void); //Thread function

///////////////////////////////////
int main(int argc, char* argv[]) 
{
  int thread_count = atoi(argv[1]);
  
  //parallel exec of Hello() with thread_count threads
  #pragma omp parallel num_threads(thread_count)
   Hello();

  return 0; 
}//main

//////////////////////////////////
void Hello(void) 
{
  int my_rank = omp_get_thread_num();
  int thread_count = omp_get_num_threads();

  #pragma omp critical //protect cout statement as c.s.
   cout<<"Hello from thread_"<<my_rank<<" of "<<thread_count<<endl;
  
}//Hello
