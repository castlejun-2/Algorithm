#include <iostream>
using namespace std;

int main()
{
    int N=0;
    long long sum=0;
    cin >> N;
    
    long long *rt = new long long[N];               //route(길) 동적할당
    long long *lt = new long long[N+1];             //location(장소) 동적할당
    
    for(int i=0;i<N-1;i++)
        cin >> rt[i];

    for(int i=0;i<N;i++)
        cin >> lt[i];
        
    for(int i=0;i<N;i++){
        sum+=(lt[i]*rt[i]);                         //자신의 위치에서 다음까지의 길 합산
        
        if(lt[i]<lt[i+1]){
            int j=i+1;
            long long temp=0;
            for(;lt[i]<lt[j];j++)                   //현재 자신의 주유소(장소)보다 적은 주유소(장소)를 찾을때 까지 미리 기름 충전
                temp+=lt[i]*rt[j];
            sum+=temp;                              //새로운 주유소를 찾기 이전까지의 합을 누적덧셈에 덧셈
            i=j-1;                                  //i의 값을 새로운 주유소(장소) 이전의 index로 설정(->다음의 i++을 계산하여)
        }    
    }
    cout << sum;  
    //동적할당 해제
    delete[] rt;                                    
    delete[] lt;
    return 0;
}
