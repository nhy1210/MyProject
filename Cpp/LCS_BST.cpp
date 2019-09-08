#include<iostream>

using namespace std;
class Node{
	public: 
	int data;
	Node* left, *right;
	Node(int val){
		this->data = val;
		left = NULL;
		right = NULL;
	}
	
};
class Solution{
public: 

	Node* insertnode(Node* root, int data)
	{
		if (!root) return new Node(data);
		if(data<= root->data)
		{
			root->left = insertnode(root->left, data);		
		}
		else 
			root->right= insertnode(root->right, data);
		return root;
	}
	Node* lca(Node* root, int v1, int v2)
	{
		if(!root) return NULL;
		if((v1 < root->data) && (v2 < root->data))
			return lca (root->left, v1, v2);
		else if((v1 > root->data) && (v2 > root->data))
			return lca(root->right, v1,v2);
		return root;
	}

};
void printTree(Node* root)
{
	if(root->left) printTree(root->left);
	if(root) cout<<root->data<<endl;
	if(root->right) printTree(root->right);
}

int main()
{
	Solution Mytree;
	Node* root = new Node(4);
	/*root = Mytree.insertnode(root, 2);
	root = Mytree.insertnode (root, 1);
	root = Mytree.insertnode(root, 3);
	root = Mytree.insertnode(root, 7);
	root = Mytree.insertnode(root, 6);*/
	root->left = new Node(2);
	root->right = new Node(7);
	root->left->left = new Node(1);
	root->left->right = new Node(3);
	root->right->left = new Node(6);
	printTree(root);
	Node* ret = Mytree.lca(root, 3,5);
	cout<<"lca of 3 & 1 is : "<<ret->data<<endl;

	return 0;
}
