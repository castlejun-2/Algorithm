import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());    //큰 순서부터 값을 갖는 우선순위 큐 생성
        int answer = 0;

        for (int i=0;i<priorities.length;i++){
            pq.add(priorities[i]);
        }

        while (!pq.isEmpty()) {   //pg가 비게 된다면 종료
            for (int i=0;i<priorities.length;i++){    
                if (priorities[i]==pq.peek()){        //i가 가장 큰 값을 갖게되고
                    if (i==location){                 //i가 원하는 target 값이 맞다면 반복 종료
                        return answer+1;
                    }
                    pq.poll();                        //그렇지 않다면 가장 큰 값을 제거 하고 프린터 순서를 +1 증가
                    answer++;
                }
            }
        }
        return -1;
    }
}
