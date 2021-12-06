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

void inorder(TreeNode* r, int level)
{
    if(!r) return;

    inorder(r->right, level+1);

    for (int i=0; i<level; ++i)
    {
        cout << "...";
    }
    cout << "* " << r->val << endl;

    inorder(r->left, level+1);

}


int main()
{
    TreeNode* root = nullptr;

    int n, level=0;
    cin >> n;
    for(int i=0; i<n; i++) {
        int x;
        cin >> x;
        insert(root,x);
    }
    inorder(root, level);
}
