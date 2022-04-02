#include <iostream>
using namespace std;

int main(){
  int N=0;
  cin >> N;
  int* dp=new int[N+1];                               //N+1만큼 dp 동적할당                 
  
  dp[1]=1;
  dp[2]=2;
  for(int i=3;i<=N;i++){
    dp[i]=(dp[i-1]+dp[i-2])%10007;                    //피보나치와 같이 이전항과 이전전항을 더한값이 dp[i]임을 인지하고 값이 너무 커져 정수형 범위를 
  }                                                   //넘어갈 수 있으므로 10007의 나머지를 미리 구해주며 정수형 범위를 넘지 않도록 값을 저장해 나아가준다.
  cout << dp[N] << endl;
  delete[] dp;                                        //동적할당해제
  return 0;
}
