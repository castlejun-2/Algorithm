#include <iostream>
using namespace std;

int main(){
  int N=0;
  cin >> N;
  int* DP=new int[N+1];                                      //1부터 N까지의 각 자신의 숫자에 최소횟수를 담을 배열 동적할당
  DP[1]=0;
  
  for(int i=2;i<=N;i++){
    DP[i]=DP[i-1]+1;                                         //일반적으로 i는 i-1이 가진값에 +1이 더해진 값을 갖는다
    if(i%3==0)                                               //만약 i가 3으로 나누어진다면, i/3의 값에 3을 곱하면 자신임으로 DP[i/3]에 +1을 값을 가지고,
      DP[i]=DP[i]>DP[i/3]+1 ? DP[i/3]+1:DP[i];               //그 값과 현재 DP[i-1]+1로 얻어진 DP[i] 의 값중 더 작은 값을 선택하게 된다.
    if(i%2==0)                                               //만약 3과 2의 공배수가 나온다면 위의 if(i%3==0)의 조건문에서 얻어진 DP[i]값과
      DP[i]=DP[i]>DP[i/2]+1 ? DP[i/2]+1:DP[i];               //현재 이 조건문을 비교하여 더 작은값을 DP[i]는 선택하게 될 것이다.
  }   
  cout << DP[N] << endl;
  return 0;
}
