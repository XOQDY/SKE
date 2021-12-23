#include <iostream>
#include <cstring>

using namespace std;

int n, m, sum;
char map[21][21], visited[21][21], land;

void dfs(int x, int y)
{
    if(y < 0)
        y = m - 1;
    if(y >= m)
        y = 0;
    if(x < 0 || x >= n)
        return;
    if(visited[x][y] != 0 || map[x][y] != land)
        return;
    visited[x][y] = 1;
    sum++;

    dfs(x+1, y);
    dfs(x, y+1);
    dfs(x-1, y);
    dfs(x, y-1);
}
int main() {
    while(cin >> n >> m)
    {
        memset(visited, 0, sizeof(visited));

        for(int i = 0; i < n; i++)
            cin >> map[i];

        int x, y;
        cin >> x >> y;

        land = map[x][y];
        dfs(x, y);

        int capture = 0;

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                sum = 0;
                dfs(i, j);

                if(sum > capture)
                    capture = sum;
            }
        }
        cout << capture << endl;
    }
}
