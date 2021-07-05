#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
  
    int N=0,T=0;
    cin >> N;
    
    int*arr = new int[N];                       //N만큼 배열을 동적할당하여준다.
    for(int i=0;i<N;i++)
        cin>>arr[i];
    
    sort(arr,arr+N);                            //탐색을 해주어야 하므로 배열을 정렬해주어야 한다.
    
    cin >> T;
    for(int i=0;i<T;i++){
        int k=0;
        cin >> k;
        auto up=upper_bound(arr,arr+N,k);       //k보다 큰 값이 나오는 첫 index를 반환하여준다.
        auto lw=lower_bound(arr,arr+N,k);       //k와 같거나 큰 값이 나오는 첫 inidex를 반환하여준다.
        cout<<up-lw<<" ";
    }
    delete[] arr;  //동적할당 해제
    return 0;
}
//기존 입출력을 동기화 해제하여주지 않으면, line20과 line23에서 입력과 출력이 동시에 이루어지므로, T 값이 커질 때 많은 시간이 걸릴 수 있어 시간이 오래 걸릴 수 있게 된다.
