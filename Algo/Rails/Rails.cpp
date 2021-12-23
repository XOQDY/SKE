#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    int n;
    while (cin >> n and n)
    {
        int coach;
        while (cin >> coach and coach)
        {
            queue<int> destination;

            destination.push(coach);

            for (int i = 1; i < n; ++i)
            {
                cin >> coach;

                destination.push(coach);
            }

            stack<int> station;

            for (int i = 1; i <= n; ++i)
            {
                station.push(i);

                while (!station.empty() and station.top() == destination.front())
                {
                    station.pop();
                    destination.pop();
                }
            }

            if (station.empty())
                cout << "Yes" << endl;
            else
                cout << "No" << endl;
        }
    }
}
