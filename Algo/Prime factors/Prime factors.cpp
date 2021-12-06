#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int isPrimeNumber(int n) {
    bool isPrime = true;

    for(int i = 2; i <= n/2; i++) {
        if (n%i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

int main()
{
    int n, distinct=0;
    bool isPrime;
    cin >> n;

    for(int i = 2; i < n+1; i++) {
        isPrime = isPrimeNumber(i);

        if(isPrime and n % i == 0)
            ++distinct;
    }

    cout << distinct;
}