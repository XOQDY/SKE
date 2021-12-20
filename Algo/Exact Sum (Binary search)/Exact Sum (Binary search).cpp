#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    while (cin >> n)
    {
        vector<int> price;
        int m;

        for (int i = 0; i < n; ++i)
        {
            int j;
            cin >> j;

            price.push_back(j);
        }

        cin >> m;

        sort(price.begin(), price.end());
        int book1 = price.front(), book2 = price.back();

        for (int i = 0; i < n; ++i)
        {
            int a = price[i];
            int b = m - a;

            if (a > b)
                break;

            if (binary_search(price.begin() + i + 1, price.end(), b))
            {
                book1 = a;
                book2 = b;
            }
        }

        cout << "Peter should buy books whose prices are " << book1 << " and " << book2 << "." << endl << endl;
    }
}