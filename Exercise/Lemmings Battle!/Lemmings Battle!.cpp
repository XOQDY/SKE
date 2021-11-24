#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>

using namespace std;

void print_output(const multiset<int, greater<>>(&x))
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

        multiset<int, greater<> > g, b;

        for (int i=0; i<sg; ++i)
        {
            int p;
            cin >> p;
            g.insert(p);
        }

        for (int i=0; i<sb; ++i)
        {
            int p;
            cin >> p;
            b.insert(p);
        }

        while (!g.empty() && !b.empty())
        {
            int min_bf = min(bf, int(min(g.size(), b.size())));

            for (int i=0; i<min_bf; ++i)
            {
                multiset<int> :: iterator fg, fb;

                fg = g.begin();
                fb = b.begin();

                g.erase(fg);
                b.erase(fb);

                if (*fg > *fb)
                    g.insert(*fg - *fb);
                else if (*fb > *fg)
                    b.insert(*fb - *fg);
            }
        }

        if (g.empty() && b.empty())
        {
            cout << "green and blue died" << endl;
        } else if (g.empty())
        {
            cout << "blue wins" << endl;
            print_output(b);
        } else
        {
            cout << "green wins" << endl;
            print_output(g);
        }
        cout << "\n";
    }
}