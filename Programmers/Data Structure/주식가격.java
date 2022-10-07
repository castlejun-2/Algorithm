import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> st = new Stack<>();
        
        for (int i=0;i<prices.length;i++) {
            while (!st.isEmpty() && prices[i]<prices[st.peek()]) {  //최근에 삽입된 값보다 작으면 pop, 자신보다 작거나 같은값 만날떄 까지 pop
                answer[st.peek()]=i-st.peek();
                st.pop();
            }
            st.push(i);
        }
        
        for (Integer idx :st) { //stack에 들어 있는 값은 끝날 때 까지 자신보다 작은값이 나오지 않은 것이다.
            answer[idx]=prices.length-idx-1;
        }
        
        return answer;
    }
}
