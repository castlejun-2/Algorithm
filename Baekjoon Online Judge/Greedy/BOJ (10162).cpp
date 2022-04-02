#include <iostream>
using namespace std;

int main(){
    int A=0,B=0,C=0,T=0;
    cin >> T;
    if(T%10!=0){                                        //1의자릿수가 존재한다면 구할 수 없으므로 -1 출력 후 바로 return
        cout << -1;
        return 0;
    }
    else{
        while(T!=0){                                    //T가 0이 될때까지 반복
            if(T>=300){                                 //A버튼(300초)를 눌러야 하는 횟수
                T-=300;
                A++;
            }
            else if(T>=60){                             //B버튼(60초)를 눌러야 하는 횟수
                T-=60;
                B++;
            }
            else if(T>=10){                             //C버튼(10초)를 눌러야 하는 횟수
                T-=10;
                C++;
            }
        }
    cout << A << " " << B << " " << C;                  //A와 B와 C를 각각 출력하고 return 해준다.
    return 0;
    }
}
