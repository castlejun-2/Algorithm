#include <stdio.h>
int main(){
    int N=0,K=0;
    int A[10]={};
    int check=0;                                //동전의 갯수를 저장해줄 변수 선언
    scanf("%d %d",&N,&K);
    for(int i=0;i<N;i++) scanf("%d",&A[i]);
    for(int i=N-1;i>=0;i--){
        if(K/A[i]>=1){                          //자릿수가 맞아 떨어지는지 확인
            check+=K/A[i];                      //몫을 check 변수에 넣어준다
            K%=A[i];                            //나머지를 다시 K에 넣어 다음 최적의 동전을 계산
        }
        if(K==0) break;                         //나머지가 0이면 for문 탈출
    }
    printf("%d",check);
    return 0;
}
