#include <iostream>
#include <cstring> // For strcpy

using namespace std;

void flag(){
    cout << "FLAG{funnyFlag123}" << endl;
}

void vulnerable_function() {
    cout << "Please type your name: " << endl;
    char input[10];

    cin >> input;
    
    cout << "Hello: " << input << endl;
}

int main() {
    vulnerable_function(); 
    return 0;
}