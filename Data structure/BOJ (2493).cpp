#include <iostream>
#include <stack>
using namespace std;

int main(){
  stack<pair<int,int>> s;
  int N=0,height=0;
  
  cin >> N;
  int* index=new int[N];                                  //자신이 수신하는 탑의 위치를 나타내줄 배열 동적 할당
  
  cin >> height;                                          //스택에 넣기 위해 첫 탑의 높이 입력
  s.push(make_pair(1,height));                            //첫번째 탑의 높이와 인덱스를 s.first, 와 s.second에 각각 넣어준다
  index[0]=0;                                             //첫 탑은 수신할 수 있는 탑이 없기에 미리 0으로 초기화
  
  for(int i=1;i<N;i++){
    cin >> height;
    if(height > s.top().second){                          //stack에 들어있는 앞 탑의 높이를 비교해주어 자신보다 큰 값인지 먼저 확인
      while(!s.empty() && height > s.top().second){       //stack에 들어가기 직전의 탑이 자신보다 높이가 큰 탑을 만날 때 까지 의미없는 작은 높이의 탑들을 pop()하여 준다.
        s.pop();
      }
      if(s.empty()) index[i]=0;                           //만약 자신이 이전 탑들중 높이가 가장 크다면 수신 할 타워가 없기 때문에 index[] 배열의 값을 0으로 설정
      else index[i]=s.top().first;                        //자신보다 높은 탑을 만났다면 s.top().first에 들어있는 해당타워의 위치를 index[] 배열에 저장
      
      s.push(make_pair(i+1,height));                      //자신의 탑의 위치와 높이를 stack에 푸쉬하여 뒤의 값이 자신을 비교할 수 있도록 설정
    }
    else{
      index[i]=s.top().first;                             //stack의 top에 들어있는 값이 자신보다 크다면 해당 타워를 수신하므로 해당 탑의 s.top().first 값을 index[] 배열에 저장
      s.push(make_pair(i+1,height));
    }
  }
  
  for(int i=0;i<N;i++) cout << index[i] <<" ";            //각 타워가 수신하는 탑의 위치를 출력
  
  return 0;
}
