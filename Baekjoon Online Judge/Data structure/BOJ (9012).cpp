#include <iostream>
#include <string>
#include <stack>

int main(){
  int N=0;
  cin >> N;
  
  for(int i=0;i<N;i++){
    stack<char> s;
    string str;
    int check=1;                                                   //stack이 비어서 마지막 조건문을 비교 할 때, )가 들어와서 반복문 전에 끝난것인지 혹은 반복문이 끝까지 수행되고
                                                                   //끝난것인지를 확인해줄 변수
    cin >> str;
    for(int j=0;str[j];j++){                                       //str이 NULL문자를 만날 때 까지 반복
      if(str[j]=='(') s.push('(');                                 //s.push(str[j])도 가능하지만 성능적 측면에서 str[j]는 메모리에 접근해야 하므로 성능이 떨어진다.
      else if(str[j]==')'){
        if(!s.empty()) s.pop;                                      //stack이 비어있지 않다는건 앞에 '('문자가 존재했던 것이므로 그에 대응하는 ')' 문자를 만났음으로 stack을 pop
        else{
          check=0;
          break;
        }
      }
    }
    if(s.empty() && check==1) cout << "YES" << endl;               //stack이 비어있고, 중간에 else문에서 빠져나온것이 아닌 문자열만이 VPS를 만족
    else cout << "NO" << endl;
  }
  return 0;
}
