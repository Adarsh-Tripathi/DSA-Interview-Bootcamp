#include <bits/stdc++.h>
using namespace std ;


int main() {

cout << "Enter the number of element in array";
int n;
cin >> n;

vector<int> arr(n);   //int arr[n];

cout << " Enter " << n << "integer: " << endl;
for(int i = 0 ; i < n ; i++) 
    {
        cin >> arr[i];
    }

int gov = 0;
int unique = 1;
int cm = 1;

while(cm < n)
{
    if(arr[cm] == arr[cm-1])
    {   
        arr[cm]++;
        continue;
    }    
    else
    {
        arr[gov+1]=arr[cm];
        gov++;
        unique++;
        cm++;
    }
}
return 0 ;
}
