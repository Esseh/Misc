#ifndef bin
#define bin

template<typename node_type> class binary_search_tree
{
    public:
    virtual void insert(int element) = 0; //Inserts an Element into the BST.
    virtual int kth_smallest(int k) = 0;  //Finds the kth smallest element and returns it from the BST.
    virtual void print_from_to(node_type *from, node_type *to) = 0; //Prints all nodes in order from pointer "from" to pointer "to", also lists the nodes traversed.
};


#endif // bst
//END CODE

