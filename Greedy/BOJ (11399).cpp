#include <stdio.h>
Selection_Sort(int* p, int n){             //삽입정렬 함수
  for(int i=0;i<n-1;i++){                  //N-1까지 Swap 해줄 대상 배열인덱스 설정
    for(int j=i+1;j<n;j++){                //두번째 중첩 for문에서는 N(마지막 인덱스)까지 비교
      if(p[i]>p[j]){                       //Swap 과정
        int temp=p[i];
        p[i]=p[j];
        p[j]=temp;
      }
    }
  }
  return 0;
}  
int main(){
  int P[1000]={};
  int N=0;
  int sum=0;                               //총 대기시간을 저장해줄 변수                        
  scanf("%d",&N);
  for(int i=0;i<N;i++) scanf("%d",&P[i];  
  
  Selection_Sort(P,N);
  
  for(int i=0;i<N;i++){
    for(int j=i;j<N;j++){
      sum+=P[i];                           //가장 낮은 배열인덱스부터 계속 불려 더해짐으로 중첩for문 통해 구현
    }
  }  
  printf("최소 대기 시간: %d",sum);
  return 0;
}  
