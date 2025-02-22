#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int> > g[7];
int from[7];

bool visited[7];
int dis[7];

void dfs(int u){
    if(visited[u] == true) return;

    visited[u] = true;

    for(auto x: g[u]){
        int v = x.first;
        if(visited[v] == true) continue;

        from[v] = u;
        dfs(v);
    }
}

int main(){
    g[0].push_back({2, 1});

    g[1].push_back({0, 7});
    g[1].push_back({5, 2});

    g[2].push_back({0, 1});
    g[2].push_back({4, 2});
    g[2].push_back({3, 5});

    g[3].push_back({2, 5});

    g[4].push_back({2, 2});
    g[4].push_back({1, 3});

    g[5].push_back({1, 2});

    // Backtracking
    for(int i=0;i<7;i++) from[i] = -1;

    dfs(0);
    for(int i=0;i<7;i++) cout << i << " " << from[i] << endl;

    int current = 5;
    while(current != -1){
        cout << current << " ";
        current = from[current];
    }

    return 0;


    // Connected Components
    int cnt = 0;
    for(int i=0;i<7;i++){
        if(visited[i] == true) continue;

        cnt++;
        dfs(i);
    }
    cout << cnt;

    return 0;

    // BFS (min distance)
    for(int i=0;i<7;i++) dis[i] = 1e9;

    dis[0] = 0;
    queue<int> q;
    q.push(0);
    while(!q.empty()){
        int u = q.front();
        q.pop();

        for(auto x:g[u]){
            int v = x.first;
            int w = x.second;
            if(dis[v] > dis[u] + w){
                dis[v] = dis[u] + w;
                q.push(v);
            }
        }
        cout << "At " << u << endl;
        for(int i=0;i<7;i++){
            cout << i << " " << dis[i] << endl;
        }
    }

}






