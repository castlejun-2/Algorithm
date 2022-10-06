import java.util.PriorityQueue;       //우선순위큐를 사용하기 위한 라이브러리

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<> ();   //int형 우선순위큐 생성
        
        for (int tmp : scoville) {                            //scoville의 원소를 삽입
            pq.add(tmp);
        }
        
        while (pq.peek() <= K) {                              //우선순위큐의 가장 작은 값이 K보다 크면 반복 종료
            if (pq.size() == 1)                               //크기가 1인데, K값을 넘지 못하였으므로 -1 출력
                return -1;
            int sm1 = pq.poll();
            int sm2 = pq.poll();
            
            pq.add(sm1+sm2*2);                                //섞은 음식의 스코빌 지수를 우선순위큐에 삽입
            answer += 1;                                      //횟수 +1 증가
        }
                
        return answer;
    }
}
