/**GLOBAL DOCUMENTATION------------------------------------------------

Name:  Kenneth Willeford
Class: CSCI 117
Date:  9-13-15

    Interpreter for the Simplified-Infix-Arithmetic-Expression -- C++ Version
    $>gpp KennethWillefordProg1.cpp
    $>./KennethWillefordProg1 data_file_name.txt

    This program parses arithmetic through the following definitions.
            E  ->   T E'
            E' -> + T E'   | - T E' | ƒÃ
            T  ->   Ex T'
            T' -> * Ex T'  | / Ex T' | ƒÃ
            Ex ->   T Ex'
            Ex'-> ^ F Ex'  | ƒÃ
            F -> ( E ) E'  | Num
            Num a 0 | 1 | 2 | 3 | . . . | 9

    For additional documentation look at the functional representations of these definitions.
END GLOBAL DOCUMENTATION--------------------------------------------**/
///Legacy documentation will be commented as // the new documentation will have ///
///These comments should stick out in an IDE / Notepad++

//PREPROCESSING
#include<iostream>  //For printing to screen.
#include<fstream>   //File I/O.
#include<cmath>

//GLOBALS
int Exp(), Term(), Exp2(int), Term2(int), Fact(); //Prototypes, Documentation will above relevant functions.
std::ifstream myfile;   //File stream, in global scope to avoid reference passing.

//MAIN
int main(int argc, char *argv[])
{
    myfile.open(argv[1]); //Open file by command line argument.
    if(myfile.is_open()) std::cout << "result= " << Exp() << std::endl; //Run the program if the file exists.
    myfile.close(); //Close the file.
}
//FUNCTIONS

//Our Expression.
//The definition E -> T E'
//We will send out a left recursive Term as well as a converted right Recursive Expression E'
int Exp()
{
    //E -> T E'
    //Exp -> Term Exp2
    return Exp2(Term());
}

//Our Term
//The definition T -> F T'
//We will send out a left recursive factor and our converted right recursive Term T'
int Term()
{
    //T -> F T'
    //Term -> Fact Term2
    return Term2(Fact());
}

//Our Converted Right Recursive Expression
//The definition E' -> + T E' | - T E' |  e
//This allows us to compute our operations right recursively.
//As we recurse to the right we are ensuring that our operations decay into values of higher precendence.
//This handles + and - then passes it onto values that decay into * or / which in turn can decay into numerical assignment. (num)
int Exp2(int inp)
{
    int result = inp; char a;
    if ((a = myfile.get()) != myfile.eof()) //As long as we aren't at the end of the file, get the next character in the stream.
    {
        if(a=='+') result = Exp2(result+Term()); //Compute our expression as addition.
        else if(a=='-') result = Exp2(result - Term()); //Compute our expression as subtraction.
    }
    return result; //Send out our 'collapsed' result.
}

//Our Converted Right Recursive Term
//The definition T' -> * F T' | / F T' |  e
//Continuing from the previous function this is where * and / are handled.
int Term2(int inp)
{
    int result = inp; char a;
    if((a = myfile.get()) != myfile.eof()) //Get next character in stream
    {
        if(a=='^'){result = Term2(pow(result,Term()));}  ///It is already right recursive, and thus works for the assignment.
                                                         ///This was my initial answer and I noticed a glaring problem with
                                                         ///Precedence that was not caught in the test cases.
                                                         ///I'll document my frustrations with dealing with it at the bottom.
        else if(a=='*') result = Term2(result * Term()); //If multiplication calculate it.
        else if(a=='/') result = Term2(result / Term()); // if division calculate it.
        else if(a == '+' || a == '-' || a == ')') myfile.putback(a);  //Lower precedence so we put it back in stream to use later.
        ///Parenthesis is returned to the stream. Doing so causes the 'sub-expression' to be unable to parse further.
        ///As a result it will collapse into a single result.
    }
    return result; //Send out the collapsed term.
}

//Our Terminal Values
//F -> Num
//Simply put it reads from our file input stream and converts the character into a proper integer for our terminal.
int Fact()
{
    char a = myfile.get(); //Capture value in stream.
    if(a == '('){return Exp();} ///In order to have parenthesis defy precedence I had the language recurse on itself making a sub-expression.
                                ///In the future functions may be able to work like this as well. (Though I may port to Python to have Reflection help with that.)
    return a - '0'; //Conversion, because '0' is int(0) spaces away from 0 and ASCII is 0,1,..,9, we can just subtract '0' to get our int.
}

/**
    What I'm turning in is my first attempt. I had another attempt that was probably closer to the actual solution but I forgot to back it up.
    Note the structure up top:
            E  ->   T E'
            E' -> + T E'   | - T E' | ƒÃ
            T  ->   Ex T'
            T' -> * Ex T'  | / Ex T' | ƒÃ
            Ex ->   T Ex'
            Ex'-> ^ F Ex'  | ƒÃ
            F -> ( E ) E'  | Num
            Num a 0 | 1 | 2 | 3 | . . . | 9

    This was my ideal solution.
    What I'm submitting is.



            E  ->   T E'
            E' -> + T E'   | - T E' | ƒÃ
            T  ->   Ex T'
            T' -> ^ F T'  | * F T'  | / F T' | ƒÃ
            F -> ( E ) E'  | Num
            Num a 0 | 1 | 2 | 3 | . . . | 9

    The parenthesis is working exactly as intended but Exponentiation was the difficult part of the assignment.
    Our current structure is..
    Exp -> Exp'(Term)
    Term -> Term'(Fact)
    Fact -> Num or New Problem

    One of my intended structures was..

    Exp -> Exp'(Term)
    Term -> Term'(Ex)
    Ex -> Ex'(Fact)
    Fact -> Num or New Problem

    I was thinking that it would keep right associativity.
    However I ran into one of two problems.
    Either:
        A. Exponentiation would lose it's precedence.
        B. Exponentiation would lose it's right associativity.
    I was unable to "have my cake and eat it too."
    What I attempted were variations on the logic in that position.

    Another of my intended structures was..

    Exp -> Exp'()(Term)
    Term -> Term'(Ex(Fact))
    Fact -> Num or New Problem

    My thinking behind this was that because exponentiation was already right recursive we didn't need to transform it.
    It seems that I was right to a point. However I still ran into the same problem.
    """
    Either:
        A. Exponentiation would lose it's precedence.
        B. Exponentiation would lose it's right associativity.
    I was unable to "have my cake and eat it too."
    """
    Using what I learned I would revise my tree...

            E  ->   T E'
            E' -> + T E'     | - T E' | ƒÃ
            T  ->   Ex T'
            T' -> * Ex T'    | / Ex T' | ƒÃ
            Ex ->  ^ F Ex    | ƒÃ
            F  -> ( E ) E'   | Num
            Num a 0 | 1 | 2 | 3 | . . . | 9


    But for all my frustrations I can't seem to get it to work.
    So I submit to you it's original form because it is the most correct for the assignment,
    although I am personally disgruntled for my inability to have exponentiation behave the way it is
    supposed to behave.

**/
