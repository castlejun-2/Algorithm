import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0,0};
        Map<String,Integer> m = new HashMap<>();
        m.put(words[0],0);
        
        for(int i=1; i<words.length;i++) {
            if (m.containsKey(words[i]) | words[i-1].charAt(words[i-1].length()-1)!=words[i].charAt(0)) { //키가 존재하고, 끝말이 다르다면 틀림
                answer[0]=(i%n)+1;
                answer[1]=(i/n)+1;
                return answer;
            m.put(words[i],0);  //그렇지 않다면, key 삽입
        }

        return answer;
    }
}
