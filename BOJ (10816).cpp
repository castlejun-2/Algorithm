#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N=0,T=0;
    cin >> N;
    
    int*arr = new int[N];
    for(int i=0;i<N;i++)
        cin>>arr[i];
    
    sort(arr,arr+N);                          //탐색을 위해 배열을 정렬하여 준다.
    
    cin >> T;
    for(int i=0;i<T;i++){
        int k=0;
        cin >> k;
        auto up=upper_bound(arr,arr+N,k);     //k로 입력된 값 보다 초과된 값의 첫 index가 반환된다.
        auto lw=lower_bound(arr,arr+N,k);     //k로 입력된 값의 첫 index가 반환된다.
        cout<<up-lw<<" ";
    }
    return 0;
}
//vector로 풀면 시간이 더 단축된다. 이 때 입출력 값들이 동시에 진행되어 sync를 해제하지 않으면 시간이 상당히 오래걸렸다.
