#include<bits/stdc++.h>
using namespace std;

int n, k;
int used[100];
int sol[100];

void recur(int len){
    if(len==k){
        for(int i=0;i<k;i++){
            cout<<sol[i];
        }
        cout << endl;
        return;
    }
    for(int i=1;i<=n;i++){
        if(used[i]) continue;
        sol[len]=i;
        used[i]=true;
        recur(len+1);
        used[i]=false;
    }
}

int main(){
    cin >> n >> k;
    recur(0);

}
