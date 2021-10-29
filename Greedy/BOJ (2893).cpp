#include <stdio.h>
int main(){
  int N=0;
  int check=0;
  scanf("%d",&N);
  if(N%5==0){
    printf("%d",N/5);
    return 0;
  }
  while(N>0){
    N=N-3;                     //큰 값(5)이 아닌 작은 값(3)을 반복하여 빼주며 줄여나아간다.
    check++;                   //check 값을 늘려가면서 3킬로그램의 봉지 개수를 확인하여줄 수 있도록 해준다.
    if(N%5==0{
      printf("%d",check+N/5);  //check+N을 통해 원하는 봉지의 총 갯수를 하나의 코드로 출력할 수 있게 해준다.
      return 0;
    }
  }
  printf("-1");                //3킬로그램과 5킬로그램의 조합으로는 해결 할 수 없을 때를 처리하여준다.
  return 0;
}  

     
