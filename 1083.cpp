#include<bits/stdc++.h>
using namespace std;

int price[1000005];
int dp[1000005];

int main(){
    ios_base::sync_with_stdio(false), cin.tie(NULL);

    int n, q;
    cin >> n;
    for(int i=1;i<=n;i++){
        cin >> price[i];
        dp[i] = dp[i-1] + max(0, price[i] - price[i-1]);
    }

    cin >> q;
    while(q--){
        int a, b;
        cin >> a >> b;
        cout << dp[b] - dp[a] << "\n";
    }
}


