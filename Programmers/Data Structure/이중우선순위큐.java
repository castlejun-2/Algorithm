import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> min_q = new PriorityQueue<>();
        PriorityQueue<Integer> max_q = new PriorityQueue<>(Collections.reverseOrder());
        
        for(String op : operations){
            String o[] = op.split(" ");
            if (o[0].equals("I")){            //값 입력
                max_q.add(Integer.parseInt(o[1]));
                min_q.add(Integer.parseInt(o[1]));
            } 
            else if (o[1].equals("-1"))       //최솟값 삭제
                max_q.remove(min_q.poll());
            else if (o[1].equals("1"))        //최대값 삭제
                min_q.remove(max_q.poll());
        }
        
        int[] answer = {0,0};
        
        if (max_q.size()!=0 && min_q.size()!=0){  //값이 존재한다면 입력
            answer[0]=max_q.peek();
            answer[1]=min_q.peek();
        }
        return answer;
    }
}
