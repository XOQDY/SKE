#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t, c=1;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<char> field(n+2);
        for (int i=0; i<n; ++i)
            cin >> field[i];

        int scarecrow=0;
        for (int i=0; i < n; ++i)
        {
            if (field[i] == '.')
            {
                field[i] = field[i+1] = field[i+2] = '#';
                ++scarecrow;
            }
        }
        cout << "Case " << c++ << ": " << scarecrow << endl;
    }
}