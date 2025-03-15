#include<bits/stdc++.h>
using namespace std;

unordered_map<, pair<pair<int, int> , pair<int, int> > > mm;

int x[5][1505], y[5][1505];


int main(){
    int tx, ty, n;
    cin >> tx >> ty >> n;
    for(int i=1;i<=4;i++){
        for(int j=0;j<n;j++){
            cin >> x[i][j] >> y[i][j];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mm[{x[1][i]+x[2][j], y[1][i]+y[2][j]}] = {{x[1][i], x[2][j]}, {y[1][i], y[2][j]}};
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(mm.find({tx-x[3][i]-x[4][j], ty-y[3][i]-y[4][j]}) != mm.end()){
                auto values = mm[{tx-x[3][i]-x[4][j], ty-y[3][i]-y[4][j]}];
                cout << values.first.first << " " << values.second.first << "\n";
                cout << values.first.second << " " << values.second.second << "\n";
                cout << x[3][i] << " " <<  y[3][i] << "\n";
                cout << x[4][j] << " " <<  y[4][j] << "\n";
            }
        }
    }
}
