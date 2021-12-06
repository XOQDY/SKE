//
// Created by XOQDY on 10/7/2021.
//

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int x[n], y[n], profit[n], sum=0;
    for (int i=0; i<n; ++i){
        cin >> x[i] >> y[i];
        profit[i] = x[i] - y[i];
        sum += profit[i];
    }

    sort(profit, profit + n);

    int throw_away=0;
    if (k > 0){
        if (profit[0] < 0){
            sum -= profit[0];
            ++throw_away;
        }
        if (profit[1] < 0 and k > throw_away){
            sum -= profit[1];
            ++throw_away;
        }
        if (profit[2] < 0 and k > throw_away){
            sum -= profit[2];
            ++throw_away;
        }
    }
    cout << sum;
}