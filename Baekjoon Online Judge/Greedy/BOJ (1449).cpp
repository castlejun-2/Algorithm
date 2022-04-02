#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  
    int N=0,L=0; //N: 수리가 필요한 구멍의 갯수, L: 테이프의 길이
    
    cin >> N >> L;
    
    int *arr=new int[N];  //수리가 필요한 구멍의 갯수만큼 동적할당
  
    for(int i=0;i<N;i++)
        cin >> arr[i];
    
    sort(arr,arr+N);  //구멍난 위치를 오름차순으로 정렬
  
    float range=(float)(arr[0]-0.5+L);  //초기 범위 설정
    int TAPE=1;
    
    for(int i=1;i<N;i++){
        if(range<arr[i]+0.5){ //현재 설정된 범위를 벗어나면, 새로운 범위를 설정하고 테이프의 갯수를 증가
            range=(arr[i]-0.5+L); 
            TAPE++;
        }
    //범위를 벗어나지 않는다면, 테이프의 갯수도 증가하지 않고 다음 for 문으로 이동
    }
    cout << TAPE;
    delete arr;    //동적할당 해제
    return 0;
}
//테이프의 길이 + 앞뒤로 0.5만큼 필요함을 인지하고, range 범위 이내에 arr[i]의 배열이 위치하면 테이프의 갯수를 증가시키지 않고 다음 for 문으로 넘어간다
//즉, 범위를 통해 해당 배열의 값에 그때그때 새로운 테이프 여부를 파악하여 넘어가주는 Greedy 형식의 알고리즘 문제이다. 
