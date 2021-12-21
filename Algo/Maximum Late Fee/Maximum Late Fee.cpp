#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<pair<int, int>> jobs;

    for (int i = 0; i < n; ++i)
    {
        int d, c;
        cin >> d >> c;

        jobs.emplace_back(d, c);
    }

    sort(jobs.begin(), jobs.end());

    int penalty = 0;
    int day = 0;

    for (int i = 0; i < n; ++i)
    {
        day += jobs[i].second;
        int late = day - jobs[i].first;
        if (late > 10)
        {
            int pay = (late - 10) * 1000;
            if (pay > penalty)
                penalty = pay;
        }
    }

    cout << penalty;
}
