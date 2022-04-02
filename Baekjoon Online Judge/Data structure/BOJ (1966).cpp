#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++){
        int N=0,index=0,cnt=0;
        cin >> N >> index;
      
        queue<pair<int,int>> q;                   //pair queue로 index와 값 동시 관리
        priority_queue <int> check_q;             //우선순위 queue 선언
      
        for(int j=0;j<N;j++){
            int num=0;
            cin >> num;
            q.push({j,num});
            check_q.push(num);
        }
        //현시점에 우선순위 값으로 정렬된 check_q 와 index와 value로 값이 입력된 q 가 setting
      
        while(!q.empty()){                         //q가 비어지게 될때까지 반복이나 실제로 다 비어지기전에 break를 통해 탈출
            int q_index=q.front().first;
            int q_value=q.front().second;
            q.pop();
            
            if(check_q.top()==q_value){            //우선순위 queue의 가장 앞의 값과 현재 queue의 value가 같은지 확인
                check_q.pop();
                cnt++;
                if(q_index==index){                //index가 M에서 구하고 있는 index와 같은지 확인(혹여 다른 queue의 index가 M의 index와 동일한 value를 가질 수 있으므로)
                    cout << cnt << "\n";
                    break;                         //맞다면 현재 자신보다 먼저 출력된 녀석들을 제외한 자신의 출력순위를 출력하고 반복문 탈출
                }    
            }
            else
                q.push({q_index,q_value});         //우선순위 queue의 가장 앞의 값과 같지 않다면 다시 queue의 가장 뒤로 push
        }
    }
    return 0;
}

//pair queue와 우선순위 queue 자료구조를 빠르게 떠올리고 이를 응용하여야 하는 문제였다.
