#include<bits/stdc++.h>
using namespace std;
const int maxN=1e5+5;

vector<pair<int, int> > g[maxN];
vector<pair<int, int> > edge;
int dists[maxN];
int distt[maxN];

int main(){

    int sum = 0;
    int n, m, s, t;
    cin >> n >> m >> s >> t;
    while(m--){
        int u, v, w;
        cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
        sum += w;
        edge.push_back({u, v});
    }

    for(int i=0;i<n;i++){
        dists[i] = 1e9;
        distt[i] = 1e9;
    }

    priority_queue<pair<int, int>> pq;
    pq.push({0, s});
    dists[s] = 0;
    while(!pq.empty()){
        int d_now = -pq.top().first;
        int u = pq.top().second;
        pq.pop();

        for(auto x: g[u]){
            int v = x.first;
            int w = x.second;

            if(dists[v] > dists[u] + w){
                dists[v] = dists[u] + w;
                pq.push({-dists[v], v});
            }
        }
    }

    pq.push({0, t});
    distt[t] = 0;
    while(!pq.empty()){
        int d_now = -pq.top().first;
        int u = pq.top().second;
        pq.pop();

        for(auto x: g[u]){
            int v = x.first;
            int w = x.second;

            if(distt[v] > distt[u] + w){
                distt[v] = distt[u] + w;
                pq.push({-distt[v], v});
            }
        }
    }

    int ans = 0;
    for(auto x: edge){
        int u = x.first;
        int v = x.second;

        ans = max(ans, sum - dists[u] - distt[v]);
        ans = max(ans, sum - dists[v] - distt[u]);
    }

    cout << ans;
}

