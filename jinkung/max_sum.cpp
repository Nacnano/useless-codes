#include<bits/stdc++.h>
using namespace std;

int n;
int arr[100];
int qsum[100];

int main(){

    cin >> n;
    for(int i=0;i<n;i++) cin >> arr[i];

    qsum[0] = arr[0];
    for(int i=1;i<n;i++){
        qsum[i] = qsum[i-1] + arr[i];
    }


    // for(int i=0;i<n;i++)cout << qsum[i] << " ";

    int maxsum = -1e9;
    int ansi, ansj;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int sum = qsum[j] - qsum[i-1];
            if(sum > maxsum){
                maxsum = sum;
                ansi = i;
                ansj = j;
            }
        }
    }

    // cout << ansi << " " << ansj << " " << maxsum;

    int mss = arr[0], prev = arr[0];
    for(int i=1;i<n;i++){
        if(prev < 0){
            prev = arr[i];
        }
        else {
            prev += arr[i];
        }
        mss = max(mss, prev);
    }
    cout << mss;
}

