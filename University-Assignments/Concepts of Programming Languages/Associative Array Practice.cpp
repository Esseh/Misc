///----------------------------------------------------------------------------------------------------------
/// CSCI 117 - Prog4
///
/// Practice for Associative Arrays using std::vector and std::unordered_map
/// By Kenneth Willeford
/// Date- 10-9-15
///
/// The program takes in a list of data from an input file in the same directory "Prog4-data"
/// This file contains data such as...
/// Label1
/// ABCDEFGHIJK
/// Label2
/// CDEFGHIJKL
/// Label3
/// ABCDEFGHIJK
///
/// It will match our values the Labeln
/// With our sequences that act as our keys such as "ABCDEFGHIJK"
/// The reason being is this will associate Labels with the same data to the proper key.
///
/// This information will be saved in an output file named "Prog4-output"
/// This file will store the information in the way we want it to be associated.
///  Label1, Label3
/// ABCDEFGHIJK
/// Label2
/// CDEFGHIJKL
///
/// No command line arguments are needed, only to have the relevant input file declared.
///----------------------------------------------------------------------------------------------------------
#include<unordered_map>             //unordered_map Hash Table implementation.
#include<vector>                    //vector to act as our buckets.
#include<fstream>                   //ifstream,ofstream for file I/O
using namespace std;                //standard library

int main(){
    ifstream myFile("Prog4-data");                          //Grabs input file.
    ofstream outputFile("Prog4-output",ios::out);           //File to write output to.
    outputFile << flush;                                    //Clean file before writing.
///----------------------------------------------------------------------------------------------------------
///     Table Portion
///----------------------------------------------------------------------------------------------------------
    if(myFile.is_open()){
        unordered_map<string,vector<string> > hashTable;    //Initialize our hash table.
        while(!myFile.eof()){                               //While not the end of file...
            string key,value;                               //Grabs our keys (Biological Sequences) and values (Labels)
            myFile >> value; myFile >> key;                 //Because of our solution's semantics, grab value first then key.
            //If key doesn't exist yet make an entry with an empty bucket.
            if(hashTable.find(key) == hashTable.end()){
                //Make an entry of our key with an empty bucket.
                vector<string> tempVector;
                pair<string, vector<string> > tempPair(key,tempVector);
                hashTable.insert(tempPair);
            }
            auto index = hashTable.find(key);               //auto to infer type of iterator. Find entry related to key.
            (index->second).push_back(value);               //Push our labels into our bucket.
        }
        myFile.close();                                     //Close inputFile
///----------------------------------------------------------------------------------------------------------
///     File Printing Portion
///----------------------------------------------------------------------------------------------------------
        //Get start of hashTable and iterate through.
        for(auto i = hashTable.begin(); i != hashTable.end(); i++){
            //If first entry is empty advance iterator to first non_empty position.
            //Additionally if that advanced position is the end of the table then break out of the loop.
            if(i->first == ""){i++; if(i==hashTable.end()){break;}}
            for(int j = 0; j < (i->second).size(); j++){            //Iterate through Label Container
                outputFile << (i->second)[j];                       //Print to output a Label
                if(j < (i->second).size() - 1){outputFile << " , ";}//If not at end of container print a comma.
            }
            outputFile << endl << (i->first) << endl;               //After completing label printing, print the sequence and a newline.
                                                                    //There is a stray endl as unordered_map's iterator appears to only go in one direction.
                                                                    //But that's only on the last entry.
        }
        outputFile.close();                                         //Close output file.
    }
    return 0;                                                       //End Program.
}
