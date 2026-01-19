#include <string>
#include <iostream>
#include <stack>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    
    for (char c : s) {
        // Push opening brackets onto stack
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        }
        // Check closing brackets
        else if (c == ')' || c == ']' || c == '}') {
            // If stack is empty, no matching opening bracket
            if (st.empty()) {
                return false;
            }
            
            char top = st.top();
            st.pop();
            
            // Check if the closing bracket matches the opening bracket
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) {
                return false;
            }
        }
    }
    
    // Stack should be empty if all brackets are matched
    return st.empty();
}

int main() {
    cout << isValid("()") << endl;        // Output: 1 (true)
    cout << isValid("()[]{}") << endl;    // Output: 1 (true)
    cout << isValid("(]") << endl;        // Output: 0 (false)
    cout << isValid("([)]") << endl;      // Output: 0 (false)
    cout << isValid("{[]}") << endl;      // Output: 1 (true)
    
    return 0;
}