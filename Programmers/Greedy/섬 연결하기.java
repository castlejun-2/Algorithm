import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        int parent[] = new int[n];
        int answer = 0;
        
        for (int i=0; i<n; i++) //자기 자신이 부모인 집합 생성
            parent[i]=i;
        
        Arrays.sort(costs,(int o1[],int o2[])->o1[2]-o2[2]);    //가중치를 기준으로 오름차순 정렬
        
        for (int i=0; i<costs.length; i++) {    //크루스칼 알고리즘(최소비용 신장트리를 찾기 위한)을 활용
            if (findParent(parent,costs[i][0]) != findParent(parent,costs[i][1])) { //두 집합의 부모 비교
                answer+=costs[i][2];
                union(parent,costs[i][0],costs[i][1]);  //두 집합을 합친다.
            }
        }
        
        return answer;
    }
    public int findParent(int[] parent, int node) {
        if (parent[node]==node)
            return node;
        return findParent(parent, parent[node]);
    }
    
    public void union(int[] parent, int n1, int n2) {   //작은 부모의 값을 기준으로 집합을 합친다.
        int p_n1 = findParent(parent,n1);
        int p_n2 = findParent(parent,n2);
        
        if (p_n1 < p_n2) parent[p_n2]=p_n1;
        else parent[p_n1]=p_n2;
    }
}
