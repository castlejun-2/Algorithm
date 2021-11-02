#include <stdio.h>
int main(){
  int N=0;
  int line[200]={};
  int Lis[200]={};                                //각 line 배열의 Longest Increasing Subsequence(LIS) 값을 저장해줄 배열
  
  scanf("%d",&N);
  for(int i=0;i<N;i++) scanf("%d",&line[i]);
  
  int max=Lis[0];                                 //가장 큰 Lis 값을 저장해줄 변수
  Lis[0]=1;                                       //자기자신의 순서관계도 또한 1이므로 line[0]값을 1로 미리 초기화
  
  for(int i=1;i<N;i++){
     Lis[i]=1;
     for(int j=0;j<i;j++){
       if(line[i]>line[j] && Lis[j]+1>Lis[i]){    //line[i]가 순서관계가 맞는지 확인해주고, Lis 값이 더 작은 값으로 재갱신되는것을 방지
         Lis[i]=Lis[j]+1;
       }
     if(max<Lis[i]) max=Lis[i];                   //가장 큰 Lis 값 갱신  
  }
  
  printf("%d",N-max);                             //순서관계가 맞지 않는 값들을 바꿔주면 해당 자리 이동의 최솟값을 얻을 수 있다
  return 0;
}
