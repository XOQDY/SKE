#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n, result;
        cin >> n;

        result = (n * 567 / 9 + 7492) * 235 / 47 - 498;
        result = result / 10;

        cout << abs(result % 10) << endl;
    }
}