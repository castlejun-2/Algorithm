#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int N;
    priority_queue<int,vector<int>,greater<int>> pq;            //오름차순 우선순위 큐 선언
    int sum=0;
    
    cin >> N;
    for(int i=0;i<N;i++){
        int a=0;
        cin >> a;
        pq.push(a);
    }
    while(pq.size()!=1){
        int a=pq.top(); pq.pop();                               //pq 가장 앞의 값(=가장 작은 값)을 a에 대입
        int b=pq.top(); pq.pop();                               //pq 가장 앞의 값(=위에서 팝한 값 그 다음으로 작은 값)을 b에 대입
        int s=a+b;                                              //a와 b를 합친 값을 s에 저장
        sum+=s;
        pq.push(s);                                             //더한 수를 다시 하나의 수로 생성하여 비교할 수 있도록 pq에 삽입
    }
    cout << sum;
    return 0;
}
/*우선순위큐를 내림차순으로 한다면 쉬운 문제였다. 내가 작성한 답 말고 다른 풀이도 보았는데, 위의 우선순위큐를 오름차순으로 설정하지 않고 line 15에서 push를 -a로 하여 음수로 받은 후
위의 line 21에서 sum+=(-s)로 구현하여 양수로 바꿔 대입한 분을 보았을 때 위의 코드와 큰 차이가 없으나, 생각하지 못하게 응용을 하여 다소 신기하였다.*/
