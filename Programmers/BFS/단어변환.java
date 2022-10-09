import java.util.*;

class Solution {
    static boolean[] visited;
    static int answer = 0;
    
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        
        dfs(begin,target,words,0);
        
        return answer;
    }
    
    public void dfs(String begin, String target, String[] words, int cnt) {
        if (begin.equals(target)){
            if (answer==0)        //값이 0이면 cnt 값 삽입
                answer = cnt;
            else if (answer>cnt)  //최소값 비교
                answer = cnt;
            return;
        }
        
        for (int i=0; i<words.length; i++){
            if (visited[i])   //방문한 words라면 스킵
                continue;
                
            int same = 0;
            for (int k=0; k<words[i].length(); k++){      //길이가 하나 차이 나는 값을 넣는다.
                if (begin.charAt(k)==words[i].charAt(k))
                    same++;
            }
            
            if (same == begin.length()-1) {
                visited[i]=true;
                dfs(words[i],target,words,cnt+1);   //길이가 하나 다른 값부터 찾아 나간다.
                visited[i]=false;
            }
        }
    }
}
