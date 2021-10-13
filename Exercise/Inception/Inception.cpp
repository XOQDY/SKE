#include <iostream>
#include <utility>
using namespace std;

typedef string ValueType;
struct ListNode {
    ValueType name;
    ListNode* next;

    ListNode(ValueType n, ListNode* nxt=nullptr)
            : name(std::move(n)), next(nxt) {}
};

ListNode* top = nullptr;

void append(ListNode*& top, ValueType x)
{
    ListNode* n = new ListNode(std::move(x));
    if (top == nullptr){
        top = n;
    } else{
        n->next = top;
        top = n;
    }
}

ValueType extract(ListNode*& top)
{
    ValueType n = top->name;
    ListNode* new_front = top->next;
    delete top;
    top = new_front;
    return n;
}

int main()
{
    int n;
    cin >> n;

    for (int i=0; i<n; ++i){
        string action;
        cin >> action;
        if (action == "Sleep"){
            string name;
            cin >> name;
            append(top, name);
        }
        else if (action == "Kick"){
            if (top != nullptr)
                extract(top);
        }
        else
        if (top == nullptr)
            cout << "Not in a dream" << endl;
        else
            cout << top->name << endl;
    }
}