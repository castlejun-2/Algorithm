import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String,Integer> map = new HashMap<>();
        
        for (String phone : phone_book) {
            map.put(phone,0);
        }
        
        for (int i=0;i<phone_book.length;i++){
            for (int j=1;j<phone_book[i].length();j++){
                if (map.containsKey(phone_book[i].substring(0,j))){     //접두어가 Hash에 존재하는지 확인
                    return false;
                }
            }
        }
        
        return true;
    }
}
