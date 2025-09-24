#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int level=0;level<n;level++){
        for(int star=0;star<n;star++){
            cout << "*";
        }
        cout << "\n";
    }
    
    return 0;
}