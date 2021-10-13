#include <iostream>
using namespace std;

typedef int ValueType;
struct ListNode {
    ValueType val=0;
    ListNode* next;

};

ListNode* last = nullptr;

void append(ListNode*& last)
{
    ListNode* temp = new ListNode();
    if (last == nullptr){
        last = temp;
        temp->next = last;
    } else{
        temp->next = last->next;
        last->next = temp;
        last = temp;
    }
}

void insert(ListNode*& last, ListNode*& current)
{
    ListNode* temp = new ListNode();
    if (last == current)
        last = temp;
    temp->next = current->next;
    current->next = temp;
}

void print_list(ListNode* last)
{
    ListNode* temp = last->next;
    do
    {
        cout << temp->val << " ";
        temp = temp->next;
    } while (temp != last->next);
}

int main()
{
    int n, m;
    cin >> n >> m;


    for (int i=0; i<n; ++i){

        append(last);
    }

    ListNode* temp1 = last->next, *temp2;
    for (int j=0; j<m; ++j){
        int action;
        cin >> action;

        if (action == 0)
            temp1 = last->next;
        else if (action == 1)
            temp1 = temp1->next;
        else if (action == 2)
            insert(last, temp1);
        else if (action == 3){
            int bonus;
            cin >> bonus;
            temp1->val += bonus;
        }
    }
    print_list(last);
}