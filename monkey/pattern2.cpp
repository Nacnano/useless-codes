#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int level=1;level<=n;level++){
        for(int star=1;star<=level;star++){
            cout << "*";
        }
        cout << "\n";
    }
    
    return 0;
}