#include <iostream>
using namespace std;

int main(){
  int T=0;
  cin >> T;
  int DP[11]={};                                              //정수 n이 11보다 작으므로 11크기의 배열을 생성해준다                      
  
  DP[1]=1;
  DP[2]=2;
  DP[3]=4;
  
  for(int i=0;i<T;i++){                                       
    int test=0;                                               //쓰레기값이 들어감을 방지해, 반복마다 test 값을 초기화해준다.
    cin >> test;                                              //테스트 할 값을 입력받는다
    for(int j=4;j<=test;j++){                                 //1-3의 index는 초기값으로 사용되었으므로 4부터 test값 까지 조건문을 반복해준다
      DP[j]=DP[j-3]+DP[j-2]+DP[j-1];                          //동적 프로그래밍 기법을 이용하여 알고리즘을 작성
    }
    cout << DP[test] <<endl;
  }
  return 0;
}
