import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String nums[] = new String[numbers.length];
        String answer = "";
        
        for (int i=0; i<numbers.length; i++){
            nums[i]=Integer.toString(numbers[i]);
        }
        
        Arrays.sort(nums,(a,b)->(b+a).compareTo(a+b));    //lambda식을 활용해 6+10(610) vs 10+6(106)을 비교
        
        for (String num: nums)
            answer+=num;
        
        if (nums[0].equals("0"))        //"000"과 같은 case 예외처리
            answer="0";
        
        return answer;
    }
}
