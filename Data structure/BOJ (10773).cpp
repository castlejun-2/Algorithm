#include <iostream>
#include <stack>
using namespace std;

int main(){
  int N=0;
  stack<int> s;
  int num=0,sum=0;
  
  cin >> N;
  for(int i=0;i<N;i++){
    cin >> num;
    if(num!=0){
      sum+=num;
      s.push(num);
    }
    else{
      num=s.top();
      sum-=num;
      s.pop();
    }
  }
  cout << sum;
  return 0;
}
