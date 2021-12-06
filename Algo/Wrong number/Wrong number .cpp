#include <iostream>
using namespace std;

int black_sheep(int arr[], int n)
{
    int index, same=0;

    for (int i = 1; i < n; i++){
        if (arr[0] != arr[i]){
            index = i;
        } else {
            ++same;
        }
    }

    if (same != 0){
        return index;
    }
    return 0;
}

int main()
{
    int n;
    cin >> n;

    int x[n][n];

    for (int a=0; a<n; ++a){
        for (int b=0; b<n; ++b){
            cin >> x[a][b];
        }
    }

    int sum_row[n], sum_column[n];
    for (int c=0; c<n; ++c){
        sum_row[c] = 0;
        sum_column[c] = 0;
    }

    for (int y=0; y<n; ++y){
        for (int z=0; z<n; ++z){
            sum_row[y] += x[y][z];
            sum_column[y] += x[z][y];
        }
    }

    cout << x[black_sheep(sum_row, n)][black_sheep(sum_column, n)];
}