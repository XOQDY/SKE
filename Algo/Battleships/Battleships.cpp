#include <iostream>

using namespace std;

int n;
char grids[110][110];

void dfs(int i, int j)
{
    if (!(i >= n || j >= n || i < 0 || j < 0))
    {
        if (grids[i][j] == '.') return;
        grids[i][j] = '.';
        dfs(i - 1, j);
        dfs(i + 1, j);
        dfs(i, j - 1);
        dfs(i, j + 1);
    }
}

int main()
{
    int t;
    cin >> t;

    int cases = 1;
    while (t--)
    {
        cin >> n;

        for (int i = 0; i < n; ++i)
        {
            cin >> grids[i];
        }

        int alive = 0;

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (grids[i][j] == 'x')
                {
                    ++alive;
                    dfs(i, j);
                }
            }
        }

        cout << "Case " << cases++ << ": " << alive << endl;
    }
}
