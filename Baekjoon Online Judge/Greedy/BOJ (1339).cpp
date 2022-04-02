#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool compare(int a,int b){              //sort를 내림차순으로 정렬
  return b<a;
}

int main(){
  int N=0;                              //문자열의 갯수를 받을 변수
  int len=0, sum=0;                     
  int i=0;
  string str;
  char ch;
  int arr[26]={0};
  
  cin >> N;
  for(i=0;i<N;i++){
    cin >> str;
    int strlen = str.length();           //str.length()가 자주 호출됨으로 메모리를 자주 접근하는것을 막기위해 strlen의 변수에 str.length() 대입
    for(int j=0;j<strlen;j++){
      ch=str[j];                         //ch에 가장 앞의 알파벳부터 넣어주면서 비교
      len=strlen-j-1;                    //해당 알파벳의 자릿수를 len에 저장
      arr[ch-'A']+=pow(10,len);          //해당 알파벳이 담당하는 배열에 자릿수를 더해준다
    }
  }
  
  sort(arr,arr+26,compare);              //가장 높은 자릿수를 가진 알파벳순으로 정렬
  
  i=0;                                   //배열의 인덱스를 나타내기위해 지역변수 재사용
  for(int k=9;k>0;k--)
    sum+=arr[i++]*k;                     //가장 높은 자릿수부터 9를 넣어주어 가장 큰 값이 되도록 만듦
    
  cout << sum;
  return 0;
}
