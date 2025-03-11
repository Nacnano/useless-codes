#include<bits/stdc++.h>
using namespace std;

int m, x, y, t[25][25];
bool visited[25][25];
int dx[5] = {0, 0, 1, -1};
int dy[5] = {1, -1, 0, 0};

int main(){

    cin >> m >> x >> y;
    for(int i=0;i<m;i++){
        for(int j=0;j<m;j++){
            cin >> t[i][j];
        }
    }

    int ans = t[y-1][x-1];
    queue<pair<int, int>> q;
    q.push({x-1, y-1});
    while(!q.empty()){
        int xnow = q.front().first;
        int ynow = q.front().second;
        q.pop();

        if(visited[ynow][xnow]) continue;
        visited[ynow][xnow] = true;

        for(int i=0;i<4;i++){
            int xnew = xnow + dx[i];
            int ynew = ynow + dy[i];

            if(xnew < 0 || xnew >= m || ynew < 0 || ynew >= m) continue;
            if(t[ynew][xnew] == 100) continue;

            if(t[ynew][xnew] > t[ynow][xnow]){
                ans = max(ans, t[ynew][xnew]);
                q.push({xnew, ynew});
            }
        }
    }

    cout << ans;
}
