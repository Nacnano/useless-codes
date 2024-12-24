#include<bits/stdc++.h>
using namespace std;

int n, k;
int arr[100];

int main(){

    cin >> n >> k;
    for(int i=0;i<n;i++) cin >> arr[i];

    int l = -1, r = n;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (k < arr[m]) {
            r = m; // a[l] <= k < a[m] <= a[r]
        } else {
            l = m; // a[l] <= a[m] <= k < a[r]
        }
        cout << r << " " << l << end;
    }

    cout << l;
}
