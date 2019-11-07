#include <bits/stdc++.h>
using namespace std;
#define INF 999
#define N 5
#define A 11

void coinChange(int d[], int C[], int S[]) {
  int i, p, min, coin;
  C[0] = 0;
  S[0] = 0;
  
  for(p = 1; p <= A; p++) {
    min = INF;
    for(i = 1; i <= N; i++) {
      if(d[i] <= p) {
        if(1 + C[p - d[i]] < min) {
          min = 1 + C[p - d[i]];
          coin = i;
        }
      }
    }
    C[p] = min;
    S[p] = coin;
  }
}

void coinSet(int d[], int S[]) {
  int a = A;
  while(a > 0) {
    cout<<" "<<d[S[a]];
    a = a - d[S[a]];
  }
}

void display(int arr[]) {
  int c;
  for(c = 0; c <= A; c++) {
    
	cout<<" "<<arr[c];
  }
  cout<<endl;
}

int main(void) {

  int d[N+1] = {0, 1, 2, 5,7,9};
  int C[A+1];
  int S[A+1];
  coinChange(d, C, S);
  cout<<"Min no. of coins :"<<C[A]<<endl;
  cout<<"Coin set :";
  coinSet(d, S);
  cout<<endl;
    
  return 0;
}
