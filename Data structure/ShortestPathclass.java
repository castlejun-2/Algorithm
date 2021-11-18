import java.util.Stack;

public class ShortestPathClass {
	
	private final int INFINITY = 9999 ;

	private	int length[][] ;  // 간선의 길이
  private int aSize ;       // 배열의 크기 - 정점들의 수 - 여기서는 사용하지 않음
  private int dist[] ;     // 배열 dist - 최대 경로의 길이
  private boolean s[] ;    // 배열 s - 정점의 선택 여부
  private int p[] ;        // 최단경로를 얻기 위한 배열
    
  public ShortestPathClass(int n) {  //생성자 함수, 정점의 수를 매개변수로 받음
  	length = new int [n][n]; 
   	dist   = new int [n];
   	s = new boolean [n];
   	p = new int [n] ;
   	aSize = n;
   	for (int i=0; i<n ; i++) {    // length 배열의 초기화
   		for (int j=0; j<n; j++) 
   			length[i][j] = INFINITY;
   	}
   }
   
   void addEdge(int s, int t, int w) {
   	length[s][t] = w ;
   }
   
void ShortestPath(int n, int v)
// dist[j],0 <= j<= n은 n개의 정점을 가진 방향 그래프 G에서 정점  v로부터  정점 j 까지 
// 의 최단 경로 길이로 설정됨. 간선의 길이는 length[j][j]로 주어짐.
{
  for (int i=0; i<n; i++) {
	   s[i] = false; 
	   dist[i] = length[v][i]; // 초기화
	   p[i] = v ;              // 시작정점으로 초기화
  }
  s[v] = true;
  dist[v] = 0;
  for (int i=0; i<n-2; i++) { // 정점 v로부터 n-1개 경로를 결정
   
  int u = 0;     // 초기값 0 은 의미 없음 (컴파일 에러 회피용
  int val = INFINITY ;
  for (int j=0; j<n; j++) {    // choose는 dist[u] = minimum dist[w]인 u를 반환
	  if (!s[j])
			 if (dist[j] < val) {
			    val = dist[j];
			    u = j ;
		   }
	  }
	  s[u] = true;
    for (int w=0; w<n; w++)
      if(!s[w])
         if(dist[u] + length[u][w] < dist[w]) {
               dist[w] = dist[u] + length[u][w];
               p[w] = u ;    // 최단 거리의 정점으로 업데이트
         }
      }// for(i=0; ...)의 끝
      Stack<Integer> stack = new Stack<Integer>();  // 자바의 시스템 스택 클래스의 객체를 생성
      
      System.out.println("시작 정점 " + v + " 에서 각 정점까지의 최단 비용 및 경로: ");   	
    	for (int i=0; i<n; i++){
      	System.out.print("정정 "+ i +" 의 최단비용: "+ dist[i] + " 최단 경로 : ");
    		if(dist[i] < INFINITY) {   // 경로가 있는 경우
    		   stack.push(i) ;
    		   int j = p[i];
    		   while(j != v) {         // 시작 정점이 나올 때까지 배열 p[] 를 역추적하며 스택에 저장
    			   stack.push(j) ;
    			   j = p[j];
  		     }
    		   System.out.print(v) ;
    		   while (!stack.isEmpty())    // 스택에 저장된 중간 정점들을 차례로 출력
    			   System.out.print(" -> " + stack.pop()) ;
    		}
    		else
    			System.out.print("경로 없음");
    		System.out.println();	    	   		
	   	} // end of for    
	} 
}
