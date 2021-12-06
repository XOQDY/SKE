#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int h0=0, h1, m=0, energy=0;
    for (int i=0; i<n; ++i){
        cin >> h1;
        int power=h1-h0;
        if (power > 0){
            energy += power+m;
            ++m;
        } else{
            m=0;
        }
        h0 = h1;
    }
    cout << energy;
}