#include <iostream>
using namespace std;

int main(){
  int N=0;
  int check=0;
  
  cin >> N;
  N=1000-N;
  
  if(N>=500){                                     //N이 500을 넘을 경우는 1번 혹은 0번이므로 if문 사용
    N-=500;
    check++;
  }
  while(N>=100){                                  //N이 100보다 작아질 때 까지 반복
    N-=100;
    check++;
  }
  if(N>=50){                                      //N이 50보다 클 경우는 위의 반복을 거칠경우 한번 혹은 0번이므로 if문 사용
    N-=50;
    check++;
  }
  while(N>=10){                                   //N이 10보다 작아질 때 까지 반복
    N-=10;
    check++;
  }
  if(N>=5){                                       //N이 5보다 클 경우는 위의 반복을 거칠경우 한번 혹은 0번이므로 if문 사용
    N-=5;
    check++;
  }
  check+=N;                                       //마지막 1의자리 숫자들은 check에 더해주면 됨으로 굳이 반복문을 사용하지 않음
  
  cout << check << endl;
  return 0;
}
