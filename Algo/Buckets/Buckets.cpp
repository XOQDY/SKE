#include <iostream>

using namespace std;

int main()
{
    int n, water, tank=0, bucket[5]= {};
    cin >> n;

    for (int i=0; i<n; ++i){
        cin >> water;
        int min_b=bucket[0], min_i=0;
        for (int j=0; j<5; ++j){
            if (min_b > bucket[j+1]){
                min_b = bucket[j+1];
                min_i = j+1;
            }
        }
        bucket[min_i] += water;
        if (bucket[min_i] >= 1000){
            tank += 1000;
            bucket[min_i] = 0;
        }
    }

    cout << tank;
}