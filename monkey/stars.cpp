// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    int level = n / 2;
    if(n % 2 == 0){
        for(int i=1;i<=level;i++){
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            if(i == 1){
                cout << "*";
            }
            else {
                cout << "*";
                for(int hy=1;hy<=2*i-3;hy++){
                    cout << "-";
                }
                cout << "*";
            }
            
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            cout << "\n";
        }
        
        for(int i=level;i>=1;i--){
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            if(i == 1){
                cout << "*";
            }
            else {
                cout << "*";
                for(int hy=1;hy<=2*i-3;hy++){
                    cout << "-";
                }
                cout << "*";
            }
            
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            cout << "\n";
        }
    }
    else {
        level++;
        for(int i=1;i<=level-1;i++){
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            if(i == 1){
                cout << "*";
            }
            else {
                cout << "*";
                for(int hy=1;hy<=2*i-3;hy++){
                    cout << "-";
                }
                cout << "*";
            }
            
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            cout << "\n";
        }
        
        for(int i=level;i>=1;i--){
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            if(i == 1){
                cout << "*";
            }
            else {
                cout << "*";
                for(int hy=1;hy<=2*i-3;hy++){
                    cout << "-";
                }
                cout << "*";
            }
            
            for(int hy=1;hy<=level-i;hy++){
                cout << "-";
            }
            
            cout << "\n";
        }
    }
    
    return 0;
}