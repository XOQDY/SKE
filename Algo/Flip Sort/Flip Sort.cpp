#include <iostream>
#include <algorithm>

using namespace std;

int bubble_sort(int a[], int n)
{
    int flip=0;
    while(true) {
        bool changed = false;
        for (int i=0; i <n-1; i++) {
            if(a[i] > a[i+1]) {
                int t;
                t = a[i];
                a[i] = a[i+1];
                a[i+1] = t;
                changed = true;
                ++flip;
            }
        }
        if(!changed)
            break;
    }
    return flip;
}

int main()
{
    int n, flip;

    while (cin >> n){
        int x[n];
        for (int i=0; i<n; ++i){
            cin >> x[i];
        }
        flip = bubble_sort(x, n);
        cout << "Minimum exchange operations : " << flip << endl;
    }
}