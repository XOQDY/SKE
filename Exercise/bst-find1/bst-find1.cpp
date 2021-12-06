#include <iostream>

using namespace std;

typedef int valueType;

struct TreeNode
{
    valueType val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(valueType val, TreeNode* left=nullptr, TreeNode* right=nullptr)
            : val(val), left(left), right(right) {}
};

void insert(TreeNode*& r, valueType x)
{
    if(!r)
        r = new TreeNode(x);
    else if(x < r->val)
        insert(r->left, x);
    else if(x > r->val)
        insert(r->right,x);
}

bool in(TreeNode* r, valueType x)
{

    if (!r)
        return false;
    if (r->val == x)
        return true;
    else if (r->val > x)
        return in(r->left, x);
    else
        return in(r->right, x);
}

int main()
{
    TreeNode* root = nullptr;

    int m;
    cin >> m;
    for(int i=0; i<m; i++) {
        int k, x;
        cin >> k >> x;
        if (k == 1)
            insert(root,x);
        else
        {
            if (in(root, x))
                cout << "1" << endl;
            else
                cout << "0" << endl;
        }
    }
}
