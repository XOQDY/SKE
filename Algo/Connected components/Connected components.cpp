#include <iostream>
#include <vector>
#include <list>

using namespace std;

const int MAX_N = 100010;

int n, m;
vector<int> adj[MAX_N];
int deg[MAX_N];
int connect = 0;

void read_input()
{
    cin >> n >> m;

    for (int u = 0; u < n; ++u) {
        deg[u] = 0;
    }

    for (int i = 0; i < m; ++i) {
        int u,v;
        cin >> u >> v; u--; v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
}

bool seen[MAX_N];

void init()
{
    for (int u = 0; u < n; ++u) {
        seen[u] = false;
    }
}

void bfs2(int s)
{
    list<int> q;

    q.push_back(s);
    seen[s] = true;

    while (!q.empty()) {
        // iterate over all nodes in currentNodes
        int u = q.front();
        q.pop_front();

        for (int d = 0; d < deg[u]; ++d) {
            int v = adj[u][d];

            if (!seen[v]) {
                seen[v] = true;
                q.push_back(v);
            }
        }
    }
}


int main()
{
    read_input();
    init();
    for (int i = 0; i < n; ++i)
    {
        if (!(seen[i]))
        {
            bfs2(i);
            ++connect;
        }
    }
    cout << connect << endl;
}
