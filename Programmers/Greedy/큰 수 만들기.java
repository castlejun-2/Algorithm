import java.util.*;

class Solution {
    public String solution(String number, int k) {
        StringBuilder answer = new StringBuilder("");
        int startIdx = 0;
        
        while (answer.length()<number.length()-k) {
            int searchIdx = k+answer.length()+1;
            int max=0;
            for(int i=startIdx; i<searchIdx; i++){    //뒤의 자릿수를 고정하고, 앞에서 가장 큰 수를 탐색
                if (max < number.charAt(i)-'0') {
                    max = number.charAt(i)-'0';
                    startIdx = i+1;                   //가장 큰 수 다음의 index부터 탐색
                }
            }
            answer.append(Integer.toString(max));     //가장 큰 수를 이어붙힌다.
        }
        
        return answer.toString();
    }
}
