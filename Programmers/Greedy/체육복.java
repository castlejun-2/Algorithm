import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i:lost) {
            map.put(i,0);
        }

        Arrays.sort(reserve);       //오름 차순으로 정렬

        for (int num : reserve) {
            if (map.containsKey(num)) map.put(num,1);   //내 체육복을 잃어버렸다면, 나에게 체육복 대여
            else if (map.containsKey(num-1) && map.get(num-1)==0) {     //앞사람에게 우선적으로 대여   
                map.put(num-1,1);
            } else if (map.containsKey(num+1) && map.get(num+1)==0) {   //앞사람이 이미 있거나, 없다면 뒷사람이 대여
                map.put(num+1,1);
            }
        }

        int get = 0;
        for (int i : map.keySet())    
            if (map.get(i)==1) get++;

        return n-map.size()+get;        //전체인원에서, 대여에 성공한 인원의 수는 제거
    }
}
