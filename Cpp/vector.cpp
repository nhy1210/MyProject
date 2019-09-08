#include<iostream>
#include<vector>

using namespace std;

int main()
{
	vector<int> myvec;
	for(int i =0; i < 10; i++)
	{
		myvec.push_back(i+1);
	}
	myvec.reserve(5);
	for (auto m : myvec)
		cout<<m<<" ";
	cout<<endl;
	return 0;
}