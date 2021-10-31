#include <iostream>
using namespace std;
    
int fibonacci(int a,int b){
    int c=a+b;
    return c;
}

int main()
{
    int a[21]={}; //20번째 수의 피보나치까지 구하기 위해 21까지의 배열 선언
    int n=0;
    //a[0]과 a[1]값만 초기화
    a[0]=0;
    a[1]=1;
    
    cin >> n;
    for(int i=2;i<=n;i++)
        a[i]=fibonacci(a[i-1],a[i-2]);       //An = An-1 + An-2(n>=2) 이므로 다음과 같은 식 성립
    
    cout << a[n];
    return 0;
}
