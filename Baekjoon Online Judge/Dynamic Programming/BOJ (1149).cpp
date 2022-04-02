#include <iostream>
using namespace std;

int min(int a,int b){
  return a>b ? b:a;
}

int main(){
  int N=0;
  int RGB[1001][3]={0};                                                      //각 Red,Green,Blue의 정보를 담고 있을 배열
  int dp[1001][3]={0};                                                       //dp[i][0]은 Red, dp[i][1]은 Green, dp[i][2]는 Blue를 택했을때의 최솟값을 담는 배열
  
  cin >> N;
  cin >> RGB[1][0] >> RGB[1][1] >> RGB[1][2];
  
  dp[1][0]=RGB[1][0],dp[1][1]=RGB[1][1],dp[1][2]=RGB[1][2];                  //초기 최솟값 설정
  
  for(int i=2;i<=N;i++){
    cin >> RGB[i][0] >> RGB[i][1] >> RGB[i][2];
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+RGB[i][0];                           //Red를 선택했다고 가정 후, 이전 값의 Green과 Blue의 최솟값과 자기자신을 더한 값을 저장
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+RGB[i][1];                           //Green를 선택했다고 가정 후, 이전 값의  Red와 Blue의 최솟값과 자기자신을 더한 값을 저장
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+RGB[i][2];                           //Blue를 선택했다고 가정 후, 이전 값의 Red와 Green의 최솟값과 자기자신을 더한 값을 저장
  }
  cout << min(min(dp[N][0],dp[N][1]),dp[N][2]);                              //최종 N번째에 저장되어 있는 dp[N]행에 위치한 배열 값들중 최솟값 선택 후 출력
  return 0;
}
