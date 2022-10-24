class Solution {
    public long solution(int n) {
        long answer = 0;
        long first = 1;
        long second = 2;
        if (n==1) return 1;
        if (n==2) return 2;
        
        for (int i=3; i<n; i++) {     //dp[i]는 dp[i-1]에 +1을 한것과, dp[i-2]에 +2를 한 결과이다.
            long tmp = first;
            first = second;
            second = (second+tmp)%1234567;  
        }
        
        return (first+second)%1234567;
    }
}
