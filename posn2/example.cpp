#include<bits/stdc++.h>
using namespace std;

long long arr[100];

int main(){
    ios_base::sync_with_stdio(0), cin.tie(NULL);

    int m, n;
    cin >> m >> n;
    for(int i=0;i<m;i++){
        cin >> arr[i];
    }

    long long l = 1, r = 1e12;
    while(r - l > 0){
        // Time
        long long mid = (l + r + 1) / 2;
        // Quantity
        long long q = 0;
        for(int i=0;i<m;i++){
            q += mid/arr[i];
        }
        cout << l << " " << r << " " << q << endl;

        if(q > n){
            r = mid;
        }
        else {
            l = mid;
        }
    }

    cout << l;

    return 0;
}
