Here is a detailed breakdown of the boilerplate and data types based on the code snippets you learned today. You can add this section directly into your notes to make the fundamental concepts crystal clear.

---

## 1. The C++ Boilerplate Explained

A "boilerplate" refers to the essential block of code required at the beginning of almost every C++ program to make it run.

```cpp
#include<bits/stdc++.h> // OR #include <iostream>
using namespace std;

int main() {
    // Your code goes here
    return 0;
}

```

* **`#include <iostream>`**: This is a header file that includes the standard Input/Output stream library. It allows you to use `cin` (to take input) and `cout` (to print output).
* **`#include<bits/stdc++.h>`**: You used this in your switch-case snippet. This is a special header file widely used in competitive programming and DSA. It automatically includes *all* standard C++ libraries at once (like `<iostream>`, `<string>`, `<vector>`, etc.), saving you the time of including them individually.
* **`using namespace std;`**: The C++ standard library (`std`) contains built-in functions. If you don't use this line, you have to write `std::cout` and `std::endl` every time. This line tells the compiler to use the standard namespace by default.
* **`int main()`**: This is the main execution function. Whenever a C++ program runs, the compiler looks for this `main()` function and starts executing the code inside its curly braces `{}`.
* **`return 0;`**: This signals to the operating system that the program has executed successfully without any errors (returning a `0` exit code).

---

## 2. C++ Data Types Explained

C++ is a strongly-typed language, meaning you must declare the type of data a variable will hold before assigning a value to it.

### `int` (Integer)

Used to store whole numbers (without fractions or decimals) like `1`, `-50`, or `1000`. It typically takes up 4 bytes of memory and can store numbers up to roughly 2 billion (`2 * 10^9`).

```cpp
int a;
int b;
cin >> a >> b;
cout << (a + b) * 10 << endl;

```

### `long` and `long long` (Large Integers)

When you are doing DSA or competitive programming, sometimes calculations result in numbers larger than 2 billion (e.g., calculating factorial or large sums). An `int` will overflow and give a garbage value.

* **`long`**: Typically takes 4 or 8 bytes depending on the system.
* **`long long`**: Guarantees at least 8 bytes of memory, safely storing massive numbers up to roughly `9 * 10^18`.

```cpp
long long a;
long long b;
cin >> a >> b;
cout << a + b << endl;

```

### `float` (Floating Point)

Used to store numbers with a fractional or decimal component (e.g., `3.14`, `-0.5`).

```cpp
float a;
float b;
cin >> a >> b;
cout << a + b << endl;

```

### `char` (Character)

Used to store a **single** character, such as a letter, number, or symbol. In C++, `char` values must always be enclosed in single quotes (`' '`).

```cpp
// characters data-type
char a = '-';
cout << a << endl;

```

### `string` (Text)

A string is a sequence of characters used to store text. Unlike `char`, string values must be enclosed in double quotes (`" "`).

Your code highlights a critical rule about taking string inputs in C++:

**Method 1: Using `cin**`
`cin` considers a space (whitespace) as a terminating character. It only reads single words.

```cpp
string s1;
string s2;
cin >> s1 >> s2; // If input is "Data Analytics", s1 gets "Data", s2 gets "Analytics"
cout << s1 << endl << s2 << endl;

```

**Method 2: Using `getline()**`
If you want to read an entire sentence including the spaces, you must use `getline()`.

```cpp
string s;
getline (cin, s); // If input is "Hello World from C++", it captures the whole sentence.
cout << s << endl;

Here is the structured markdown file. I have broken down the code you learned today into logical sections, explaining *what* the code does and *why* it works. This will serve as an excellent revision guide for your repository.

You can copy and paste this directly into your **`DSA CPP/Notes/C++ Basics Part - 1.md`** file.

---

```markdown
# C++ Basics Part - 1

This document contains my study notes and explanations for the fundamental C++ concepts I learned on Day 1 of my Data Structures and Algorithms (DSA) preparation.

---

## 1. Boilerplate & Basic Output

Every C++ program requires a basic structure (boilerplate) to run. 

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World" << endl;
    return 0;
}

```

* **`#include <iostream>`**: This is a header file library that allows us to work with input and output objects, such as `cout` and `cin`.
* **`using namespace std;`**: This tells the compiler to use the standard namespace, meaning we don't have to write `std::cout` every time.
* **`cout`**: Used to output (print) text to the console.
* **`endl`**: Ends the current line and moves the cursor to the next line (similar to `\n`).

---

## 2. Variables & Data Types

C++ requires you to declare the type of data a variable will hold before you use it.

```cpp
int main() {
    // Integer: Stores whole numbers
    int a, b;
    cin >> a >> b;
    cout << (a + b) * 10 << endl;

    // Float: Stores fractional numbers
    float f1, f2;

    // Long Long: Stores very large integers
    long long l1, l2;

    // Char: Stores a single character inside single quotes
    char symbol = '-';
    cout << symbol << endl;
    
    return 0;
}

```

* **`cin`**: Takes input from the user.
* We can perform direct arithmetic operations (like `+`, `*`) inside the `cout` statement.

---

## 3. String Inputs

Handling text in C++ behaves differently depending on whether you want a single word or an entire sentence.

```cpp
#include <iostream>
#include <string> // Required for string operations
using namespace std;

int main() {
    // Method 1: Standard cin
    string s1, s2;
    cin >> s1 >> s2; 
    // Note: 'cin' stops reading as soon as it hits a space. 
    
    // Method 2: Getline
    string s;
    getline(cin, s);
    // Note: 'getline' reads the entire line of text, including spaces, until the user presses Enter.
    
    return 0;
}

```

---

## 4. Conditional Statements (If-Else)

`if-else` statements allow the program to make decisions based on conditions. The program checks conditions from top to bottom and executes the first one that evaluates to `true`.

```cpp
int main() {
    int runs;
    cin >> runs;
    
    if(runs >= 100) {
        cout << "Scored Century" << endl;  
    } 
    else if (runs >= 50) {
        cout << "Scored Half Century" << endl;
    } 
    else {
        cout << "Scored below Half Century" << endl;
    }
    
    return 0;
}

```

* **`if`**: The first condition checked.
* **`else if`**: Checked only if the first `if` is false.
* **`else`**: The default fallback if all previous conditions are false.

---

## 5. Switch Case Statements

A `switch` statement is used to execute one block of code out of many based on exact matching values. It is often cleaner than writing multiple `else if` statements.

```cpp
int main() {
    int n;
    cin >> n;
    
    switch(n) {
        case 1:
            cout << "jan";
            break;
        case 2:
            cout << "feb";
            break;
        // ... cases 3 to 11 omitted for brevity ...
        case 12:
            cout << "dec";
            break;
        default:
            cout << "Not valid Number";
    }
    
    return 0;
}

```

* **`case`**: Represents a specific value to match against `n`.
* **`break`**: Crucial! It stops the execution of the switch block. If you forget `break`, the program will continue executing the code in the cases below it.
* **`default`**: Runs if none of the `case` values match (similar to `else`).

---

## 🎯 Purpose

These notes are part of my **Data Analyst & DSA Journey** repository where I document my learning progress, logic implementation, and technical growth.

## 👨‍💻 Repository Owner

**Bhuvan Teki**

* **GitHub:** https://github.com/bhuvan-teki/
* **LinkedIn:** https://www.linkedin.com/in/bhuvanteki/
