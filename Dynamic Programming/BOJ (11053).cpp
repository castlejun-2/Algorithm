#include <iostream>
using namespace std;

int main()
{
    int N;
    int max=0;
    cin >> N;
    int *arr=new int[N];                                       //배열의 value를 받을 arr 배열 동적 할당
    int *dp=new int[N];                                        //수열의 길이를 담을 dp 배열 동적 할당
    for(int i=0;i<N;i++){
        cin >> arr[i];
        dp[i]=1;                                                //모든 dp 값은 자기 자신의 수열이 1이므로 1로 초기화
    }
    for(int i=1;i<N;i++){
        for(int j=0;j<i;j++){
            if(arr[i]>arr[j] && dp[i]<=dp[j]){                  //자신 이전의 배열 값이 자기보다 작다면 이전 배열이 쌓아온 dp값에 자기 자신을 1 더해줌
                dp[i]=dp[j]+1;                                  //이때 10 20 10 30 50 40 와 같을 때 30(Index 3 기준)에서 10(Index 2)의 dp 값인 1이 자신을 덮어 쓰게 될
            }                                                   //경우를 방지하여준다.
        }
    }
    for(int i=0;i<N;i++){
        if(dp[i]>max)
            max=dp[i];                                          //최고값 출력
    }
    cout << max;
    //동적할당 해제  
    delete[] arr; 
    delete[] dp;
    return 0;
}
//동적프로그래밍 기법을 어떻게 활용해야 할지 바로 떠오르지 않아 고전했던 문제이다. 특히 새로운 값이 자신을 덮어쓸 경우를 어떻게 해야할지 고민을 많이 한 문제이다.
