https://theory.cpe.ku.ac.th/wiki/index.php/Algo_lab/zooma_1
#include <iostream>
using namespace std;

const int MAX_N = 2000100;

int c[MAX_N];

int balls[MAX_N];
int ball_count = 0;

void insert_end(int lst[], int& s, int val)
{
    lst[s] = val;
    s++;
}

int find(int lst[], int s, int target)
{
    for (int i=0; i<s; ++i){
        if (lst[i] == target)
            return i;
    }
    return 0;
}

int* insert(int lst[], int& s, int val, int loc)
{
    for (int i=s; i > loc; --i)
        lst[i] = lst[i-1];
    lst[loc] = val;
    ++s;
    return lst;
}

int main()
{
    int n,m;
    int d,p;

    cin >> n >> m;
    for(int i=0; i<n; i++) {
        cin >> c[i];
        insert_end(balls, ball_count, i+1);
    }
    for(int i=0; i<m; i++) {
        cin >> d >> p;

        int idx = find(balls, ball_count, p);
        insert(balls, ball_count, i+n+1, idx+1);
    }

    for(int i=0; i<ball_count; i++) {
        cout << balls[i] << endl;
    }
}