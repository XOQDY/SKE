#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;

    while (cin >> n >> m and (n || m))
    {
        int cd=0;

        vector<int> jack(n), jill(m);

        for (int i=0; i<n; ++i)
            cin >> jack[i];

        for (int i=0; i<m; ++i)
            cin >> jill[i];

        if (n>m)
        {
            for (int i=0; i<m; ++i)
            {
                if (find(jack.begin(), jack.end(), jill[i]) != jack.end())
                    ++cd;
            }
        } else
        {
            for (int i=0; i<n; ++i)
            {
                if (find(jill.begin(), jill.end(), jack[i]) != jill.end())
                    ++cd;
            }
        }

        cout << cd << endl;
    }
}
