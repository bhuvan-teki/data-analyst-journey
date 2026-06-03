// ==========================================
// C++ DSA - Day 1 Fundamentals
// ==========================================
#include <iostream>
#include <string>

using namespace std;

int main() {
    
    // --------------------------------------
    // 1. Basic Output
    // --------------------------------------
    cout << "Hello World" << endl;
    cout << "Hello World" << "\n" << "hi" << endl;

    // --------------------------------------
    // 2. Data Types & Variables
    // --------------------------------------
    cout << "\n--- Arithmetic Operations ---" << endl;
    
    // Integer operations
    int a, b;
    // cin >> a >> b;
    // cout << (a + b) * 10 << endl;
    
    // Float operations
    float f1, f2;
    // cin >> f1 >> f2;
    // cout << f1 + f2 << endl;
    
    // Long types
    long long l1, l2;
    // cin >> l1 >> l2;
    // cout << l1 + l2 << endl;

    // Character data-type
    char ch = '-';
    cout << ch << endl;

    // --------------------------------------
    // 3. String Inputs
    // --------------------------------------
    cout << "\n--- String Inputs ---" << endl;
    
    // Standard input (reads until the first space)
    string s1, s2;
    // cin >> s1 >> s2;
    // cout << s1 << endl << s2 << endl;
    
    // Getline (reads the entire line including spaces)
    string s;
    // getline(cin, s);
    // cout << s << endl;

    // --------------------------------------
    // 4. Conditional Statements (If-Else)
    // --------------------------------------
    cout << "\n--- If-Else Conditions ---" << endl;
    
    // Dhoni runs in IPL finals
    int runs = 105; // Example hardcoded value for testing
    // cin >> runs; 
    
    if (runs >= 100) {
        cout << "Scored Century" << endl;  
    } 
    else if (runs >= 50) {
        cout << "Scored Half Century" << endl;
    } 
    else {
        cout << "Scored below Half Century" << endl;
    }

    // --------------------------------------
    // 5. Switch Case Statement
    // --------------------------------------
    cout << "\n--- Switch Cases ---" << endl;
    
    int month = 6; // Example hardcoded value for testing
    // cin >> month;
    
    switch(month) {
        case 1: cout << "jan" << endl; break;
        case 2: cout << "feb" << endl; break;
        case 3: cout << "march" << endl; break;
        case 4: cout << "apr" << endl; break;
        case 5: cout << "may" << endl; break;
        case 6: cout << "june" << endl; break;
        case 7: cout << "july" << endl; break;
        case 8: cout << "aug" << endl; break;
        case 9: cout << "sep" << endl; break;
        case 10: cout << "oct" << endl; break;
        case 11: cout << "nov" << endl; break;
        case 12: cout << "dec" << endl; break;
        default: cout << "Not valid Number" << endl;
    }

    return 0;
}
