#include<iostream>

using namespace std;
class Node{
	public: 
	int data;
	Node* left, *right;
	Node(int val){
		this->data = val;
		this->left = NULL;
		this->right = NULL;
	}
};
class Solution{
	public: 
		Node* insert(Node* root, int data)
		{
			if (!root)	return new Node(data);
			else 
			{
				Node* cur;
				if(data <= root->data)
				{
					cur = insert(root->left, data);
					root->left = cur;
				}
				else{
					cur = insert(root->right, data);
					root->right = cur;
				}
			}
			return root;
		}
		
};
void printNode(Node* root) //DFS : pre-order
{
	if(root) cout<<root->data<<endl;
	if(root->left) printNode(root->left);
	if(root->right) printNode(root->right);
}
int heightofTree(Node* root)
{
	if(!root) return -1;
	int leftHeight = heightofTree(root->left);
	int rightHeight = heightofTree(root->right);
	return max(leftHeight, rightHeight)+1;
}
int main()
{
	Node* root = new Node(2);
	root->left = new Node(3);
	root->right = new Node(4);
	root->left->left = new Node(7);
	root->right->right = new Node(8);
	printNode(root);

	cout<<"Height of the tree : "<<heightofTree(root)<<endl;
	

	return 0;
}
