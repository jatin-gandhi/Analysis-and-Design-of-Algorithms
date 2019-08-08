#include <iostream>

using namespace std;

int MaxArray(int a[],int n)
{
    int maxx=a[0];
    for (int i=1; i<n; i++)
        if(maxx<a[i])
        maxx=a[i];
    return maxx;
}

int main()
{   int n ;
    cout<<"\nEnter the size of the array\n";
    cin>>n;
    int arr[n];
    cout<<"Enter the elements\n";
    for(int i=0;i<n;i++)
    cin>>arr[i];
    cout<<"Max Element in the given array : "<<MaxArray(arr,n);


}
