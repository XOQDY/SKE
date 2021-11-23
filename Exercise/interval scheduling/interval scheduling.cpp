#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int max_n = 1000010;

int n;
int s[max_n];
int t[max_n];

void read_input()
{
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> s[i] >> t[i];
    }
}

int main() {
    vector<pair<int,int>> tidx;

    read_input();
    for (int i = 0; i < n; ++i) {
        tidx.emplace_back(t[i], i);
    }

    sort(tidx.begin(), tidx.end());

    int last_finish = -1;   // the time last accepted job is done
    int c = 0;

    for (int i = 0; i < n; ++i) {
        int j = tidx[i].second;        // consider job j

        // consider job j, if j does not start before last_finish,
        // accept j and update last_finish
        if (s[j] >= last_finish) {
            c++;
            last_finish = t[j];
            // update last_finish
        }
    }

    cout << c << endl;
}