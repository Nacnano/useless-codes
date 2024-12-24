#include<bits/stdc++.h>
using namespace std;

int n;
int table[100];

int fibo_memo(int n) {
if (n == 1 || n == 0)
return n;
if (n >= 2) {
if (table[n] > 0) {
return table[n];
}
int value = fibo_memo(n-1) + fibo_memo(n-2);
table[n] = value;
return value;
}
}

int fibo[100];

int main(){

    cin >> n;

    fibo[0] = 0;
    fibo[1] = 1;

    for(int i=2;i<=n;i++){
        fibo[i]  = fibo[i-1] + fibo[i-2];
    }

    cout << fibo[n];
}
