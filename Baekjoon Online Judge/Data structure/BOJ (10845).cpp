#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main(){
  int N=0;                                                                  //변수 선언 및 초기화 과정
  queue<int> q;
  string str={};
  cin >> N;
  
  for(int i=0;i<N;i++){                                                     //명령어 갯수 N만큼 반복
    cin >> str;
    if(str=="push"){                                                        //queue의 push()함수
      int x;
      cin >> x;
      q.push(x);
    }
    else if(str=="pop"){                                                    //queue의 pop()함수
      if(q.empty()) cout << "-1" << endl;
      else{
        cout << q.front() << endl;
        q.pop();
      }
    }
    else if(str=="size"){                                                   //queue의 size()함수
      cout << q.size() << endl; 
    }  
    else if(str=="empty"){                                                  //queue의 empty()함수
      if(q.empty()) cout << "1" << endl;
      else cout << "0" << endl;
    } 
    else if(str=="front"){                                                  //queue의 front()함수
      if(q.empty()) cout << "-1" << endl;
      else cout << q.front() << endl;
    }
    else if(str=="back"){                                                   //queue의 back()함수
      if(q.empty()) cout << "-1" << endl;
      else cout << q.back() << endl;
    }
  }
  return 0;
}
