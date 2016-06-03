/*  Mark and Sweep Garbage Collection Simulation
//  By Kenneth Willeford
//  This program imitates the mark and sweep style garbage collection found in many languages.
//  To see details of the algorithm refer to documentation.
//  Of note this isn't a 'true' garbage collector and may actually have some
//  Dangling pointer leaks, but the 'simulation' should still be correct.
//
//  I took an object oriented approach towards implementing this and from working on this simulation
//  I have determined the following.
//  I'm sure by utilizing some overloaded keywords I could implement an actual pseudo garbage collector
//  Though I still have to consider how I would parse for it in an interpreter so my knowledge is not complete at this time.
*/
#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;

struct memoryCell{
    int id;                         //The ID of a Memory Cell
    int key;                        //The Key assigned when using the element.
    int next;                       //The Memory Cell value of the 'next' reference.
    int mark;                       //The Marked state for mark/sweep.
    memoryCell(){
        mark = 0;
        key = -2;
    };
};
struct list{
    memoryCell*data;                //Reference to memoryCell
    list*next;                      //Recursive Reference(Linked List)
    list(memoryCell* element){      //Constructor for connecting cell to list.
        data = element;
    };
};
struct runtime{
    vector<memoryCell*>heap;        //Container for Memory Cells
    list*H1;                        //List 1
    list*H2;                        //List 2
    list*Free;                      //Our Free List
    runtime(){                      //Our constructor.
        H1 = NULL;                              //Initialize List 1 to Empty
        H2 = NULL;                              //Initialize List 2 to Empty
        for(int i = 0; i <=8; i++){             //Construct Heap Through Iteration.
            heap.push_back(new memoryCell());
            heap[heap.size()-1]->id = i;
            heap[heap.size()-1]->next = i+1;
        }
        heap.push_back(new memoryCell());       //Place Last Heap Value explicitly.
        heap[heap.size()-1]->id = 9;
        heap[heap.size()-1]->next = -2;
        //EXPLICIT INITIALIZATION OF FREELIST.
        Free = new list(heap[0]);
        Free->next = new list(heap[1]);
        Free->next->next = new list(heap[2]);
        Free->next->next->next = new list(heap[3]);
        Free->next->next->next->next = new list(heap[4]);
        Free->next->next->next->next->next = new list(heap[5]);
        Free->next->next->next->next->next->next = new list(heap[6]);
        Free->next->next->next->next->next->next->next = new list(heap[7]);
        Free->next->next->next->next->next->next->next->next = new list(heap[8]);
        Free->next->next->next->next->next->next->next->next->next = new list(heap[9]);
    }
    list*pop(list*&target){                      //Given a list it returns the front most element.
        if(target==NULL){return NULL;}          //If List is Empty return NULL.
        list*temp = target;                     //Grab the target.

        target = target->next;                  //Advance the head of the list.
        temp->next = NULL;                       //Clear references on result.
        temp->data->next = -2;                  //Clear any symbolic references.
        temp->data->mark = 0;                   //Reset Mark Status
        return temp;                            //Send out the result.
    };

    void insert(list*&target,int k){
        list*templist = pop(Free);                  //Pop the front out of the freelist.
        if(templist==NULL){                         //Break the program if 'out of memory'
            cout << "Out of Memory" << endl;
            exit(1);
        }
        templist->data->key = k;                    //Set key for new value.
        //If Empty list just make the newlist.
        if(target == NULL){target = templist; target->next = NULL; return;}
        //If the first entry is bigger. Then place myself in front.
        if(templist->data->key <= target->data->key){
            templist->next = target;          //Make myself known as the front of the list.
            templist->data->next = target->data->id; //Match symbolic reference.
            target = templist;          //Move reference to front of list.
            return;
        }
        //If Other Place inbetween two value.
        list*traverse = target;                     //Start Traversal
        while(traverse->next!=NULL){
            //If an inbetween value is found. Put it there.
            if(templist->data->key >= traverse->data->key && templist->data->key <= traverse->next->data->key){
                templist->data->next = traverse->next->data->id;            //Match Symbolic Reference
                templist->next = traverse->next;                            //Match Actual Reference
                traverse->data->next = templist->data->id;                  //Match Symbolic Reference
                traverse->next = templist;                                  //Match Actual Reference.
                return;
            }
            traverse = traverse->next;              //Advance Traversal
        }
        //If search is exhausted. Place at end.
        traverse->next = templist;                      //Place at end.
        traverse->next->data->next = templist->data->id;  //Resolve symbolic references.
        templist->data->next = -2; // Set tail symbolic reference to symbolic null.
    };
    void print_memory(){
        for(int i = 0; i < heap.size(); i++){   //Print IDS:
            cout << heap[i]->id + 1 << "\t";
        }
        cout << endl;
        for(int i = 0; i < heap.size(); i++){   //Print Keys
            if(heap[i]->key == -2){cout << "\t"; } else {cout << heap[i]->key << "\t";}
        }
        cout << endl;
        for(int i = 0; i < heap.size(); i++){   //Print Nexts
            cout << heap[i]->next + 1 << "\t";
        }
        cout << endl;
        for(int i = 0; i < heap.size(); i++){   //Print Marks
            cout << heap[i]->mark << "\t";
        }
        cout << endl;
        if(H1==NULL){cout << "H1: -1" << endl;}
        else{cout << "H1: " << H1->data->id+1 << endl;}
        if(H2==NULL){cout << "H2: -1" << endl;}
        else{cout << "H2: " << H2->data->id+1 << endl;}
        if(Free==NULL){cout << "Free: -1" << endl;}
        else{cout << "Free: " << Free->data->id+1 << endl;}
    }
    void Delete(list*&target,int k){
        if(target == NULL){return;}     //If target is empty just go back.
        if(target->data->key == k){
            target = target->next;      //If our goal is on the front simply advance pointer.
                                        //No need to change ID as it has stayed the same.
            return;
        }

        list*traverser = target->next;        //Traverse the list.
        list*slow = target;

        while(traverser != NULL){
            if(slow->next->data->key == k){
                slow->next = slow->next->next;
                if(slow->next == NULL){slow->data->next = -2;}        //If Only NULL remains resolve reference.
                else{slow->data->next = slow->next->data->id;}       //Otherwise form symbolic reference.
            }
            slow = traverser;              //Advance One Step Behind
            traverser = traverser->next;    //Advance Pointer
        }
        //Search Failed, Do Nothing
    }
    //The garbage collector that utilizes the mark sweep algorithm.
    //Check Mark and Sweep for specific documentation.
    void garbage_collect(){
        mark();
        sweep();
    }
    //Mark will search each list and mark each memory cell it can access with a '1'.
    void mark(){
        for(list*traverser=H1;traverser!=NULL;traverser=traverser->next){           //Mark all accessible nodes in list 1.
            traverser->data->mark = 1;
        }
        for(list*traverser=H1;traverser!=NULL;traverser=traverser->next){           //Mark all accessible nodes in list 2.
            traverser->data->mark = 1;
        }
		for(list*traverser=Free;traverser!=NULL;traverser=traverser->next){
			traverser->data->mark = 1;
		}
    }
    //Any nodes that cannot be accessed(cannot be marked) will be returned to the free list with their relative order restored in memory.
    void sweep(){
        for(int i = 0; i<heap.size(); i++){         //Search Through the Heap
            if(heap[i]->mark == 1){heap[i]->mark = 0;}          //If marked just switch the mark back.
            //Otherwise move into free list.
            else{
                list*temp = new list(heap[i]);                  //Make new node for free list.
                temp->next = Free;                              //Make the next position of the new node the front of the free list.
                Free = temp;                                    //Make the new node officially the front of the free list.
            }
        }
    }
};

int main(){
    runtime *environment = new runtime();       //Construct 'runtime environment' simulation.
    string input;                               //User input.
    int inp;                                    //Integer Input
        cout << "Type ? for help." << endl;
    while(true){
    //Give the User Instructions.

    cin >> input;                                       //Get Input
            if(input == "?"){
        cout << "0 - Insert to List 1" << endl;
        cout << "1 - Insert to List 2" << endl;
        cout << "2 - Delete from List 1" << endl;
        cout << "3 - Delete from List 2" << endl;
        cout << "4 - Print Memory" << endl;
        cout << "5 - Run Garbage Collector" << endl;
        cout << "6 - Exit Program" << endl;}
    if(input == "0"){                                   //Insert to List 1
            cout << "Input Integer to Insert" << endl;
            cin >> inp;
            environment->insert(environment->H1,inp);
    }
    if(input == "1"){
            cout << "Input Integer to Insert" << endl;  //Insert to List 2
            cin >> inp;
            environment->insert(environment->H2,inp);
    }
    if(input == "2"){                                   //Delete from List 1
            cout << "Input Integer to Delete" << endl;
            cin >> inp;
            environment->Delete(environment->H1,inp);
    }
    if(input == "3"){                                   //Delete from List 2
            cout << "Input Integer to Delete" << endl;
            cin >> inp;
            environment->Delete(environment->H2,inp);
    }
    if(input == "4"){environment->print_memory();}      //Print Memory
    if(input == "5"){environment->garbage_collect();}   //Run Garbage Collector
    if(input == "6"){return 0;}                         //End Program
    }
}
