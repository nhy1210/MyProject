#include<iostream>

using namespace std; 
//The function that return number of sock pair
int sockpair(int arr[], int size)
{
	int ret =0;
	sort(arr, arr+size);
	for(int i =0; i < size; i++)
		cout<<arr[i]<<" ";
	cout<<endl;
	for(int i =0; i < size; i++)
	{
		if(i != size-1)
		{
			if(arr[i] == arr[i+1] )
			{
				ret++;
				i++;
			}
		}
	}
	return ret;
}
int main()
{
	int arr[] = {10,20,40,30,20,40, 50, 10};
	int size = sizeof(arr)/sizeof(arr[0]);
	cout<<"Number of sock pair: "<<sockpair(arr, size)<<endl;
	return 0;
}
