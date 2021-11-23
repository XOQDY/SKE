#include <iostream>
using namespace std;

void rotate(int arr[])
{
    int x, y, z, i;
    i = arr[0];
    x = arr[1];
    y = arr[2];
    z = arr[3];

    arr[0] = z;
    arr[1] = i;
    arr[2] = x;
    arr[3] = y;
}

int calculate_score(int o[], int t[], int th[], int f[])
{
    int score=0;
    for (int i=0; i<4; ++i){
        if (o[i] == t[i] and o[i] == th[i] and o[i] == f[i])
            ++score;
    }
    return score;
}

int main()
{
    int one[4], two[4], three[4], four[4], max_score=0;
    for (int i=0; i<4; ++i){
        cin >> one[i] >> two [i] >> three[i] >> four[i];
    }

    for (int x=0; x<4; ++x){
        for (int y=0; y<4; ++y){
            for (int z=0; z<4; ++z){
                int score = calculate_score(one, two, three, four);
                if (score > max_score)
                    max_score = score;
                rotate(four);
            }
            rotate(three);
        }
        rotate(two);
    }

    cout << max_score;
}