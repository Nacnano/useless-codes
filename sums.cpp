#include<bits/stdc++.h>
using namespace std;

int arr[10] = {3, 7, 2, 6, 3, 1, 8, 1, 6, 2};
map<int, int> mm;

int main(){
    int target = 13;
    for(int i=0;i<10;i++){
        if(mm.find(target - arr[i]) != mm.end()){
           cout << i << " " << mm[target - arr[i]];
           break;
        }
        mm[arr[i]] = i;
    }
}
