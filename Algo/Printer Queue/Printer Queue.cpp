#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int testcase;
    cin >> testcase;

    while (testcase--)
    {
        int n, m;
        cin >> n >> m;

        int min = 0;
        bool printed = false;
        queue<pair<int, int>> job;
        vector<int> order;

        for (int i = 0; i < n; ++i)
        {
            int p;
            cin >> p;

            job.push(make_pair(p, i));
            order.push_back(p);
        }

        sort(order.begin(), order.end(), greater<>());

        for (int i = 0; i < n; ++i)
        {
            while (job.front().first != order[i])
            {
                job.push(job.front());
                job.pop();
            }
            if (job.front().second == m)
            {
                ++min;
                break;
            }
            job.pop();
            ++min;
        }
        cout << min << endl;
    }
}
