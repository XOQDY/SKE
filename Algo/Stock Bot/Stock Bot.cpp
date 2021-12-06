#include <iostream>

using namespace std;

int main()
{
    int n, k, stock=0, buy, sell, profit=0;
    cin >> n >> k;

    int x[n];
    cin >> x[0];

    for (int i=1; i<n; ++i){
        cin >> x[i];
        if (stock == 0){
            if (x[i] - x[i-1] >= k){
                ++stock;
                buy = x[i];
            }
        } else{
            if (x[i-1] - x[i] >= k){
                --stock;
                sell = x[i];
                profit += sell - buy;
            }
        }
    }

    cout << profit;
}