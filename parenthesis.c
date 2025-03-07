#include<bits/stdc++.h>
using namespace std;

bool isValid(string s){
    stack<char> stk;

    int count = 0;
    for(int i=0;i<s.size();i++){
        if(s[i] == '(') count++;
        else if(s[i] == ')') count--;
    }
    return count == 0;
}

int main(){

    string s;
    cin >> s;

    cout << isValid(s);
}
