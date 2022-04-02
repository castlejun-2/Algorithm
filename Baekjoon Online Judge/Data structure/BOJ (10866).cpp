#include <iostream>
#include <deque>
using namespace std;

int main(){
    deque<int> dq;
    int N=0;
    cin >> N;
    for(int k=0;k<N;k++){
        string s;
        cin >> s;
        if(s=="push_front"){      //덱의 가장 앞에 입력
            int a;
            cin >> a;
            dq.push_front(a);
        }
        else if(s=="push_back"){  //덱의 가장 뒤에 입력
            int a;
            cin >> a;
            dq.push_back(a);
        }
        else if(s=="pop_front"){  //가장 앞의 값 pop
            if(dq.empty())
                cout << -1 << "\n";
            else{
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }
        else if(s=="pop_back"){   //가장 뒤의 값 pop
            if(dq.empty())
                cout << -1 << "\n";
            else{
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        }
        else if(s=="size"){       //덱의 크기 출력
            cout << dq.size()  << "\n";
        }
        else if(s=="empty"){      //덱이 비어있는지 확인
            if(dq.empty())
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
        else if(s=="front"){      //덱의 가장 앞의 값 출력
            if(dq.empty())
                cout << -1 << "\n";
            else
                cout << dq.front() << "\n";
        }
        else if(s=="back"){       //덱의 가장 뒤의 값 출력
            if(dq.empty())
                cout << -1 << "\n";
            else
                cout << dq.back() << "\n";
        }
    }
}
//덱의 기본 함수를 되짚는 문제였다.
