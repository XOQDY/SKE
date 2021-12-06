#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int t, c=1;
    cin >> t;

    for (int i=0; i<t; ++i, ++c)
    {
        int n, p, q;
        cin >> n >> p >> q;

        vector<int> weight;
        int bowl=0, gm=0;
        for (int j=0; j<n; ++j)
        {
            int x;
            cin >> x;
            weight.push_back(x);
        }

        sort(weight.begin(), weight.end());

        for (int j=0; j<n; ++j)
        {
            if (bowl + 1 > p || gm + weight[j] > q)
                break;
            else
            {
                gm += weight[j];
                ++bowl;
            }
        }
        cout << "Case " << c << ": " << bowl << endl;
    }
}