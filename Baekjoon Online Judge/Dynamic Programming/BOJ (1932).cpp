#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    int *sum=new int[N+1];                              //합을 구해줄 배열 동적 할당
    int *cmp=new int[N+1];                              //더한값을 임시로 저장해줄 배열 동적 할당
    int *get=new int[N+1];                              //값을 받을 배열 동적 할당
    int max=0;
    sum[0]=get[0]=0;
    for(int i=0;i<N;i++){
        sum[i+1]=0;
        for(int j=1;j<=i;j++){
            cin >> get[j];
            if(sum[j-1]+get[j]>sum[j]+get[j])           //이 전 층에 있던 대각선의 값들 중 자신의 더한값이 큰값을 임시 배열에 저장           
                cmp[j]=sum[j-1]+get[j];
            else
                cmp[j]=sum[j]+get[j];
        }
        for(int k=1;k<=i;k++)                           //임시 배열의 값을 sum배열에 복사
            sum[k]=cmp[k];
    }
    for(int i=1;i<N+1;i++){
        if(sum[i]>max)                                  //가장 큰 값이 대각선으로 내려왔을 때의 최대 값이다.
            max=sum[i];
    }
    cout << max;                                        //최댓값 출력
    //동적 해제
    delete[] sum;
    delete[] get;
    delete[] cmp;
    return 0;
}
