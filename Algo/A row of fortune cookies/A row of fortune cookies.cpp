#include <iostream>
using namespace std;

typedef int ValueType;
struct ListNode{
    ValueType val;
    ListNode* next;

    ListNode(ValueType v, ListNode* nxt = nullptr)
            : val(v), next(nxt) {}
};

ListNode* first = nullptr;
ListNode* last = nullptr;

int cookie_count = 0;

void print_list(ListNode*& first)
{
    ListNode* temp = first;
    do
    {
        cout << temp->val << endl;
        temp = temp->next;
    } while (temp != nullptr);
}

void insert_end(ListNode*& first, ListNode*& last, int val)
{
    ListNode* n = new ListNode(val);
    if (first == nullptr)
    {
        first = n;
    } else if (last == first)
    {
        first->next = n;
    } else
    {
        last->next = n;
    }
    last = n;
}

void insert(ListNode*& first, int val, int loc)
{
    ListNode* n = new ListNode(val);
    ListNode* temp = first;

    int i = 0;
    while (i != loc)
    {
        if (i == 0)
        {
            ++i;
            continue;
        }

        temp = temp->next;
        ++i;
    }

    if (i == 0)
    {
        n->next = first;
        first = n;
    } else
    {
        n->next = temp->next;
        temp->next = n;
    }
}

void eat(ListNode*& first, int loc)
{
    ListNode* temp = first;
    ListNode* keep = first->next;

    int i = 1;
    while (i != loc)
    {
        if (i == 1)
        {
            ++i; continue;
        }
        temp = temp->next;
        ++i;
    }
    if (i == 1)
    {
        delete first;
        first = keep;
    } else
    {
        keep = temp->next->next;
        delete temp->next;
        temp->next = keep;
    }
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int l, k;
        cin >> l >> k;

        if (l==1){
            int x;
            cin >> x;
            if (k < cookie_count)
                insert(first, x, k);
            else
                insert_end(first, last, x);
            ++cookie_count;
        } else{
            if (k <= cookie_count)
            {
                eat(first, k);
                --cookie_count;
            }
        }
    }
    print_list(first);
}