import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown+yellow;
        ArrayList<Integer> num = new ArrayList<>();
        int answer[] = new int[2];
        
        for (int i=1; i<=area; i++) {       //약수 생성
            if (area%i==0)
                num.add(i);
        }
        Integer[][] set = new Integer[(int)Math.ceil((double)num.size()/2)][2]; //약수의 조합으로 가능한 넓이 생성
        
        for (int i=0; i<(int)Math.ceil((double)num.size()/2); i++) {  
            set[i][0]=num.get(i);
            set[i][1]=num.get(num.size()-i-1);
        }

        for(Integer[] s : set) {  //각각 -2를 해서 곱한 값이 yellow 영역
            if ((s[0]-2)*(s[1]-2)==yellow){
                answer[0]=s[1];
                answer[1]=s[0];
            }
        }
        return answer;
    }
}
