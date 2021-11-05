#include <iostream>
#include <string>
using namespace std;

int main(){
  int stack[10000]={};                                //스택을 구성할 저장공간
  int top=-1;                                         //스택의 top 위치를 나타낼 변수
  string cmd=NULL;                                    //명령어를 받을 변수
  int N=0;                                            //명령어의 갯수를 받을 변수
  
  cin >> N;
  for(int i=0;i<N;i++){
    cin >> cmd;
    if(cmd=="push"){                                  //push 명령어가 들어오면 그 다음에 들어올 정수를 받아 top을 증가 시킨 후 stack의 top에 저장
      top++;
      int X=0;
      cin >> X;
      stack[top]=X;
    }
    else if(cmd=="pop"){                              //pop 명령어가 들어오면 현재의 top 값을 보여준 뒤 top의 위치를 감소
      if(top==-1){
        cout << "-1" << endl;
      }
      else{
        cout << stack[top] << endl;
        top--;                                       
      }
    }
    else if(cmd=="size"){                             //size 명령어가 들어오면 현재 스택의 크기이므로 top에 +1을 해준 값을 출력(top은 index이기 때문에 0부터 시작하므로)
      cout << top+1 << endl; 
    }  
    else if(cmd=="empty"){                            //empty 명령어가 들어오면 현재 top의 위치를 확인해준 후 해당 결과에 맞는 값 출력
      if(top==-1) cout << "1" << endl;
      else        cout << "0" << endl;
    }
    else if(cmd=="top"){                              //top 명령어가 들어오면 현재 top의 위치를 출력
      if(top==-1){
        cout << "-1" << endl;
      }
      else{
        cout << stack[top] << endl;
      }
    }
    else{
      cout << "It is not right command" << endl       //다른 명령어가 들어온다면 "옳바른 명령어가 아닙니다" 를 출력
    }
  }
  return 0;
}
