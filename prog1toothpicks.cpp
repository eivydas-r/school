/*--------------------------------------------------------------------------------------------
 prog1toothpicks.cpp
 
 Program #1: Toothpicks: Puzzle to equalize the number of toothpicks in three stacks.
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
 5 Input can be adjacent or have spaces between them
 15 Makes moves correctly
 10 Handles the specified error conditions
 2 Gives appropriate end of program messages
 
 50 Programming Style (Given only if program runs substantially correctly)
 5 Program naming convention is followed
 10 Meaningful identifier names
 10 Comments: Has header.  Comments on each block of code
 10 Appropriate data and control structures
 10 Code Layout: Appropriate indentation and blank lines
 --------------------------------------------------------------------------------------------*/

#include <iostream>
using namespace std;

int trial = 1;

void display(int num1,int num2,int num3) {
    cout << "Stack:\t\t\t\t\tA\tB\tC" << endl;
    cout << "Number of toothpicks:\t" << "\t" << num1 << "\t" << num2 << "\t" << num3 << endl;
}

int add(int stack, int input1, int input2) {
    int result;
    if (input1 > input2) {
        input2 += input2;
        result = input2;
    } else {
        cout << "There's not enough toothpicks, try again." << endl << endl;
        result = stack;
    }
    return result;
}

int subtract(int stack, int input1, int input2) {
    int result;
    if (input2 < input1) {
        input1 -= input2;
        trial++;
    }
    result = input1;
    return result;
}


int main() { //correct combo: ab -- bc -- ca --- 11 7 6 -- 4 14 6 -- 4 8 12 -- 8 8 8
    char choice1;
    char choice2;
    int stack1 = 11;
    int stack2 = 7;
    int stack3 = 6;
    int *current1;
    int current2;
    
    cout << "Program #1: Toothpicks" << endl << "Class: CS 141" << endl << "Author: Eivydas Raulynaitis" << endl << "Lab: Tues 3pm" << endl << "System:  C++ Mac Xcode" << endl << endl;
    
    cout << "Welcome to the Toothpick Puzzle, where the goal is to get an equal number of toothpicks in each stack, in three moves." << endl << endl;
    
    display(stack1, stack2, stack3);
    
    cout << endl << "A move consists of moving toothpicks from one stack to a second stack, where the number of toothpicks moved is exactly the number that is in the destination stack.  In other words, to move from stack B (7 toothpicks) to stack C (6) as shown above, we would move 6 from B to C, leaving us with 1 in B and 12 in stack C." << endl << endl;
    
    cout << "Here we go... " << endl << endl;
    
    while (trial <= 3) {
        current1 = NULL;
        current2 = NULL;
        
        display(stack1,stack2,stack3);
        
        cout << endl << trial << ". " << "Enter FROM and TO stack letters: ";
        cin >> choice1;
        cin >> choice2;
        
        switch(choice1){
            case 'a':
                current1 = &stack1;
                break;
            case 'A':
                current1 = &stack1;
                break;
            case 'b':
                current1 = &stack2;
                break;
            case 'B':
                current1 = &stack2;
                break;
            case 'c':
                current1 = &stack3;
                break;
            case 'C':
                current1 = &stack3;
                break;
            default:
                cout << "Sorry, " << choice1 << " isn't a valid entry. Try again." << endl << endl;
                continue;
                break;
        }
        if (choice1 != choice2) {
            switch(choice2){
                case 'a':
                    current2 = stack1;
                    stack1 = add(stack1, *current1, current2);
                    *current1 = subtract(stack1, *current1, current2);
                    
                    break;
                case 'A':
                    current2 = stack1;
                    stack1 = add(stack1, *current1, current2);
                    *current1 = subtract(stack1, *current1, current2);
                    break;
                case 'b':
                    current2 = stack2;
                    stack2 = add(stack2, *current1, current2);
                    *current1 = subtract(stack2, *current1, current2);
                    
                    break;
                case 'B':
                    current2 = stack2;
                    stack2 = add(stack2, *current1, current2);
                    *current1 = subtract(stack2, *current1, current2);
                    break;
                case 'c':
                    current2 = stack3;
                    stack3 = add(stack3, *current1, current2);
                    *current1 = subtract(stack3, *current1, current2);
                    break;
                case 'C':
                    current2 = stack3;
                    stack3 = add(stack3, *current1, current2);
                    *current1 = subtract(stack3, *current1, current2);
                    break;
                default:
                    cout << "Sorry, " << choice2 << " isn't a valid entry. Try again." << endl << endl;
                    continue;
                    break;
                    
            }
        } else {
            cout << "Sorry, you can't break the laws of logic, try again." << endl << endl;
            current1 = 0;
            current2 = 0;
        }
    }
    display(stack1,stack2,stack3);
    
    if (stack1 == stack2 && stack2 == stack3) {
        cout << endl << "Congratulations! You did it! Great job!" << endl << endl;
    } else {
        cout << endl << "Nope, sorry, that's not it. Try again." << endl << endl;
    }
}
