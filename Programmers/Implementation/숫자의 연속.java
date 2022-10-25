class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i=1;i<=n;i++){         #i부터 연속된 숫자 탐색
            int tmp=i;
            for (int j=i+1;j<=n;j++){
                tmp+=j;
                if (tmp==n) answer++;
                else if (tmp>n) break;  #n을 넘어간다면 반복 종료
            }
        }
        
        return answer+1;      #자기 자신으로 만드는 방법 +1
    }
}
