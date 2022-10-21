import java.util.*;

class Solution {
    public int solution(int[] arr) {
        if (arr.length==1) return arr[0]; #arr의 길이가 1일 경우
        if (arr.length==2) return arr[0]*arr[1]/gcd(arr[0],arr[1]); #arr의 길이가 2일 경우
        
        Arrays.sort(arr);
        
        int answer=arr[0]*arr[1]/gcd(arr[0],arr[1]);  #answer의 초기값 설정
        
        for (int i=2; i<arr.length; i++) answer=(answer*arr[i])/gcd(answer,arr[i]); #최대공배수/최대공약수 = 최소공배수
        
        return answer;
    }
    private static int gcd(int a, int b) {  #최대공약수를 구하는 함수
        int r = a % b;
        if(r == 0) return b;
        else return gcd(b, r);
    }
}
