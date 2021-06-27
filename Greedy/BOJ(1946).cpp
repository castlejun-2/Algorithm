#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<pair<int,int>> vt;
    int T=0,N=0;
    int a=0,b=0;
    cin >> T;
    for(int k=0;k<T;k++){
        int min = 100001;              //N이 100000까지 가능하므로 min값을 100001로 설정
        int sum = 0;
        vt.clear();                    //vector을 비워준다.
      
        cin >> N;
        for(int i=0;i<N;i++){
            cin >> a >> b;
            vt.push_back({a,b});
        }
      
        sort(vt.begin(),vt.end());     //오름차순으로 vector 정렬
      
        for(int i=0;i<N;i++){          //1차 서류심사순서도 낮은데 2차 면접심사점수까지 낮으면 sum에 반영되지 않는다
            if(min>vt[i].second){
                min=vt[i].second;      //1차 서류심사의 뒷 등수들은 2차 면접심사점수가 이전 1차 서류심사 순위자들보다 높아야 살아남는다
                sum++;
            }
        }
        cout << sum << "\n";
    }
    return 0;
}
