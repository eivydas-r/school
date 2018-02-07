//cs141 lab4
//eivydas raulynaitis
//louis lee
//2/6/18

#include <iostream>
using namespace std;

int main(){
    int choice;
    cout << "Enter the length of the line: ";
    cin >> choice;
    
    for(int i=0; i < choice; ++i){
        cout << '*';
    }
    cout << endl;
    
    cout << "Enter the length of the side of the square: ";
    cin >> choice;
    for (int i = 0; i < choice; i++){
        for (int i = 0; i < choice; i++){
            cout << "*";
        }
        cout << endl;
    }
    
    cout << "Enter the height of the triangle: ";
    cin >> choice;
    for (int i = 1; i < choice; i++){
        for (int j = 0; j < i; j++){
            cout << "*";
        }
        cout << endl;
    }
    for (int i = choice; i > 0; i--){
        for (int j = 0; j < i; j++){
            cout << "*";
        }
        cout << endl;
    }
        
    return 0;
}
