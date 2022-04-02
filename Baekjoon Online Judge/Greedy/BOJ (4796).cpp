#include <iostream>
using namespace std;

int main(){
    int a,b,c,i=0;    
    while(1){
        cin >> a >> b >> c;
        if(a == 0) break;
        int sum=0;
        while(c >= b){                                   //남은 휴가 일수가 최대 캠핑일 보다 작아질 때 까지 반복
            sum+=a;
            c-=b;
        }
        if(a > c)                                        //남은 휴가 일수가 사용가능한 일수보다 작으면 남은 휴가일 수 +
            sum += c;
        else
            sum += a;                                    //남은 휴가 일수가 사용가능한 일수보다 크면 사용가능한 일 수 +
        cout << "Case " << ++i << ": " << sum << "\n";
    }
    return 0;
}
