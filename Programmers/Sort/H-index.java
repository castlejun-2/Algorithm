import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int answer = 0;

        for (int i=0; i<citations.length; i++) {
            int h = citations.length-i; //논문의 갯수
            if (citations[i]>=h){       //논문의 갯수(h-index)보다 많이 인용되었다면 종료
                answer=h;   
                break;
            }
        }
        
        return answer;
    }
}
