#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
bool compare(const pair<int,string>& a,const pair<int,string>& b){           //sort함수 compare함수 재정립
  if(a.first==b.first){                                                     
    if(a.second.size()==b.second.size()){                                       
      return a.second < b.second;                                            //반복횟수가 같고 단어의 길이도 같다면 알파벳순으로 return 
    }
    else{
      return a.second.size() > b.second.size();                              //반복횟수만 같다면 단어의 길이가 긴순으로 return
    }
  }
  else{
    return a.first > b.first;                                                //반복횟수가 같지 않다면 많이 반복한 순으로 return
  }
}

int main(){
  int N=0,M=0;
  string str;
  vector<string> v;
  vector<pair<int,string>> vp;
  
  ios::sync_with_stdio(false);                                               //stdio와 iostream의 동기화를 끊어 독립적인 버퍼를 갖게해 실행속도를 개선해준다.
  cin.tie(0);                                                                //cin과 cout의 tie를 풀어서 속도를 개선해준다.
  
  cin >> N >> M;
  for(int i=0;i<N;i++){
    cin >> str;
    if(str.size()<M){                                                        //길이가 애초에 M 미만이라면 vecotor에 저장해주지 않는다.
      continue;
    }
    else{
      v.push_back(str);
    }
  }  
  sort(v.begin(),v.end());                                                   //같은 문자열이 붙어있도록 정렬을 한번 해준다.
  
  int cnt=v.size();
  vp.push_back(make_pair(1,v[0]));                                           //초기값으로 가장 앞의 값과 횟수를 pair vector에 push 해준다.
  
  for(int i=1;i<cnt;i++){
    if(v[i]==vp.rbegin()->second){                                           //해당 값이 가장 마지막에 push된 pair vector의 값과 같다면 해당 pair vector의 first에 있는 반복횟수 값을 증가시켜준다.
      vp.rbegin()->first++;
    }
    else{
      vp.push_back(make_pair(1,v[i]));                                       //만약 없던 영단어라면 pair vector에 추가해준다.
    }
  }
  sort(vp.begin(),vp.end(),compare);                                         //push된 pair vector을 재정립해준 함수순으로 재정렬해준다.
  cnt=vp.size();
  
  for(int i=0;i<cnt;i++){
    cout << vp[i].second << "\n";                                            //각 단어를 정렬된 순서대로 출력해준다.
  }
  return 0;
}
else{
  vp.push_back(make_pair(1,v[i]));                                       
}
