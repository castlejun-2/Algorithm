#include <iostream>
#include <algorithm>

using namespace std;

typedef struct{                                           //미팅의 시작시간과 끝나는 시간을 담은 구조체 선언
  int start;
  int end;
}meet_time;

int rule(const meet &a, const meet &b){                   //끝나는 시간이 같으면 먼저 시작하는 순서로 정렬 ex) 1 4, 4 4 이면 2개의 회의가 가능하기 때문에
  if(a.end==b.end)
    return a.start < b.start;
  return a.end < b.end;
}

int main(){
  int N=0;                                                //입력받을 미팅의 갯수를 받을 변수
  int check=0;
  cin >> N;
  
  meet_time* mt=new meet_time[N];                         //meet_time 구조체 동적 할당
  
  for(int i=0;i<N;i++){
    cin >> mt[i].start >> mt[i].end;
  }
  
  sort(mt,mt+N,rule);
  
  int cmp_end=-1;                                         //시작시간과 비교해줄 비교변수 선언
  for(int i=0;i<N;i++){
    if(mt[i].start>=cmp_end){                             //mt 배열의 시작시간이 cmp_end 보다 크다면 회의 시작 가능하므로 check를 증가 시킨 후, 해당 배열의 end 값으로 cmp_end 설정
      check++;
      cmp_end=mt[i].end;
    }
  }
  cout << check;
  delete[] mt;                                            //동적할당 해제
  return 0;  
}
