#include<bits/stdc++.h>
using namespace std;

int n;
int arr[100];

int main(){

    cin >> n;
    for(int i=0;i<n;i++) cin >> arr[i];

    // bubble sort
    for(int i=0;i<n;i++){
        for(int j=0;j<n-1;j++){
            if(arr[j] > arr[j+1]) swap(arr[j], arr[j+1]);
        }
    }

    for(int i=0;i<n;i++) cout << arr[i] << " ";
}
