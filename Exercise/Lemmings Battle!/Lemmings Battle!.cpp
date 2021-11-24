#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void print_output(const vector<int>(&x))
{
    for (int i : x)
        cout << i << endl;
}

int main() {
    int n;
    cin >> n;

    while (n--)
    {
        int bf, sg, sb;
        cin >> bf >> sg >> sb;

        vector<int> g(sg), b(sb);

        for (int i=0; i<sg; ++i)
            cin >> g[i];
        for (int i=0; i<sb; ++i)
            cin >> b[i];

        sort(g.begin(), g.end(), greater<int>());
        sort(b.begin(), b.end(), greater<int>());

        while (!g.empty() && !b.empty())
        {
            int min_bf = min(bf, int(min(g.size(), b.size())));

            sort(g.begin(), g.end(), greater<int>());
            sort(b.begin(), b.end(), greater<int>());

            for (int i=0; i<min_bf; ++i)
            {
                int fg = g.front();
                int fb = b.front();

                g.erase(g.begin());
                b.erase(b.begin());

                if (fg > fb)
                    g.push_back(fg - fb);
                else if (fb > fg)
                    b.push_back(fb - fg);
            }
        }

        if (g.empty() && b.empty())
        {
            cout << "green and blue died" << endl;
        } else if (g.empty())
        {
            cout << "blue wins" << endl;
            sort(b.begin(), b.end(), greater<>());
            print_output(b);
        } else
        {
            cout << "green wins" << endl;
            sort(g.begin(), g.end(), greater<>());
            print_output(g);
        }
        cout << "\n";
    }
}
