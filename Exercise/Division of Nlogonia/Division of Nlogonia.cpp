#include <iostream>

using namespace std;

int main()
{
    int k;
    cin >> k;

    while (k != 0){
        int n, m;
        cin >> n >> m;

        for (int i=0; i<k; ++i){
            int x, y;
            cin >> x >> y;

            if (x == n or y == m)
                cout << "divisa\n";
            else if (x > n){
                if (y > m)
                    cout << "NE\n";
                else
                    cout << "SE\n";
            } else if (x < n){
                if (y > m)
                    cout << "NO\n";
                else
                    cout << "SO\n";
            }
        }
        cin >> k;
    }
}