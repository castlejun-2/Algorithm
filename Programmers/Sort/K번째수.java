import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int ansIdx = 0;
        
        for (int[] command: commands){
            int i=command[0],j=command[1],k=command[2];
            ArrayList<Integer> tmp = new ArrayList<>();
            
            for (int a=i;a<=j;a++){     //i번째부터 j번째까지 복사
                tmp.add(array[a-1]);
            }
            Collections.sort(tmp);      //복사한 배열 정렬
            answer[ansIdx++]=tmp.get(k-1);    //answer에 원하는 index 값 추가
        }
        
        return answer;
    }
}
