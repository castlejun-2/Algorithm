import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> s = new Stack<>();
        s.push(arr[0]);
        
        for (int i=1; i<arr.length; i++){
            if (s.peek()==arr[i]) continue;     //가장 최근에 삽입된 값과 같다면 무시
            else s.push(arr[i]);
        }
        
        return s.stream().mapToInt(i->i).toArray();   //Stack의 값을 int형 배열로 변환
    }
}
