import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = board.length*board[0].length;
        int dp[][] = new int[board.length+2][(board[0].length)+2];
        HashMap<String,Integer> map = new HashMap<>();
        
        for (int i=0; i<skill.length; i++) {    //변화량 저장
            int type=skill[i][0],r1=skill[i][1],c1=skill[i][2],r2=skill[i][3],c2=skill[i][4],degree=skill[i][5];
            if (type==1) degree=-degree;    //공격일 경우
            dp[r1+1][c1+1]+=degree;
            dp[r2+2][c1+1]-=degree;
            dp[r1+1][c2+2]-=degree;
            dp[r2+2][c2+2]+=degree;
        }

        for (int i=1; i<=board.length; i++) {       //특정 구간까지의 변화량 누적합을 더한다.
            for (int j=1; j<=board[0].length; j++)
                dp[i][j]=dp[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1];
        }
        
        for (int i=1; i<=board.length; i++) {       //자기 자신의 변화량과 기존 초기값을 더한다.
            for (int j=1; j<=board[0].length; j++) {
                if (board[i-1][j-1]+dp[i][j]<=0) answer--;
            }
        }
        
        return answer;
    }
}
