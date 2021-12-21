#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    int n, d;
    int cases = 1;

    while (cin >> n >> d and (n || d)) {
        d *= d;
        int cont = 0;
        bool ok = true;
        pair<double, double> islands[1002];
        for (int i = 0; i < n; i++) {
            int x, y;
            cin >> x >> y;

            int sq = d - y*y;
            if (sq < 0) ok = false;
            if (ok) {
                double r = sqrt(sq);
                islands[i].first = x - r;
                islands[i].second = x + r;
            }
        }
        if (ok) {
            sort(islands, islands+n);
            for (int i = 0; i < n; i++) {
                cont ++;
                int j;
                for (j = i + 1; j < n; j++) {
                    if (islands[i].second >= islands[j].first) {
                        if(islands[i].second >= islands[j].second) i = j;
                    }
                    else {
                        i = j - 1;
                        break;
                    }
                }
                if(j == n) break;
            }
        } else cont = -1;

        cout << "Case " << cases++ << ": " << cont << endl;
    }
}