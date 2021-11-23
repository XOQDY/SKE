#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, d, r;
    while (cin >> n >> d >> r and (n and d and r))
    {
        vector<int> a, b;
        int price=0;

        for (int i=0; i<n; ++i)
        {
            int x;
            cin >> x;

            a.push_back(x);
        }

        for (int i=0; i<n; ++i)
        {
            int x;
            cin >> x;

            b.push_back(x);
        }

        sort(a.begin(), a.end());
        sort(b.begin(), b.end(), greater<int>());


        for (int i=0; i<n; ++i)
        {
            int overtime=a[i] + b[i];

            if (overtime > d)
                price += (overtime - d) * r;
        }

        cout << price << endl;
    }
}