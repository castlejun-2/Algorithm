import java.util.*;

class Solution {
    public ArrayList solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<>();
        int s1=0,s2=0,s3=0;
        int[] p1={1,2,3,4,5},p2={2,1,2,3,2,4,2,5},p3={3,3,1,1,2,2,4,4,5,5};
        
        for (int i=0;i<answers.length;i++) {
            if (answers[i]==p1[i%p1.length]) s1++;
            if (answers[i]==p2[i%p2.length]) s2++;
            if (answers[i]==p3[i%p3.length]) s3++;
        }
        
        int score = Math.max(s1,Math.max(s2,s3));
        
        if (score==s1) answer.add(1);
        if (score==s2) answer.add(2);
        if (score==s3) answer.add(3);
        
        return answer;
    }
}
