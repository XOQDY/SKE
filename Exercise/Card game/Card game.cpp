#include <iostream>
using namespace std;

typedef int ValueType;
struct ListNode {
    ValueType val;
    ListNode* next;

    ListNode(ValueType v, ListNode* nxt=nullptr)
            : val(v), next(nxt) {}
};

ListNode* last = nullptr;

void append(ListNode*& last, ValueType x)
{
    ListNode* temp = new ListNode(x);
    if (last == nullptr){
        last = temp;
        temp->next = last;
    } else{
        temp->next = last->next;
        last->next = temp;
        last = temp;
    }

}

void extract(ListNode*& last, ListNode*& current, ListNode*& before)
{
    if (current == last)
        last = before;
    before->next = current->next;
    delete current;
    current = before->next;
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
        int x;
        cin >> x;

        append(last, x);
    }
    print_list(last);

    ListNode* temp1 = last->next, *temp2 = last;
    for (int j=0; j<m; ++j){
        int value;
        cin >> value;

        int sum=temp1->val;
        while (sum < value){
            temp2 = temp1;
            temp1 = temp1->next;
            sum += temp1->val;
        }
        extract(last, temp1, temp2);
        print_list(last);
    }
    print_list(last);
}