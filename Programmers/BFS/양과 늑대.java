import java.util.*;

class Solution {
    static int answer = 0;
    Map<Integer,List<Integer>> graph;
    
    public int solution(int[] info, int[][] edges) {
        graph = new HashMap<>();
        
        for (int[] edge : edges){
            if (!graph.containsKey(edge[0])) graph.put(edge[0],new ArrayList<Integer>());
            graph.get(edge[0]).add(edge[1]);
        }
        
        List<Integer> list = new ArrayList<>();
		list.add(0);
        
        dfs(0,0,0,list,info);
    
        return answer;
    }
    public void dfs(int node,int sheep, int wolf, List<Integer> list, int[] info) {
        sheep+=info[node]^1;
        wolf+=info[node];
        
        if (sheep<=wolf) return;    //늑대가 많으면 반환
        
        answer = Math.max(answer,sheep);
        
        List<Integer> next = new ArrayList<>(); //노드값 복사
        next.addAll(list);
        
        if (graph.containsKey(node)) next.addAll(graph.get(node));  //리프노드가 아니면 연결된 노드 추가
        next.remove(Integer.valueOf(node)); //remove(Ojbect) 이므로 객체형으로 mapping 하는 valueOf 사용
        
        for (Integer n : next)
            dfs(n,sheep,wolf,next,info);
        
    }
}
