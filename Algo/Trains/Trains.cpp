#include <iostream>
#include <vector>
#include <list>

using namespace std;

const int MAX_N = 100010;

int n, m, q;
vector<int> adj[MAX_N];
vector<int> levels[MAX_N];
int deg[MAX_N];

void read_input()
{
    cin >> n >> m >> q;

    for (int u = 0; u < n; ++u) {
        deg[u] = 0;
    }

    for (int i = 0; i < m; ++i) {
        int a, b, c;
        cin >> a >> b >> c; a--; b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
        levels[a].push_back(c);
        levels[b].push_back(c);
        deg[a]++;
        deg[b]++;
    }
}


void init(bool visited[])
{
    for (int u = 0; u < n; ++u) {
        visited[u] = false;
    }
}

bool bfs2(int a, int b, int c)
{
    bool visited[MAX_N];
    init(visited);

    list<int> queue;

    queue.push_back(a);
    visited[a] = true;


    while (!queue.empty()) {
        // iterate over all nodes in currentNodes
        int u = queue.front();
        queue.pop_front();

        for (int d = 0; d < deg[u]; ++d) {
            int v = adj[u][d];
            int level = levels[u][d];

//            cout << "v " << v << " level " << level << endl;

            if (!visited[v] and c >= level) {
                visited[v] = true;
                queue.push_back(v);
            }
        }
    }
    if (visited[b])
        return true;
    else
        return false;
}


int main()
{
    read_input();

    for (int i = 0; i < q; ++i)
    {
        int l, s, t;
        cin >> l >> s >> t; s--; t--;
        if (bfs2(s, t, l))
            cout << "yes" << endl;
        else
            cout << "no" << endl;
    }
}

