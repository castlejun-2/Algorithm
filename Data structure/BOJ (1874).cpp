#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main(){
  int N=0,index=0;                                                        //코드에 필요한 변수 및 동적선언 부분
  stack<int> s;
  vector<char> v;
  cin >> N;
  
  int *seq=new int[N];                                                    //seq[]에 성립하는지 확인하기 위한 수열 입력
  for(int i=0;i<N;i++)
    cin >> seq[i];
  
  for(int i=1;i<=N;i++){                                                  
    s.push(i);                                                            //수열이 잘 쌓이는지 확인하기 위해 1부터 push 해준다.                                                                                                                                                                                                  
    v.push_back('+'); 
    while(!s.empty() && s.top()==seq[index]){                             //stack의 top값과 seq[]의 같으면 빼준다
      s.pop();
      v.push_back('-');
      index++;
    }
  }
  
  if(!s.empty()){                                                         //수열이 성립하기 위해선 원하는 수열의 배열 사이에 다른 값이 들어가면 즉 pop()을 해야하는 상황이 나와선 안된다.
    cout << "No\n";                                                       //만약 임의의 값이 끼어있다면 그 값으로 갈 수 없으므로(=pop()을 해야하기때문에) 스택엔 값이 남게 된다.
    return 0;
  }
  
  for(int i=0;i<v.size();i++)
    cout << v[i] << "\n";
    
  return 0;
}
