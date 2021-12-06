#include <iostream>

using namespace std;

int main()
{
    int n, eaten=0;
    cin >> n;

    int a, yesterday=0;
    for (int i=0; i<n; ++i){
        cin >> a;
        if (a > 1000)
            a = 1000;
        if (yesterday == 1000)
            a = 0;
        else
            eaten += a;
        yesterday = a;
    }

    cout << eaten;
}