#include <iostream>
using namespace std;

int main(){
  int N=0,K=0;
  int ret0[41]={},ret1[41]={};                                     //0과 1이 return 되는 횟수를 담은 배열을 N은 40이하이므로 41크기까지 생성
  cin >> N;
  
  ret0[0]=1,ret1[0]=0;                                             //0일때 0과 1이 return 되는 횟수 초기화
  ret0[1]=0,ret1[1]=1;                                             //1일때 0과 1이 return 되는 횟수 초기화
  
  for(int i=0;i<N;i++){
    cin >> K;
    for(int j=2;j<=K;j++){
      ret0[j]=ret0[j-1]+ret0[j-2];                                 //fibonacci(n)=fibonacci(n-1)+fibonacci(n-2) 이므로 n-1항과 n-2항 수열의 각 ret을 더하면 n의 ret을 얻는다
      ret1[j]=ret1[j-1]+ret1[j-2];
    }
    cout << ret0[K] << " " << ret1[K] << endl;                     //ret0과 ret1 배열에 저장된 수를 출력해준다
  }
  return 0;
}
