#include <iostream>
using namespace std;

int main()
{
    int g;
    while (cin >> g, g != 0){
        string group, reverse;
        cin >> group;

        int n = group.length();
        int group_size = n / g;

        for (int i=0; i<n; i+=group_size){
            string temp;
            for (int j=i; j<=i+group_size-1; ++j){
                temp = group[j] + temp;
            }
            reverse += temp;
        }
        cout << reverse << endl;
    }
}