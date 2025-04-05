#include<bits/stdc++.h>
using namespace std;

int main(){
    unordered_map<int, int> mm;
    int target = 9;
    int arr[10] = {1, 2, 4, 7, 3, 1};

    for(int i=0;i<6;i++){
        if(mm.find(target-arr[i])!=mm.end()){
           cout << i << " " << mm[target-arr[i]];
           return 0;
        }
        mm[arr[i]] = i;
    }
    cout << "Not Found";
}
