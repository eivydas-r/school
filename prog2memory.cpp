/*---------------------------------------------------------
 Author:  Eivydas Raulynaitis
 Class:   CS 141, Spring 2018
 Lab:     Tues 3pm
 Program: #2, Memory Game
 
 Welcome to the memory game!
 
 Look away from the board and have a helper enter r
 to randomize the board until they have a random board
 that they like.  Then you glance at it and try to
 imprint it in your mind and look away.  Your helper
 will then select a single piece to be flipped by
 choosing its row and column.  The changed board is then
 displayed. You then must try to guess which one it was.
 Enter x to exit the program.
 ---------------------------------------------------------*/

/*--------------------------------------------------------------------------------------------
 prog2memory.cpp
 
 Program #2: Memory game of guessing which X or O changed.
 Class: CS 141
 Author: Eivydas Raulynaitis
 Lab: Tues 3pm
 System:  C++ Mac Xcode
 
 Grading Rubric:
 
 50 Execution points
 5 Displays header info on screen when run
 5 Displays instructions
 5 Output is formatted as shown in sample output
 3 Handles both upper and lower case input
 2 Input of 'x' in first prompt exits program
 5 Input can be adjacent or have spaces between them
 15 Displayed boards all have odd parity in rows and columns
 5 Repeated input of 'r' gives new valid random board each time
 5 Gives appropriate end of program messages
 
 45 Programming Style (Given only if program runs substantially correctly)
 5 Program naming convention is followed
 10 Meaningful identifier names
 10 Comments: Has header.  Comments on each block of code
 10 Appropriate data and control structures (-20 if using arrays or strings)
 10 Code Layout: Appropriate indentation and blank lines
--------------------------------------------------------------------------------------------*/

#include <iostream>
#include <cstdlib>

using namespace std;

char p0, p1, p2, p3, p4, p5, //initialize variables
p6, p7, p8, p9, p10,p11,
p12,p13,p14,p15,p16,p17,
p18,p19,p20,p21,p22,p23,
p24,p25,p26,p27,p28,p29,
p30,p31,p32,p33,p34,p35;

void display(){ //display the updated board, no return
    cout << endl << "       1 2 3 4 5 6" << endl;
    cout << "     - - - - - - - -" << endl;
    cout << "   A | " << p0 << " " << p1 << " " << p2 << " " << p3 << " " << p4 << " "
         << p5 << " | A" << endl;
    cout << "   B | " << p6 << " " << p7 << " " << p8 << " " << p9 << " " << p10 << " "
         << p11 << " | B" << endl;
    cout << "   C | " << p12 << " " << p13 << " " << p14 << " " << p15 << " " << p16 << " " << p17
         << " | C" << endl;
    cout << "   D | " << p18 << " " << p19 << " " << p20 << " " << p21 << " " << p22 << " " << p23
         << " | D" << endl;
    cout << "   E | " << p24 << " " << p25 << " " << p26 << " " << p27 << " " << p28 << " " << p29
         << " | E" << endl;
    cout << "   F | " << p30 << " " << p31 << " " << p32 << " " << p33 << " " << p34 << " " << p35
         << " | F" << endl;
    cout << "     - - - - - - - -" << endl << endl;
}


bool randomize(char& p){ //randomize a single variable using modulus, returns true or false based on if X or O
    if (rand() % 2 == 1){
        p = 'X';
        return true;
    } else {
        p = 'O';
        return false;
    }
}


char paritize(char dep, char ind1, char ind2, char ind3, char ind4, char ind5){ //apply odd parity for the inputted variables, dep being the dependent variable based on the parity of the rest, return dependent variable
    int num = 0;
    if (ind1 == 'X'){
        num++;
    }
    if (ind2 == 'X'){
        num++;
    }
    if (ind3 == 'X'){
        num++;
    }
    if (ind4 == 'X'){
        num++;
    }
    if (ind5 == 'X'){
        num++;
    }
    if (num % 2 == 0){
        dep = 'X';
    } else{
        dep = 'O';
    }
    return dep;
}


void randomizeBoard(){ //randomize every variable and apply odd parity, no return
    randomize(p0);
    randomize(p1);
    randomize(p2);
    randomize(p3);
    randomize(p4);
    randomize(p5);
    randomize(p6);
    randomize(p7);
    randomize(p8);
    randomize(p9);
    randomize(p10);
    randomize(p11);
    randomize(p12);
    randomize(p13);
    randomize(p14);
    randomize(p15);
    randomize(p16);
    randomize(p17);
    randomize(p18);
    randomize(p19);
    randomize(p20);
    randomize(p21);
    randomize(p22);
    randomize(p23);
    randomize(p24);
    randomize(p25);
    randomize(p26);
    randomize(p27);
    randomize(p28);
    randomize(p29);
    randomize(p30);
    randomize(p31);
    randomize(p32);
    randomize(p33);
    randomize(p34);
    randomize(p35);

    p6 = paritize(p6, p7, p8, p9, p10, p11); //do parity for rows
    p12 = paritize(p12, p13, p14, p15, p16, p17);
    p18 = paritize(p18, p19, p20, p21, p22, p23);
    p24 = paritize(p24, p25, p26, p27, p28, p29);
    p30 = paritize(p30, p31, p32, p33, p34, p35);

    p0 = paritize(p0, p6, p12, p18, p24, p30); //do parity for columns
    p1 = paritize(p1, p7, p13, p19, p25, p31);
    p2 = paritize(p2, p8, p14, p20, p26, p32);
    p3 = paritize(p3, p9, p15, p21, p27, p33);
    p4 = paritize(p4, p10, p16, p22, p28, p34);
    p5 = paritize(p5, p11, p17, p23, p29, p35);
}


void change(char& var){ //change variable from X to O or to X, no return
    if (var == 'X'){
        var = 'O';
    } else{
        var = 'X';
    }
}


void guess(bool& gameEnd, char selection1, char selection2){ //allow a guess, decide if correct, end game, no return
    char choice1;
    char choice2;
    
    cout << "What piece do you think it was? -> "; //ask for guess
    cin >> choice1;
    cin >> choice2;
    selection1 = toupper(selection1);
    
    if (toupper(choice1) == selection1){ //check is correct, decide ending
        if (tolower(choice2) == selection2){
            cout << endl << "*** Congratulations, you did it! ***" << endl << endl << "Thank you for playing.  Exiting..." << endl;
            gameEnd = true;
        } else{
            cout << endl << "Sorry, it was " << selection1 << selection2 << ". Better luck next time." << endl << endl << "Thank you for playing.  Exiting... " << endl;
            gameEnd = true;
        }
    } else{
        cout << endl << "Sorry, it was " << selection1 << selection2 << ". Better luck next time." << endl << endl << "Thank you for playing.  Exiting... " << endl;
        gameEnd = true;
    }
}


void process(char& choice2, char& var1, char& var2, char& var3, char& var4, char& var5, char& var6){ //process the selections correctly based on the given parameters of the board, selecting the correct tile, no return
    choice:
    cin >> choice2;
    switch (choice2) {
        case '1':
            change(var1);
            break;
        case '2':
            change(var2);
            break;
        case '3':
            change(var3);
            break;
        case '4':
            change(var4);
            break;
        case '5':
            change(var5);
            break;
        case '6':
            change(var6);
            break;
        default:
            cout << endl << "Sorry, that's not a valid input, try again -> ";
            goto choice; //allow user to retry
            break;
    }
    for (int i = 0; i < 25; i++){
        cout << endl;
    }
    display();
}


int main(){
    srand(static_cast<unsigned int>(time(0))); //random seed
    
    bool gameEnd = false; //if true, game ends
    char choice1;
    char choice2;
    
    cout << "Author:  Eivydas Raulynaitis" << endl << "Class:   CS 141, Spring 2018" << endl << "Lab:     Tues 3pm" << endl << "Program: #2, Memory Game" << endl << endl << "Welcome to the memory game!" << endl << endl << "Look away from the board and have a helper enter r to randomize the board until they have a random board that they like. Then you glance at it and try to imprint it in your mind and look away. Your helper will then select a single piece to be flipped by choosing its row and column. The changed board is then displayed. You then must try to guess which one it was. Enter x to exit the program." << endl << endl << endl;
    
    randomizeBoard();
    display();
    
    cout << "Enter r to randomize to board, or row and column to change a value -> ";
    
    while (!gameEnd){ //while game isn't over
        cin >> choice1;
        choice1 = tolower(choice1);
        switch (choice1) { //switch statement for possible inputs
            case 'r': //randomize the board and clear the screen
                for (int i = 0; i < 25; i++){
                    cout << endl;
                }
                randomizeBoard();
                display();
                
                cout << "Enter r to randomize to board, or row and column to change a value -> ";
                break;
            case 'x': //exit the program
                cout << "Exiting program..." << endl;
                gameEnd = true;
                break;
            case 'a': //if choice is in A row
                process(choice2, p0, p1, p2, p3, p4, p5);
                guess(gameEnd, choice1, choice2);
                break;
            case 'b': //if choice is in B row
                process(choice2, p6, p7, p8, p9, p10, p11);
                guess(gameEnd, choice1, choice2);
                break;
            case 'c': //if choice is in C row
                process(choice2, p12, p13, p14, p15, p16, p17);
                guess(gameEnd, choice1, choice2);
                break;
            case 'd': //if choice is in D row
                process(choice2, p18, p19, p20, p21, p22, p23);
                guess(gameEnd, choice1, choice2);
                break;
            case 'e': //if choice is in E row
                process(choice2, p24, p25, p26, p27, p28, p29);
                guess(gameEnd, choice1, choice2);
                break;
            case 'f': //if choice is in F row
                process(choice2, p30, p31, p32, p33, p34, p35);
                guess(gameEnd, choice1, choice2);
                break;
            default: //invalid choice, let retry
                cout << endl << "Sorry, that's not a valid input, try again -> ";
                break;
        }
    }
    return 0;
}
