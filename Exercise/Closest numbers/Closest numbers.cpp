#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, mn=1000000, diff;
    cin >> n;

    int x[n];
    for (int i=0; i<n; ++i){
        cin >> x[i];
    }

    n = sizeof(x) / sizeof(x[0]);
    sort(x, x+n);

    for (int j=0; j<n-1; ++j){
        diff = abs(x[j] - x[j+1]);
        if (diff < mn)
            mn = diff;

    }

    cout << mn;
}