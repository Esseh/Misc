//////////////////////////////
//// Park -- this is a C++ version of the OpenMPP Hello program
//// Slightly different version to test the scope of each #pragma, i.e.,
//// the scope is within a block { }.
////
//// compile and run:
//// $> g++ -fopenmp -o xxx Park-omp-hello3.cpp
//// $>./xxx 4
////   //4 is the number of threads to use - any
//////////////////////////////

#include <cstdlib> //needed for atoi
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
  Hello(); //this is done in serial in the main process(thread)
  
  #pragma omp parallel num_threads(thread_count)
  { Hello();
    Hello();
  }//pragma omp parall - scope in a block { }
  
  #pragma omp parallel //num_threads(thread_count)
  { 
    #pragma omp critical
    { cout<<"111111\n";
      cout<<"222222\n";
    }
  }//pragma omp parall - scope in a block { }
    
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
