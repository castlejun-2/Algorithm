public class Solution {
    public int solution(int n) {
        int ans = 0;
        
        while (n>0) {
            if (n%2==0) n=n/2;    #짝수이면, 순간이동
            else {
                n-=1;             #홀수이면, 앞으로 전진
                ans++;
            }
        }

        return ans;
    }
}
