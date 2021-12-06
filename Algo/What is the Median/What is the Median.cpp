#include <iostream>
#include <algorithm>

using namespace std;

int main()
{

    int x[10000];

    int n=0;
    while (cin >> x[n++]){
        sort(x, x+n);
        if (n % 2 == 0)
            cout << (x[n/2] + x[(n/2)-1]) / 2 << endl;
        else
            cout << x[n/2] << endl;
    }
}