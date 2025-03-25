#include<bits/stdc++.h>
using namespace std;
const int maxN=1e5+5;

vector<pair<int, pair<int , int> > > g[maxN];
int distw[maxN], distd[maxN];

int main(){

    int n, m, k;
    cin >> n >> m >> k;
    while(m--){
        int u, v, d, w;
        cin >> u >> v >> d >> w;
        g[u].push_back({v, {d, w}});
        g[v].push_back({u, {d, w}});
    }

    for(int i=0;i<n;i++){
        // distw[i] = 0;
        distd[i] = 1e9;
    }

    priority_queue<pair<pair<int, int>, int>> pq;
    pq.push({{1e9, 0}, 0});
    distw[0] = 1e9;
    distd[0] = 0;
    while(!pq.empty()){
        int w_now = pq.top().first.first;
        int d_now = -pq.top().first.second;
        int u = pq.top().second;
        pq.pop();

        // cout << w_now << " " << d_now << " " << u << endl;
        for(auto x: g[u]){
            int v = x.first;
            int d = x.second.first;
            int w = x.second.second;

            if(distw[v] < min(w_now, w)){
                distw[v] = min(w_now, w);
                distd[v] = distd[u] + d;
                pq.push({{distw[v], -distd[v]}, v});
            }
            else if(distw[v] == min(w_now, w)){
                if(distd[v] > distd[u] + d){
                    distd[v] = distd[u] + d;
                    pq.push({{distw[v], -distd[v]}, v});
                }
            }
        }
    }

    int ans_w = 1e9;
    vector<int> ans_d;
    while(k--){
        int v;
        cin >> v;
        ans_w = min(ans_w, distw[v]);
        ans_d.push_back(distd[v]);
    }
    cout << ans_w << "\n";
    for(auto x: ans_d) cout << x << "\n";
}

