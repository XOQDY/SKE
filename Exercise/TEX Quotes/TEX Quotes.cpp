#include <iostream>

using namespace std;

int main() {
    string text;
    bool open = true;

    while (getline(cin, text)){
        for (int i=0; text[i]; ++i){
            if (text[i] == '"'){
                if (open)
                    cout << "``";
                else
                    cout << "''";
                open = not open;
            } else
                cout << text[i];
        }
        cout << "\n";
    }
}