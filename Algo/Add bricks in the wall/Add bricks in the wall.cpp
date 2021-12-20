#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        int wall[10][10] = {};

        for (int i = 0; i < 9; i += 2)
        {
            for (int j = 0; j <= i; j += 2)
            {
                cin >> wall[i][j];
            }
        }

        int top, left, right;

        for (int i = 0; i < 8; i += 2)
        {
            for (int j = 0; j <= i; j += 2)
            {
                top = wall[i][j];
                left = wall[i + 2][j];
                right = wall[i + 2][j + 2];

                wall[i + 2][j + 1] = (top - (left + right)) / 2;
                wall[i + 1][j] = left + wall[i + 2][j + 1];
                wall[i + 1][j + 1] = right + wall[i + 2][j + 1];
            }
        }

        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j <= i; ++j)
            {
                cout << wall[i][j] << " ";
            }
            cout << endl;
        }
    }
}