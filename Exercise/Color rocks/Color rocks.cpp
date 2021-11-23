#include <iostream>
using namespace std;

typedef int ValueType;
struct ListNode {
    ValueType val;
    ListNode* next;

    ListNode(ValueType v, ListNode* nxt=nullptr)
            : val(v), next(nxt) {}
};
ListNode* top = nullptr;

void append(ListNode*& top, ValueType x)
{
    ListNode* n = new ListNode(x);
    if (top == nullptr){
        top = n;
    } else{
        n->next = top;
        top = n;
    }
}

void extract(ListNode*& top, ValueType x)
{
    ListNode* n = top->next;
    for (int i=0; i<x; ++i){
        delete top;
        if (n != nullptr){
            top = n;
            n = top->next;
        } else
            top = nullptr;
    }
}

int check_duplicate(ListNode*& top, ValueType x)
{
    ListNode* next = top->next;
    for (int i=1; i<x; ++i){
        if (next == nullptr or top->val != next->val)
            return false;
        next = next->next;
    }
    return true;
}

int left_list(ListNode* top)
{
    int left=0;
    while (top != nullptr){
        ++left;
        top = top->next;
    }
    return left;
}

int main()
{
    int n, k;
    cin >> n >> k;

    for (int i=0; i<n; ++i){
        int c;
        cin >> c;

        append(top, c);
        if (check_duplicate(top, k))
            extract(top, k);
    }
    int left= left_list(top);
    cout << left;
}