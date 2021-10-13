#include <iostream>

using namespace std;

int largest(int arr[])
{
    int max=arr[0];

    for (int i=1; i<10; ++i){
        if (max < arr[i])
            max = arr[i];
    }
    return max;
}

int main()
{
    int n, c[10]={};
    cin >> n;

    char type;
    int column;
    for (int i=0; i<n; ++i){
        cin >> type >> column;
        --column;
        int max=c[column];
        if (type == '-'){
            for (int x=column+1; x<column+4; ++x){
                if (max < c[x])
                    max = c[x];
            }
            for (int y=column; y<column+4; ++y)
                c[y] = max + 1;
        }
        else if (type == 'i')
            c[column] += 4;
        else if (type == 'o'){
            for (int z=column+1; z<column+2; ++z){
                if (max < c[z])
                    max = c[z];
            }
            for (int k=column; k<column+2; ++k)
                c[k] = max + 2;
        }
    }

    cout << largest(c);
}