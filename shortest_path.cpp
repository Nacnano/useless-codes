#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int> > g[10005];
int dist[10005];

int main(){
    int n, m;
    cin >> n >> m;

    for(int i=0;i<m;i++){
        int a, b, w;
        cin >> a >> b >> w;
        g[a].push_back({b, w});
    }
    for(int i=1;i<=n;i++) dist[i] = 1e9;

    // start at 1
    priority_queue<pair<int, int> > pq;
    dist[1] = 0;
    pq.push({0, 1});
    while(!pq.empty()){
        int u = pq.top().second;
        int current_dist = -pq.top().first;
        pq.pop();

        for(auto x: g[u]){
            int v = x.first;
            int w = x.second;

            if(dist[v] > dist[u] + w){
                dist[v] = dist[u] + w;
                pq.push({-dist[v], v});
            }
        }
    }

    cout << dist[3];
}

