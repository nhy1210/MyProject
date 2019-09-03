#include<iostream>
#include<map>
using namespace std;
/* You are given an array and you need to find number of triplets that sasticfied geometric progression for a given common ratio r and i< j< k
 For ex) Arr[] ={1,4,16,64] and r = 4
 Result [1,4,16]  and [4,16,64]
*/ 
/* //Below method has O(n^2 * logn) complexity time. We can archive in O(n^2) only in other method
int findTriplet(int arr[], int size, int r)
{
	int count =0;
	multimap<int,int> mymap;
	for(int i =0; i < size; i++)
	{
		mymap.insert(pair<int,int>(arr[i], i));
	} 
	for(int j =0; j < size -2; j++)
	{
		for(int m = j+1; m< size-1; m++)
		{
			if(arr[j]*r == arr[m])
			{
				typedef std::multimap<int, int>::iterator MMAPIterator;
                std::pair<MMAPIterator,MMAPIterator> result= mymap.equal_range(arr[m]*r);
                for (MMAPIterator it = result.first; it != result.second; it++)
                {
                    if (it->second>m)
                        count++;
                }
			}
		}
	}
	return count;
}*/
//This method will archive O(n*log(n)) complexity time
long findTriplet(int arr[], int size, int d)
{
	map<int,int> mymap1, mymap2;
	long ret =0;
	for(int i =0; i < size; i++)
	{
		if(mymap2.count(arr[i]) count+= mymap2[arr[i]];
		if(mymap1.count(arr[i])) mymap2[arr[i]*d]+= mymap1[arr[i]];
		mymap1[arr[i]*d]++;
	}
}
int main()
{

    int arr[] = {1,4,16,64};
	int size = sizeof(arr)/sizeof(arr[0]);
	long ret = findTriplet(arr, size, 4);
	cout<<ret<<endl;
	return 0;
}
