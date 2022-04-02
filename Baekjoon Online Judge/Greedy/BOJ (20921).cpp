#include <iostream>
using namespace std;

int main(){
  int N=0,K=0;
  cin >> N >> K;
  
  int* arr=new int[N+1];                            //배열 동적할당
  int num=1;                                        //나눠주게 될 쪽지의 값 초기화
  int index=N;                                      //배열의 인덱스 공간 변수 선언
  
  while(K!=0){                                      //그렇고 그런사이가 다 찰때까지 반복
    if(K>=index){                                   
      arr[index--]=num++;                           //그렇고 그런사이가 현재의 index 즉 남은공간보다 크다면 배열의 가장 뒤에 가장 작은 쪽지값 전달
      K-=index;                                     //남은 그렇고 그런사이는 N-1만큼 이전 명령문에서 달성했으므로 index만큼 빼준다.
    }
    else{
      arr[K+1]=num++;                               //그렇고 그런사이가 남은 공간보다 적게 남았다면 K+1공간에 현재 가장 작은 num을 주고 반복문 종료
      K=0;
    }
  }
  for(int i=1;i<=N;i++){                            //위의 else문에서 K+1에 가장 작은 값을 설정해주면 오름차순으로 정렬시 해당 남은 공간=index만큼 그렇고 그런사이가 형성됨
    if(arr[i]==0){                                  //배열이 차지 않은 부분들을 오름차순으로 쭉 전달
      cout << num++ << " ";
    }
    else{
      cout << arr[i] << " ";
    }
  }
  return 0;
}
