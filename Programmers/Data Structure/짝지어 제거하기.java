import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> st = new Stack<>();
        
        for (int i=0;i<s.length();i++){
            if (st.isEmpty()){         //비어있다면 그냥 삽입
                st.push(s.charAt(i));
            } else {
                if(st.peek()==s.charAt(i)){     //바로 이전의 삽입된 값이 같다면 pop
                    st.pop();
                } else{                         //그렇지 않다면 삽입
                    st.push(s.charAt(i));
                }
            }
        }
        
        if (st.isEmpty())   //스택이 비어있다면 1을 리턴
            return 1;
        
        return 0;           //그렇지 않다면 1을 리턴
    }
}
