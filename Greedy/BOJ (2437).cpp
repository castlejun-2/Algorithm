#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N=0;
    cin >> N;
    
    int *arr=new int[N];
    for(int i=0;i<N;i++)
        cin >> arr[i];
    
    sort(arr,arr+N);            //arr을 오름차순으로 정렬
    
    if(arr[0]!=1)
        cout << "1";
    else{
        int sum=1;
        for(int i=1;i<N;i++){   
            if(arr[i]>sum+1)    //누적합의 +1 보다 arr[i]에 든 수가 크다면 누적합+1의 값을 표현할 수 없게 된다.
                break;
            else
                sum+=arr[i];    //그 외에 arr[i]가 누적합+1보다 같거나 작다면 sum+arr[i]까지의 숫자는 전부 표현가능해지므로 더해준다.
        }
        cout << sum+1;          //break를 만나거나, 마지막 반복까지 break문을 만나지 않아 for문을 마친다면 누적합+1이 표현할 수 없는 최솟값이 된다.
    }
    delete[] arr;               //동적 할당 해제
    return 0;
}
