/*---------------------------------------------------
 Author:  Eivydas Raulynaitis
 Class:   CS 141, Spring 2018
 Lab:     Tues 3pm
 Program: #3, Newton Game
 Xcode on a Mac
 
 
 Welcome to the game of Newton, where you try to be the first
 to get 5 in a row either vertically, horizontally or diagonally.
 Two players alternate making moves.  On each turn you may enter
 the column number where your piece will be placed, where that
 piece is inserted from the top and slides down as far as it can
 go in that column.  You may also enter 'r' to rotate a piece out
 of the bottom of a column to be dropped back in at the top of
 that column.  Enter 'x' to exit.
 ---------------------------------------------------*/

/*---------------------------------------------------
 erauly2Prog3.cpp
 
 Program #3: Newton game to get 5 in a row.
 Players alternate placing a piece or
 rotating a column.
 
 Class: CS 141
 Author: Eivydas Raulynaitis
 Lab: Tues 3pm
 System:  C++ Mac Xcode
 
 Grading Rubric:
 
 50 Execution points
 2 Displays header info and instructions on screen when run
 5 Move number and character-to-move update correctly
 3 Handles upper and lower-case user input, spaces between inputs, and 'X' to exit
 5 Does error checking of user input for valid input and space in column
 10 Handles 'R' to rotate a column
 10 Correctly places pieces on board
 15 Detects a win of 5 in a row, and gives the corresponding ending message
 
 45 Programming Style (Given only if program runs substantially correctly)
 5 Program naming convention is followed
 10 Meaningful identifier names
 10 Comments: Has header and this rubric.  Has comments on each block of code
 10 Appropriate data and control structures
 10 Code Layout: Appropriate indentation and blank lines
 --------------------------------------------------*/

#include <iostream>
#include <vector>
using namespace std;

/*
 Why using global vectors was necessary for this program:
 Using global vectors was necessary for this program because the whole program is based off of 5 separate
 vectors, which make up the board of the game. Localizing these vectors wouldn't be beneficial for the
 organization of the program's code, because the vectors would have to be referenced in the parameters for every
 function of the program, making the code less clean, harder to work with, and to understand.
 Therefore, I believe using global vectors was a necessary component of this program.
*/
vector<char> first{'.','.','.','.','.','.','.','.'}; //declare first column vector
vector<char> second{'.','.','.','.','.','.','.','.'}; //declare second column vector
vector<char> third{'.','.','.','.','.','.','.','.'}; //declare third column vector
vector<char> fourth{'.','.','.','.','.','.','.','.'}; //declare fourth column vector
vector<char> fifth{'.','.','.','.','.','.','.','.'}; //declare fifth column vector


void display(){ //function that displays the board, no return
    cout << endl;
    cout << " 1   2   3   4   5" << endl <<
    "--- --- --- --- ---" << endl <<
    " " << first.at(7) << "   " << second.at(7) << "   " << third.at(7) << "   " << fourth.at(7) << "   " << fifth.at(7) << endl <<
    " " << first.at(6) << "   " << second.at(6) << "   " << third.at(6) << "   " << fourth.at(6) << "   " << fifth.at(6) << endl <<
    " " << first.at(5) << "   " << second.at(5) << "   " << third.at(5) << "   " << fourth.at(5) << "   " << fifth.at(5) << endl <<
    " " << first.at(4) << "   " << second.at(4) << "   " << third.at(4) << "   " << fourth.at(4) << "   " << fifth.at(4) << endl <<
    " " << first.at(3) << "   " << second.at(3) << "   " << third.at(3) << "   " << fourth.at(3) << "   " << fifth.at(3) << endl <<
    " " << first.at(2) << "   " << second.at(2) << "   " << third.at(2) << "   " << fourth.at(2) << "   " << fifth.at(2) << endl <<
    " " << first.at(1) << "   " << second.at(1) << "   " << third.at(1) << "   " << fourth.at(1) << "   " << fifth.at(1) << endl <<
    " " << first.at(0) << "   " << second.at(0) << "   " << third.at(0) << "   " << fourth.at(0) << "   " << fifth.at(0) << endl <<
    "--- --- --- --- ---" << endl <<
    " 1   2   3   4   5" << endl;
}


bool selectVector(vector<char>& chosenVector, char type){ //references the vector, uses type of piece, returns true or false based if empty/full, allows to edit the vector, adds a piece to column if not full
    for (int i = 0; i < 8; i++){ //for every piece in column (is 8 so there's no error)
        if (chosenVector.at(7) != '.' && i==7){ //if last piece isn't empty, give error and retry
            cout << endl << "*** Sorry, that column is already full.  Please choose another." << endl;
            return false; //tell it failed
        } else if (chosenVector.at(i) == '.'){
            chosenVector.at(i) = type;
            return true; //tell it succeeded
            break; //break when success
        }
    }
    return false; //tell it failed (default)
}


bool addPiece(int column, char type){ //function that'll add a piece to selected column, using parameter column and piece type, returns true or false based on if the piece was added correctly
    switch (column) { //for every possible column
        case 1:
            return selectVector(first, type); //check first column, add a piece if not full
            break;
        case 2:
            return selectVector(second, type); //check second column, add a piece if not full
            break;
        case 3:
            return selectVector(third, type); //check third column, add a piece if not full
            break;
        case 4:
            return selectVector(fourth, type); //check fourth column, add a piece if not full
            break;
        case 5:
            return selectVector(fifth, type); //check fifth column, add a piece if not full
            break;
        default: //if not a possible column, error and retry
            cout << endl << "*** Invalid input. Please retry..." << endl;
            return false; //tell main that piece wasn't added
            break;
    }
    return false; //tell main that piece wasn't added (default)
}


void rotateColumn(vector<char>& chosenVector){ //rotate selected column, parameter is the selected vector, no return
    int i = 0; //start counter
    char temp = chosenVector.at(0); //make temporary var for first piece
    
    while (i < 7 && chosenVector.at(i+1) != '.'){ //loop until reaching top of pieces
        chosenVector.at(i) = chosenVector.at(i+1); //move pieces down
        i++; //add counter
    }
    chosenVector.at(i) = temp; //change final piece to first piece
}


void checkColumn(vector<char>& chosenVector, char& winner){ //check chosen column for 5 in a row of X or O, pass winner to parameter winner, no return
    int streak = 1; //see how many repetitions of a piece
    
    for (int i = 0; i < 7; i++){ //for every piece in column
        if (chosenVector.at(i) == chosenVector.at(i+1) && chosenVector.at(i) != '.'){ //add to streak if the same piece
            streak++;
        } else { //restart streak if not same
            streak = 1;
        }
        if (streak >= 5){ //if streak is 5 or more, then that piece is a winner
            winner = chosenVector.at(i);
            break; //break loop if winner found
        }
    }
}


bool checkForWinner(){ //check combinations for 5 in a row horizontally, vertically, or diagonally
    char winner = ' '; //no winner until not ' '
    
    for (int i = 7; i >= 0; i--){ //check rows for winner, starting from the top
        if (first.at(i) == second.at(i) && second.at(i) == third.at(i) && third.at(i) == fourth.at(i) && fourth.at(i) == fifth.at(i) ){ //check that whole row is the same piece
            if (fifth.at(i) == 'X'){ //if row is all X, then X wins
                winner = 'X';
            } else if (fifth.at(i) == 'O'){ //if row is all O, then O wins
                winner = 'O';
            }
        }
    }
    
    //all columns, starting from the left
    checkColumn(first, winner); //check first column for winner
    checkColumn(second, winner); //check second column for winner
    checkColumn(third, winner); //check third column for winner
    checkColumn(fourth, winner); //check fourth column for winner
    checkColumn(fifth, winner); //check fifth column for winner
    
    for (int i = 7; i > 4; i--){ //upper-left to lower-right diagonals, starting from upper left corner
        if (first.at(i) != '.' && first.at(i) == second.at(i-1) && second.at(i-1) == third.at(i-2) && third.at(i-2) == fourth.at(i-3) && fourth.at(i-3) == fifth.at(i-4)){ //check all in diagonal are equal
            winner = first.at(i); //award the win to piece
            break;
        }
    }
    
    for (int i = 3; i >= 0; i--){ //lower-left to upper-right diagonals, starting from the middle on the left side.
        if (first.at(i) != '.' && first.at(i) == second.at(i+1) && second.at(i+1) == third.at(i+2) && third.at(i+2) == fourth.at(i+3) && fourth.at(i+3) == fifth.at(i+4)){ //check all in diagonal are equal
            winner = first.at(i); //award the win to piece
            break;
        }
    }
    
    if (winner != ' '){ //if there's a winner
        if (winner == 'X'){ //if the winner is X
            cout << "X wins! Good game!" << endl;
            return true;
        } else if (winner == 'O'){ //if the winner is O
            cout << "O wins! Good game!" << endl;
            return true;
        }
    }
    return false; //if no matches, no wins
}


int main(){ //main function of program that'll run everything, default main return is 0
    bool win = false; //for the while loop at bottom
    int turn = 1; //count the turns in game
    char choice; //the input the player gives
    char type = 'X'; //whos turn it currectly is
    
    cout << "Author:  Eivydas Raulynaitis" << endl << //header info
    "Class:   CS 141, Spring 2018" << endl <<
    "Lab:     Tues 3pm" << endl <<
    "Program: #3, Newton Game" << endl <<
    "Xcode on a Mac" << endl << endl << endl << 
    "Welcome to the game of Newton, where you try to be the first " << //header directions
    "to get 5 in a row either vertically, horizontally or diagonally. " <<
    "Two players alternate making moves. On each turn you may enter " <<
    "the column number where your piece will be placed, where that " <<
    "piece is inserted from the top and slides down as far as it can " <<
    "go in that column. You may also enter 'r' to rotate a piece out " <<
    "of the bottom of a column to be dropped back in at the top of " <<
    "that column. Enter 'x' to exit." << endl << endl;
    
    display(); //initial display
    
    while (!win){ //while the game isn't over
        //type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
        
        cout << turn << ". Enter column number to place " << type << " or 'r' to rotate: "; //ask for input
        cin >> choice; //get input
        
        if (tolower(choice) == 'r') { //for r or R, if 'r', allow another input, run rotate function
            cin >> choice; //get second input
            int column = (int)choice-48; //convert into number
            
            switch(column){ //check for every column number
                case 1: //rotate first column
                    rotateColumn(first);
                    turn++;
                    type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                    display();
                    break;
                case 2: //rotate second column
                    rotateColumn(second);
                    turn++;
                    type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                    display();
                    break;
                case 3: //rotate third column
                    rotateColumn(third);
                    turn++;
                    type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                    display();
                    break;
                case 4: //rotate fourth column
                    rotateColumn(fourth);
                    turn++;
                    type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                    display();
                    break;
                case 5: //rotate fifth column
                    rotateColumn(fifth);
                    turn++;
                    type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                    display();
                    break;
                default: //if not a possible column, error and retry
                    cout << endl << "*** Invalid input. Please retry..." << endl;
                    continue;
            }
        } else if (tolower(choice) == 'x'){ //for x and X
            cout << "Exiting program..." << endl; break; //exit the program if 'x'
        } else { //if input is just a column number
            int column = (int)choice-48; //convert into number
            
            switch(column){ //check for every column number, default if out of range
                case 1: //add piece to 1, 2, and so on, no breaks because it leads to same function for 1-5
                case 2:
                case 3:
                case 4:
                case 5:
                    if (addPiece(column, type)){ //if piece is added
                        type = (type == 'X')? 'O' : 'X'; //switch piece types every turn
                        turn++; //add a turn
                        display(); //show board
                    }
                    break;
                default: //if not a possible column, error and retry
                    cout << endl << "*** Invalid input. Please retry..." << endl;
                    continue;
            }
        }
        if (checkForWinner()){ //checks for winning combinations
            win = true; //if true, make win true, end win while loop, therefore end game
        }
    }
    return 0;
}



