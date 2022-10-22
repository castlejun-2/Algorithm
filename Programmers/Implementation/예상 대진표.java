class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        
        while (a!=1 | b!=1) {     #둘 다 1이 된다면(최종라운드) 종료
            if ((a+1)/2==(b+1)/2) #같은 라운드 그룹에 속한다면 return
                return answer;
            else {
                a=(a+1)/2;        #다음 그룹으로 진출
                b=(b+1)/2;        #다음 그룹으로 진출  
                answer++;         #라운드 증가
            }
        }
        return answer;
    }
}
