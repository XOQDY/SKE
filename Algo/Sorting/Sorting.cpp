#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k, count=0;
    cin >> n >> k;


    int x[n];

    for (int i=0; i<n; ++i)
    {
        cin >> x[i];
    }

    n = sizeof(x) / sizeof(x[0]);
    sort(x, x + n);

    for (int j=k-1; j < n; j=j+k)
    {
        cout << x[j] << endl;
    }
}