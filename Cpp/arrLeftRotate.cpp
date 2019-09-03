#include<iostream>
#include<vector>
using namespace std;

/* In this exercise, left rotate likes below example
Original arr[] = {2,3,4,5,6}; 
After 2 left rotate
Result arr[]  = {4,5,6,2,3}*/ 

vector<int> leftrotate(int arr[], int size, int left)
{
	vector<int> ret;
	for(int i =left; i < size; i++)
	{
		ret.push_back(arr[i]);
	}
	for(int i =0; i < left; i++)
		ret.push_back(arr[i]);
	return ret;

}
int main()
{
	int arr[] = {0,2,3,4,7};
	int size = sizeof(arr)/sizeof(arr[0]);
	vector<int> ret = leftrotate(arr, size, 3);
	for(auto i : ret)
		cout<<i<<" ";
	cout<<endl;
	return 0;
}
