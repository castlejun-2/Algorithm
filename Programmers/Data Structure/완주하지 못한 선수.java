import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer> m = new HashMap<>();
        
        for (String pc : participant) {
            if (m.containsKey(pc)) m.put(pc,m.get(pc)+1);     //동명이인이 있다면 +1
            else m.put(pc,1);
        }
        
        for (String cp : completion) m.put(cp,m.get(cp)-1);   //완주했다면 -1
        
        for (String key : m.keySet()) {                       //이름이 남아있다면 완주하지 못한것이다.
            if (m.get(key)>0) answer=key;
        }
        return answer;
    }
}
