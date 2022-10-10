import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Map<Integer,Integer> m = new HashMap<>();
        
        for (int num: nums){
            if (m.containsKey(num)) {       //이미 있는 key라면 기존의 값에 +1
                m.put(num,m.get(num)+1);
            } else {
                m.put(num,1);               //그렇지 않다면 생성
            }
        }
        
        if (nums.length/2 <= m.size())      //절반보다 많은 종류라면 nums.length/2 출력
            return nums.length/2;
        
        return m.size();                    //그렇지 않다면 종류의 최대값 출력
    }
}
