#include<bits/stdc++.h>
using namespace std;

bool isMaxHeap(int a[], int n)
{

    int i, flag=0;
    for(i=1; i<=n/2; i++)
    {
        if(a[i] >= max(a[2*(i)], a[2*(i)+1]))
            {
                flag=1;
                continue;
            }
        else
            {
                 flag=0;
                 break;
            }
    }

    if(flag==1)
        return true;
    else 
        return false;
}

int main()
{

    int n, i;
    cout<<"Enter the size of array: ";
    cin>>n;
    int array[n+1];
    cout<<"Enter the elements: "<<endl;
    for(i=1; i<=n; i++)
        cin>>array[i];
 
    bool var=isMaxHeap(array, n);
    if(var)
        cout<<"Given array is a Max Heap"<<endl;
    else
        cout<<"Given array is not a Max Heap"<<endl;
        
    return 0;
 
}

