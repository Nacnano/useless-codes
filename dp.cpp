#include<bits/stdc++.h>
using namespace std;

int a[1000005];
int dp[1000005]; // use first
int dp2[1000005]; // use second
int dp3[1000005]; // use third

int main(){
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        cin >> a[i];
    }

    dp[1] = a[1];
    dp[2] = a[1];
    dp[3] = a[1]+a[3];
    for(int i=4;i<=n;i++){
        dp[i] = max(dp[i-2], dp[i-3]) + a[i];
    }
    // use first value
    cout << dp[n-1];

    dp2[1] = 0;
    dp2[2] = a[2];
    dp2[3] = a[2];
    for(int i=4;i<=n;i++){
        dp2[i] = max(dp2[i-2], dp2[i-3]) + a[i];
    }
    // use second
    cout << dp2[n];

    // use third;
    cout << dp3[n];
}



