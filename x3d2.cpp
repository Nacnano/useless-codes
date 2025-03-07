#include<bits/stdc++.h>
using namespace std;

bool check[100000000];



int main(){
    int x;
    cin >> x;

    list<int> l;

    l.insert(10);z

    queue<pair<int, string> > q;
    q.push({1, "1"});
    while(!q.empty()){
        int value = q.front().first;
        string s = q.front().second;
        q.pop();
        if(check[value] == true) continue;
        check[value] = 1;

        cout << value << " " << s << endl;
        if(value == x) break;

        q.push({value / 2, s + " / 2"});
        q.push({value * 3, s + " * 3"});
    }

}
