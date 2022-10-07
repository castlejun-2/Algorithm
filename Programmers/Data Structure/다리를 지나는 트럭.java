import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int tmp = 0;
        Queue<Integer> q = new LinkedList<Integer>();

        for (Integer tq : truck_weights) {
            while (true) {
                if (q.size()==bridge_length){  //다리위가 꽉 차면, 가장 앞의 트럭이 나간다.
                    tmp -= q.poll();
                } else {
                    if (tmp + tq <= weight) { //트럭이 올라갈 수 있으면 다리에 올라간다.
                        q.add(tq);
                        tmp += tq;
                        answer++;
                        break;
                    } else {
                        q.add(0);     //값이 꽉 차면, 가장 앞 트럭이 지나갈때까지 기다린다.
                        answer++;
                    }
                }
            }
        }
        return answer+bridge_length;
    }
}
