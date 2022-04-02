#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int N=0,cnt=2;
  cin >> N;
  
  int *arr=new int[N];
  for(int i=0;i<N;i++){
    cin >> arr[i];
  }
  
  sort(arr,arr+N);                              //각 로프의 중량을 오름차순으로 정렬
  int max=arr[N-1];                             //가장 큰 로프의 중량을 max 값으로 설정
  
  for(int i=N-2;i>=0;i--){
    if(arr[i]*cnt>max){                         //로프의 최대 무게는 최소로프*사용하는 로프의 갯수에서 나오므로 max값과 비교하며 반복
      max=arr[i]*cnt;
    }
    cnt++;
  }
  cout << max << endl;                          //최대값 출력
  return 0;
}
