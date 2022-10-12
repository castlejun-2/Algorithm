import java.util.*;

class Solution {
    HashSet<Integer> answer = new HashSet<>();
    static boolean visited[];
    static String numArr[];
    
    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        numArr = numbers.split("");
        
        recursion("",0);
        
        return answer.size();
    }
    public void recursion(String tmp,int idx) {       //재귀를 통해 가능한 소수 탐색
        if (tmp!=""){
            if (isPrime(tmp))
                answer.add(Integer.parseInt(tmp));
        }
        if (idx==numArr.length) return;               //무한 재귀 호출 예방
            
        for (int i=0; i<numArr.length; i++) {
            if (!visited[i]) {
                visited[i]=true;
                recursion(tmp+numArr[i],idx+1);
                visited[i]=false;
            }
        }
    }
    
    public boolean isPrime(String n) {      //소수 판별
        int num = Integer.parseInt(n);
        if (num<2) return false;
        
        for (int i=2;i<=Math.pow(num,0.5);i++) {
            if (num%i==0) return false;
        }
        return true;
    }
}
