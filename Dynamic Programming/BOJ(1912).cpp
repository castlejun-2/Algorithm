#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    int *arr=new int[N];      //각 배열의 값을 담을 변수
    int *dp=new int[N];       //각 배열까지의 최대 연속 값을 담을 변수
    
    for(int i=0;i<N;i++){
        cin >> arr[i];
        dp[i]=arr[i];
    }
    
    int max=dp[0];            //최종 결과값을 알려줄 변수
    
    for(int i=1;i<N;i++){           //연속된 합을 구하는 것이므로, 이전의 dp 값들에 자신의 arr을 더한 값이 자신의 현재 arr보다 작다면 이전 연속값들은 무의미 해진다.
        if(dp[i]<dp[i-1]+arr[i])
            dp[i]=dp[i-1]+arr[i];
        if(max<dp[i])               //결정된 dp[i] 값이 이전의 max 값보다 크다면 갱신하여 준다.
            max=dp[i];
    }
    cout << max;
    //동적 해제
    delete[] arr;
    delete[] dp;  
    return 0;
}
