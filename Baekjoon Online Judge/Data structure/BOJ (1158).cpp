#include <iostream>
#include <queue>
using namespace std;

int main(){ 
  int N=0,K=0;                                              //변수선언 초기화 부분
  queue<int> q;
  
  cin >> N >> K;
  for(int i=1;i<=N;i++){                                    //1부터 N까지의 값을 queue에 push()
    q.push(i);
  }
  cout << "<";
  
  while(q.size()!=1){
    for(int j=0;j<K-1;j++){                                 //K번째의 숫자가 가장 앞에 올 수 있도록 K-1까지 반복
      q.push(q.front());                                    //K번째 앞의 숫자들은 맨 뒤로 이동시켜주고 pop()
      q.pop();
    }
    cout << q.front() << ", ";                              //K번째 숫자가 맨 앞에 있으므로 queue의 front값을 출력해준 후 pop()
    q.pop();
  }
  cout << q.front() << ">";                                 //마지막 queue의 원소를 출력해주고 괄호를 닫아준 후 pop()
  q.pop();
  
  return 0;
}
