#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>
#include <queue>

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
            queue<int> store_g, store_b;
            int min_bf = min(bf, int(min(g.size(), b.size())));

            for (int i=0; i<min_bf; ++i)
            {
                multiset<int> :: iterator fg, fb;

                fg = g.begin();
                fb = b.begin();

                g.erase(fg);
                b.erase(fb);

                store_g.push(*fg);
                store_b.push(*fb);
            }

            for (int i=0; i<min_bf; ++i)
            {
                if (store_g.front() > store_b.front())
                    g.insert(store_g.front() - store_b.front());
                else if (store_b.front() > store_g.front())
                    b.insert(store_b.front() - store_g.front());

                store_g.pop();
                store_b.pop();
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