import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String,Integer> map = new HashMap<>();
        
        for (int i=0;i<clothes.length;i++){
            map.put(clothes[i][1],map.getOrDefault(clothes[i][1], 0) + 1);
        }

        for (String key : map.keySet()) {
            answer *= map.get(key)+1;           //현재 의류를 입거나 안입거나 하는 경우의 수
        }
        
        return answer-1;                        //모든 의류를 안입는 경우 -1을 빼고 반환
    }
}
