#include <stdio.h>
int max(int a,int b){                                 //두 조건중 최대값 반환
  if(a>b) return a;
  else return b;
}  
int main(){
  int N=0;                                            //개단의 개수
  int a[300];                                         //각 개단의 점수
  int sum[300];                                       //각 개단까지의 최대합
    
  scanf("%d",&N);
  for(int i=0;i<N;i++) scanf("%d",a[i]);
  
  sum[0]=a[0];
  sum[1]=a[0]+a[1];
  sum[2]=max(a[0]+a[2],a[1]+a[2]);                    //3번째 계단부터 비교해줘야 할 대상이 생기고, 4번째 개단부터 규칙이 생기는것을 알 수 있다.
  
  for(int i=3;i<N;i++){
    sum[i]=max(sum[i-2]+a[i],sum[i-3]+a[i-1]+a[i]);   //2번의 조건으로 인하여, 이전(i-1)의 계단을 밟으면 전전(i-2)의 계단을 밟을 수 없으므로 전전전(i-3)까지의 최대합과
  }                                                   //더해주어야 하고, 이전(i-1)의 계단을 밟지 않았으면 전전(i-2)의 계단까지의 최대핪과만 더해주면 된다.
  
  printf("%d",sum[N-1]);
  return 0;
}
