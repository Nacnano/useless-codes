#include<bits/stdc++.h>
using namespace std;

const int maxN = 100005;

vector<int> levels[maxN];
vector<int> g[maxN];

bool vis[maxN];
int current_time = 0;

bool dfs(int u){
    vis[u] = 2;
    current_time++;
    for(auto v: g[u]){
        if(vis[v] == 2) return false;
        if(vis[v] == 1) continue;
        dfs(v);
    }
    return true;
}

int main(){

    int n, k, t;
    cin >> n >> k >> t;
    for(int i=1;i<=n;i++){
        int level, p;
        cin >> level >> p;
        levels[level].push_back(i);
        while(p--){
            int x;
            cin >> x;
            g[i].push_back(x);
        }
    }

    for(int i=1;i<=k;i++){
        for(auto u: levels[i]){
            if(vis[u]) continue;
            int success = dfs(u);
        }

        for(int something) vis[u] = 1;

        if(!sucess) cout << "-1";

        if(current_time > t){
            cout << i-1;
            break;
        }
    }

}

