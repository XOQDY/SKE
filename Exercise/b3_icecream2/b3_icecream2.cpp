#include <iostream>
using namespace std;

typedef int ValueType;
struct ListNode {
    ValueType val;
    ValueType flavour;
    ListNode* next;

    ListNode(ValueType v, ValueType f, ListNode* nxt=nullptr)
            : val(v), flavour(f), next(nxt) {}
};

ListNode* front = nullptr;
ListNode* rear = nullptr;

void append(ListNode*& front, ListNode*& rear, ValueType x, ValueType f)
{
    ListNode* n = new ListNode(x, f);
    if (rear != nullptr) {
        rear->next = n;
        rear = n;
    } else {
        front = rear = n;
    }
}

ValueType extract(ListNode*& front, ListNode*& rear)
{
    ValueType v = front->val;

    ListNode* new_front = front->next;
    delete front;
    front = new_front;
    if (front == nullptr) {
        rear = nullptr;
    }
    return v;
}

int main()
{
    int m, q=0, flavour[20]={};

    cin >> m;
    for (int i = 0; i < m; ++i) {
        int t;

        cin >> t;
        if (t == 1) {
            int n;
            cin >> n;
            for (int j=0; j<n; ++j){
                int x, f;
                cin >> x >> f;
                append(front, rear, x, f);
                ++q;
            }
        } else {
            int out;
            ++flavour[front->flavour - 1];
            out = extract(front, rear);
            --q;
            cout << out << endl;
        }
    }
    cout << q << endl;
    for (int k : flavour)
        cout << k << " ";

}