//--------------------------------------------------------------------------------
//Kenneth Willeford
//3/17/2015
//
//The MIT License (MIT)
//
//Copyright (c) 2015 Kenneth Willeford
//
//Permission is hereby granted, free of charge, to any person obtaining a copy
//of this software and associated documentation files (the "Software"), to deal
//in the Software without restriction, including without limitation the rights
//to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//copies of the Software, and to permit persons to whom the Software is
//furnished to do so, subject to the following conditions:
//
//The above copyright notice and this permission notice shall be included in all
//copies or substantial portions of the Software.
//
//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
//SOFTWARE.
//
//The purpose of this was to provide an invariant to the binary search tree such
//that I can print between nodes in a minimum number amount of traversals as well
//as find a kth minimum element as effeciently as possible.
//
//It should be noted that this isn't the fastest possible implementation.
//Like most data structures retrieval speed can be increased with caching.
//I will list my implementation cost but I will also list the cost assuming
//caching of a minimum and maximum value.
//
//The invariant I chose is that every node in the tree will know its successor and
//predecessor.
//This adds transitivity between these nodes such that
//Node A -> Node B  and Node B -> C, as such this implies that from Node A you can reach Node C
//which you can through B.
//
//This invariant is maintained through the insert function.(And if applicable delete.)
//The idea is that when a new node is inserted it can find it's successor and predecessor. (Both LogN Complexity.)
//A symmetrical connection is then formed.
//This ensures that any given node is always pointing to its relative predecessor and successor.
//
//Delete is normally a LogN action that relies on a LogN search and then a LogN search for the successor.(If it isn't a mid node / leaf.)
//But because the information is cached it can skip this step, this comes at the cost of maintaining the invariant afterward though.
//
//Likewise insert becomes a bit more expensive.
//It begins with a LogN find, then with the invariant a LogN predecessor action, a LogN successor action (each with their own LogN actions.)
//While technically this is still a LogN action it should be noted that 5LogN actions are occuring overall so it is a substantial difference in constant.
//You can shave off 2LogN by caching min and max respectively.
//
//The implemented version of k'th smallest is a Log(N)+K action however this can be
//reduced simply to a O(K) complexity operation by caching the minimum value.
//
//The Print_From_To has a worst case time complexity of O(N).
//The invariant makes sure that the data is able to be accessed sequentially so we don't need to access any excess nodes.
//
//
//This specific invariant in addition to what it was intended to be implemented for gives the BST
//a decent range query, Although it still has to find the first node before it can return the range.
//--------------------------------------------------------------------------------
#include<iostream>
using namespace std;
#include"bst.h"


//Special Node to Make Used of the Additional Invariant for the Binary Search Tree
//The nodes in addition to knowing the normal information of a BST node will also know it's predecessor and successor.
class node
{
        public:   //Public only for convienence of current implementation.
        int data; //Element in the Node
        node*left; //Left pointer.
        node*right; //Right pointer.
        node*parent; //Parent Pointer

        node(int el){data = el; left = NULL; right = NULL; parent = NULL; successor = NULL; predecessor = NULL;}//Constructor;

        node*successor;  //Invariant Pointer to Successor.
        node*predecessor;//Invariant Pointer to Predecessor.

};

//This implementation of bst makes the assumption that a given node knows it's successor/predecessor.
//A node with a null predecessor is said to be it's own predecessor.
//A node with a null successor is said to be it's own successor.

template<typename node_type> class bst: public binary_search_tree<node_type>
{
    public:                                                                 //Public only for convienence of current implementation.
    node_type*top;                                                          //Top of the tree
    bst()                                                                   //Base Constructor
    {
        top=NULL;
    };
    //Begin Required Methods
    //Inserts an Element into the BST.
    //This is where the magic happens and the invariant is maintained through the helper functions.
    //Due to the nature of the implementation it will be trivial to maintain it with deletion as well.
    //Delete and Insert will be more costly but only by a constant factor, asymptotically they should be the same.
    void insert(int element)
    {
        node_type*newnode = new node_type(element); //Construct Node
        if(top==NULL) //Top is NULL simply make the node the top and exit.
        {
            top = newnode; //Set head to be the new node.
            return; //Exit.
        }
        else
        {
            push(newnode,top); //Push it onto the tree.
        }
    };
    //Finds the kth smallest element and returns it from the BST.
    //It is a LogN operation to find the smallest element,
    //with the invariant in place it will only take an additional k-1 actions to find the kth smallest value.
    int kth_smallest(int k)
    {
        if(top==NULL || k<1){return 0;} //Nothing to find, return 0.
        node_type *temp = top; //Create Temp Value
        while(temp->left != NULL){temp = temp->left;} //Find Minimum Value
        while(k>1 && temp->successor != NULL){temp = temp->successor; k--;} //Find kth Minimum value. or the maximum value if improper input for k.
        return temp->data; //Return the minimum value.
    };

    //Prints all nodes in order from pointer "from" to pointer "to", also lists the nodes traversed.
    //This will demonstrate the invariant at work and only traverse "from - to" nodes.
    void print_from_to(node_type *from, node_type *to)
    {
        if((to->data < from->data ) || top==NULL || from == NULL){cout << "0 Nodes Traversed." << endl; return;}//Cannot Print, Return.
        node_type *temp = from;//Place Iterator
        int increment = 0;//Set Incrementor
        while(temp!=to)//Iterate until we have reached to.
        {
            cout << temp->data << " "; //Print out the data.
            temp = temp->successor;    //Iterate through successors.
            increment ++;              //Add to Incrementor.
        }
        cout << temp->data << endl;    //Print final value.
        increment++;                   //Increment One Last Time
        cout <<  increment << " nodes traversed." << endl; //Print amount of nodes traversed.
    };
    //End Required Methods

    //Begin Helper Methods
    //Recursively determines where to place the node as per protocol and once it finds the correct spot and inserts it will force the invariant on the inserted node.
    void push(node_type*input,node_type*current)
    {
        if(input->data <= current->data) //If Less than or Equal to Go left of the tree.
        {
            if(current->left==NULL)
            {
                current->left = input;
                input->parent = current;
                invariant(input);
                return;
            } //Insert in position then enforce invariant..
            else{push(input,current->left); return;} //Traverse Tree.
        }
        else //Otherwise go right of the tree.
        {
            if(current->right==NULL)
            {
                current->right = input;
                input->parent = current;
                invariant(input);
                return;
            } //Insert in position then enforce invariant..
            else{push(input,current->right); return;} //Traverse Tree
        }
    }
    //Enforces the Invariant so that the inserted node knows its predecessor and successor and also enforces the changes for all nodes changed.
    void invariant(node_type*input)
    {
        input->successor = nextInOrder(input); //Find next in order and set it as successor.
        input->predecessor = prevInOrder(input); //Find prev in order and set it as predecessor.
        if(input->successor!=NULL){input->successor->predecessor = input;} //Maintain connected node's invariant.
        if(input->predecessor!=NULL){input->predecessor->successor = input;} //Maintain connected node's invariant.
    }
    //Finds the successor node.
    node_type*nextInOrder(node_type*input)
    {

        node_type*temp = top; //Create traverser.
        while(temp->right!=NULL){temp = temp->right;}//Check Max
        if(temp == input){return NULL;} //It's max, return NULL

        temp = input; //Traverser
        if(input->right!=NULL){temp=temp->right; while(temp->left!=NULL){temp=temp->left;} return temp;} //If right isn't null find the minimum.
        else //Otherwise find successor in ancestor.
        {
            node_type *temp_par = temp->parent;
            while(temp_par != NULL && temp==temp_par->right)
            {
                temp = temp_par;
                temp_par = temp_par->parent;
            }
        return temp_par; //Send out successor in ancestor.
        }
    }
    //Finds the predecessor node.
    node_type*prevInOrder(node_type*input)
    {
        node_type*temp = top; //Create traverser.
        while(temp->left!=NULL){temp = temp->left;}//Check Min
        if(temp == input){return NULL;} //It's min, return NULL
        temp = input;
        if(temp->left!=NULL){temp = temp->left; while(temp->right!=NULL){temp=temp->right;}return temp;} //Go left then find maximum.
        else //Otherwise find predecessor in ancestor.
        {
            node_type *temp_par = temp->parent;
            while(temp_par != NULL && temp==temp_par->left)
            {
                temp = temp_par;
                temp_par = temp_par->parent;
            }
        return temp_par;
        }
    }
    //End Helper Methods
};

int main()
{
    bst<node> *test = new bst<node>();
    //Testing the Insertion
    test->insert(5);
    test->insert(4);
    test->insert(6);
    test->insert(8);
    test->insert(7);
    test->insert(337);
        node*input = test->top->left;
        while(input!=NULL){
        if(input->successor != NULL){cout << input->data <<"'s successor is " << input->successor->data << endl;}
        if(input->predecessor != NULL){cout << input->data <<"'s predecessor is " << input->predecessor->data << endl;}
        input = input->successor;}
    //AHA! They're aligned correctly. And it's not the 'nicest' tree either. The invariant is holding.
    //Now let's try finding kth smallest!
    cout << "kth smallest 0:" << test->kth_smallest(0) << endl; //Should return 0.
    cout << "kth smallest 1:" << test->kth_smallest(1) << endl; //Should return 4
    cout << "kth smallest 2:" << test->kth_smallest(2) << endl; //should return 5
    cout << "kth smallest 999:" << test->kth_smallest(999) << endl; //Should return 337
    //Working!
    //Now let's test out the print from to
    cout << endl;
    cout << "Failed Print" << endl;
    test->print_from_to(test->top->right->right->right,test->top->left); //printing backwards makes no sense although the implementation allows it, so this will print nothing.
    cout << endl;
    cout << "Successful Print" << endl;
    test->print_from_to(test->top->left,test->top->right->right->right); //Given the shape of the tree this should print the entire tree.
    //And it works!
}
