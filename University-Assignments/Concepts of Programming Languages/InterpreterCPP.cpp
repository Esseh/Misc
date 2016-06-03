//C++ Implementation of the Python Interpreter

#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <sstream>

using namespace std;

///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///BEGIN
///--------------------------------
class variable
{
    public:
        char id;
        string type;
        string value;
        variable(char a, string b, string c){id = a; type = b; value = c;}
};
///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///END
///--------------------------------

int Exp(), Term(), Exp2(int), Term2(int), Fact(), Pwr(), stoi(string);
bool validVarName(char), validType(string), varDeclared(char);
variable &accessVar(char);
string itos(int);
void output_statement(), input_statement(), assignment_statement(char),isInt(char),statement(),declaration(),idList(string),prog();
///-------------------------------------------------------------------------
///PREVIOUS LAB
///-------------------------------------------------------------------------
std::ifstream inputFile;
///-------------------------------------------------------------------------
///END PREVIOUS LAB
///-------------------------------------------------------------------------
///Needed because TA's Math is fat and eats too much.
stringstream expressionStream;



vector<variable> v_table;


int main(int argc, char* argv[])
{
///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///BEGIN
///--------------------------------
    ///Build Vtable in One Pass
    for(int i = 0; i < 26; i++){v_table.push_back(variable(i+65,"None","None"));}
    for(int i = 0; i < 26; i++){v_table.push_back(variable(i+97,"None","None"));}
///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///END
///--------------------------------

    std::string fileName = "input4.txt";
    inputFile.open(fileName);
    if(!inputFile.is_open())
    {
        std::cerr << "Unable to open file " << fileName << std::endl;
    }

    prog(); //Run program.

}

///--------------------------------
/// <Prog> ::= program <Declarations> begin <Statements> end
///BEGIN
///--------------------------------
void prog()
{
    string first_word; //Grab First word.
    inputFile >> first_word;
    if(first_word!="program"){cout << "Expected 'program'" << endl; exit(1);}
    declaration(); //Run declarations.
    statement(); //Run statements.
}

///--------------------------------
/// <Prog> ::= program <Declarations> begin <Statements> end
///END
///--------------------------------


///--------------------------------
/// Doing them separately is tricky because streams can be a bit buggy.
/// <Declarations> ::= <Declaration> | <Declaration> <Declarations>
/// <Declaration> ::= var <Id-list> ; | É√
///BEGIN
///--------------------------------
void declaration()
{
    string word; //Grab word.
    inputFile >> word;
    if(word == "begin"){return;} //If done.. End!
    else if(validType(word)){idList(word);} //Run ID List if it's a valid type.
    declaration();
}
///--------------------------------
/// Doing them separately is tricky because streams can be a bit buggy.
/// <Declarations> ::= <Declaration> | <Declaration> <Declarations>
/// <Declaration> ::= var <Id-list> ; | É√
///END
///--------------------------------

///--------------------------------
/// <Id-list> ::= <Id> | <Id> , <Id-list>
///BEGIN
///--------------------------------
void idList(string type)
{
    char letter;
    inputFile >> letter; //Grab letter.
    if(letter == ','){idList(type); return;} //Comma, keep going.
    else if(letter == ';'){return;} //Semicolon, end recursion.
    else if(validVarName(letter)){ //Check if valid variable name, take appropriate action then recurse.
        accessVar(letter).type = type;
    idList(type); //Recurse.
    }
}

///--------------------------------
/// <Id-list> ::= <Id> | <Id> , <Id-list>
///END
///--------------------------------

///--------------------------------
///<Statement> ::= <Assign-St> | <Input-St> | <Output-St> THIS IS ALSO STATEMENTS, They had to be combined because streams are stupid.
///BEGIN
///--------------------------------
void statement()
{
    string word;
    inputFile >> word; //Grab Word

    if(word == "end"){return;}
    else if(word.size() == 1) //Assume I just grabbed a variable.
    {
        char letter;
        inputFile >> letter; //Grab letter.
        if(letter == '='){assignment_statement(word[0]);} //Assignment Statement
        else{cout << "Invalid Statement" << endl; exit(1);} //Invalid Statement
    }
    else if(word == "input"){input_statement();}  //Input Statement
    else if(word == "output"){output_statement();}//Output Statement
    else{cout << "Invalid Statement" << endl; exit(1);} //Not in our language, invalid statement.
    statement();
}
///--------------------------------
///<Statement> ::= <Assign-St> | <Input-St> | <Output-St>
///END
///--------------------------------

///--------------------------------
///<Assign-St> ::= <Id> = <Exp> ;
///BEGIN
///--------------------------------
void assignment_statement(char id)
{
    varDeclared(id);
    //Check if we can actually store numbers in this thing.
    if(accessVar(id).type != "var"){cout << "Type Mismatch" << endl; exit(1);}
    //TA's code eats stuff!
    string tempWord;
    inputFile >> tempWord; //Grab 'Word' (Expression Block)
    if((tempWord[0]+0 >= 48 && tempWord[0]+0 <= 57) || tempWord[0] == '('){}else{cout << "Not an Expression" << endl;; exit(1);}//Check if Expression by assuming it is if the first value is 1..9 or (
    expressionStream.clear();//clear any bits set
    expressionStream.str(std::string()); //Empty stream.
    expressionStream.str(tempWord); //Set expressionStream's buffer to the expression block.
    int temp = Exp(); //Compute expression.
    ///NOTE: replace inputFile with expressionStream in math!
    accessVar(id).value = itos(temp);  //Set variable to our value.
}
///--------------------------------
///<Assign-St> ::= <Id> = <Exp> ;
///END
///--------------------------------


///--------------------------------
/// <Input-St> ::= input <Id> ;
///BEGIN
///--------------------------------
void input_statement()
{
    char var,semicolon;
    inputFile >> var; //Grab variable.
    inputFile >> semicolon; //Grab semicolon.
    varDeclared(var); //Check if variable is declared.
    validVarName(var); //Check if valid variable name.
    if(semicolon != ';'){cout << "Expected ';'" << endl; exit(1);} //Error is missing semicolon.
    cin >> accessVar(var).value; //Input
    if(accessVar(var).type == "var"){isInt(var);} //If var(int) check if it's really int.
}

//Checks if value is an integer.
bool isInt(char var)
{
    //Compare value to it's string converted to int converted back to string.
    if(accessVar(var).value == itos(stoi(accessVar(var).value))){return true;}
    else cout << "Type Mismatch" << endl; exit(1);
}

//Converts string to integer.
int stoi(string input)
{
    int result = 0;
    for(int i = 0; i < input.size(); i++)
    {
        result+=(input[i]-48);
        result*=10;
    }
    result/=10;
    return result;
}

//Converts integer to string.
string itos(int input)
{
    string result = "";
    while(input > 0)
    {
        result.push_back((input%10)+48);
        input/=10;
    }
    string result2;
    for(int i = result.size()-1; i >= 0; i--){result2.push_back(result[i]);}
    return result2;
}
///--------------------------------
/// <Input-St> ::= input <Id> ;
///END
///--------------------------------

///--------------------------------
/// <Output-St> ::= output <Id> ; | output <Exp> ;
///BEGIN
///--------------------------------
void output_statement()
{
    char var,semicolon;
    inputFile >> var;       //Grab var or first part of expression.
    if(var == '(' || (var+0 >= 48 && var+0 <= 57))
    {
        inputFile.putback(var); //Put letter back.
        string tempWord; //Get as word instead.
        inputFile >> tempWord;
        expressionStream.clear();//clear any bits set
        expressionStream.str(std::string()); //Empty stream.
        expressionStream.str(tempWord); //Set expressionStream's buffer to the expression block.
        cout << Exp() << endl;
        return;
    }// If first part of expression, put value back and assume.
    varDeclared(var); //Standard variable checks if variable.
    validVarName(var);
    inputFile >> semicolon; //Grab semicolon if variable.
    if(semicolon != ';'){cout << "Expected ';'" << endl; exit(1);}
    cout << accessVar(var).value << endl;
}
///--------------------------------
/// <Output-St> ::= output <Id> ; | output <Exp> ;
///END
///--------------------------------


///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///BEGIN
///--------------------------------

//Accesses variable in constant time.
variable &accessVar(char input)
{
    if(validVarName(input)) //If name is valid rest should be fine.
    {
        if(input+0 <= 90){return v_table[input-65];} //Offset from Uppercase
        return v_table[input-71]; //Offset from Lowercase
    }
}

//Checks if an id has been declared or not.
bool varDeclared(char input)
{
    if(accessVar(input).type != "None"){return true;}
    cout << "Variable Has Not Been Declared" << endl; exit(1);
}

//Checks if an id is a valid variable name.
bool validVarName(char input)
{
    //It is in ascii range, return true.
    if((input + 0 >= 65 && input + 0 <= 90) || (input + 0 >= 97 && input + 0 <= 122)){return true;}
    cout << "Invalid Variable ID" << endl; exit(1);
}

//Checks if an id is a valid type name.
bool validType(string input)
{
    //var is only valid type in current language. (Same as int.)
    if(input == "var"){return true;}
    cout << "Invalid Variable Type" << endl; exit(1);
}

///--------------------------------
///<ID> ::= a|b|c|...|z|A|B|C|...|Z
///END
///--------------------------------

///-------------------------------------------------------------------------
///PREVIOUS LAB
///-------------------------------------------------------------------------
int Exp()
{
    return Exp2(Term());
}

int Term()
{
    return Term2(Pwr());
}

int Exp2(int inp)
{
    int result = inp;
    char a;
    if(expressionStream >> a)
    {
        if(a == '+')
        {
            result = Exp2(result + Term());
        }
        else if(a == '-')
        {
            result = Exp2(result - Term());
        }
        else if(a == ')')
            expressionStream.putback(a);
    }

    return result;
}

int Term2(int inp)
{
    int result = inp;
    char a;
    if(expressionStream >> a)
    {
        if (a == '*')
            result = Term2(result * Pwr());
        else if (a == '/')
            result = Term2(result / Pwr());
        else if (a == '+' || a == '-' || a == ')')
            expressionStream.putback(a);
    }

    return result;
}

int Pwr() {
    int p = Fact();
    char a;

    if (expressionStream >> a) {
        if (a == '^') {
            p = pow(p, Pwr());
        }
        if (a == '+' || a == '-' || a == '*' || a == '/' || a == ')')
            expressionStream.putback(a);
    }
    return p;
}


int Fact(){
    char a;
    expressionStream.get(a);
    if (a == '('){
        int exp = Exp();
        expressionStream >> a;
        if (a == ')'){
            return exp;
        }
    }
    return (a - '0');
}
///-------------------------------------------------------------------------
///END PREVIOUS LAB
///-------------------------------------------------------------------------