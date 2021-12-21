#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;

    vector<int> row;

    while (t--)
    {
        int l, k;
        cin >> l >> k;

        if (l == 1)
        {
            int x;
            cin >> x;

            if (k <= row.size())
                row.insert(row.begin() + k, x);
            else
                row.push_back(x);
        } else
        if (k <= row.size())
            row.erase(row.begin() + k - 1);
    }
    for (auto i : row)
        cout << i << endl;
}
