#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    int banner = -1;
    cin >> n;

    vector<pair<int, int>> poles;

    for (int i = 0; i < n; ++i)
    {
        int x;
        cin >> x;
        poles.emplace_back(x, i);
    }

    sort(poles.begin(), poles.end());

    for (int i = 0; i < n; ++i)
    {
        int j = i + 1;

        if (poles[i].first == poles[j].first)
        {
            int range = poles[j].second - poles[i].second;
            if (banner < range)
                banner = range;
        }

    }

//    for (int i = 0; i < n; ++i)
//    {
//        cout << poles[i].first << endl;
//    }
    cout << banner;
}