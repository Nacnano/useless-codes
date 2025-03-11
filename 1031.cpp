#include<bits/stdc++.h>
using namespace std;

vector<int> ladder[10005];
int dist[10005];

int main(){
    int k, n, m;
    cin >> k >> n >> m;

    for(int i=0;i<m;i++){
        int a, b;
        cin >> a >> b;
        ladder[a].push_back(b);
    }
    for(int i=1;i<=n;i++) dist[i] = 1e9;

    // floor, move
    priority_queue<pair<int, int> > pq;
    dist[1] = 0;
    pq.push({0, 1});
    while(!pq.empty()){
        int move_number = pq.top().first;
        int floor = pq.top().second;
        pq.pop();

        if(move_number == k) {
            continue;
        }

        for(auto next_floor: ladder[floor]){
            if(dist[next_floor] > dist[floor] + 1){
                dist[next_floor] = dist[floor] + 1;
                pq.push({dist[next_floor], next_floor});
            }
        }
    }


    for(int i=n;i>=1;i--){
        if(dist[i] <= k){
            cout << i;
            break;
        }
    }
}
