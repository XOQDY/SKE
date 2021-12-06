#include <iostream>

using namespace std;

int main()
{
    int n, exp=0;
    cin >> n;

    int x[n];

    for (int i=0; i<n; ++i){
        cin >> x[i];
        if ((i+1) % 4 == 0)
            exp += x[i] * 2;
        else
            exp += x[i];
    }
    cout << exp;
}