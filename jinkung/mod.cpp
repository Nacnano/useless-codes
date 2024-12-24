#include<bits/stdc++.h>
using namespace std;

int a, n, k;

int main(){
    int ans;
    cin >> a >> n >> k;
    int l = 1;
    for(int i=0;i<n;i++){
        l*=a;
        l = l%k;
    }
    ans=l%k;
    cout<<ans;
}
