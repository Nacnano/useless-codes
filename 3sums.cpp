#include<bits/stdc++.h>
using namespace std;

int arr[10] = {3, 7, 2, 6, 3, 1, 8, 1, 6, 2};

int main(){
    sort(arr, arr+10);

    int target = 13;
    for(int i=0;i<8;i++){
        int j = i+1, k = 9;
        while(j<9 && j<k){
            int current_sum = arr[i]+arr[j]+arr[k];
            if(current_sum > target) {
                k--;
            }
            else if (current_sum < target) {
                j++;
            }
            else {
                cout << arr[i] << " " << arr[j] << " " << arr[k];
                return 0;
            }
        }
    }
}
