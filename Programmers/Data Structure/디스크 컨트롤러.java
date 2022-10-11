import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int solved = 0;
        int jobIdx = 0;
        int time = 0;
        int answer = 0;
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt((int[] o) -> o[1]));
        Arrays.sort(jobs,Comparator.comparingInt((int[] o) -> o[0]));
            
        while (solved < jobs.length) {
            while(jobIdx < jobs.length && jobs[jobIdx][0]<=time){   //새로 들어온 요청 추가
                q.add(jobs[jobIdx++]);
            }

            if (q.isEmpty()){           //현재 진행 가능한 작업이 없다면 현재 시간 변경
                time = jobs[jobIdx][0];
            } else {
                int task[] = q.poll();  //가장 수행시간이 짧은 작업 수행
                answer += time+task[1]-task[0];
                time += task[1];
                solved ++;
            }
        }
        
        return answer/jobs.length;
    }
}
