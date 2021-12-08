public class GreedyKnapsackClass {
    private Obj obj[] ;
    private float x[] ;
    private int ObjSize ;
	
    public GreedyKnapsackClass(Obj ob[], int n) {  
    	obj = ob; 
    	ObjSize = n ;
    	x = new float [n+1] ;
        // pi/wi 의 내림차순으로 정렬	
        for (int i=2; i<=n; i++) {   // 삽입정렬 사용
        	Obj b = obj[i] ;
        	int j;
        	for (j=i-1; j >=1 && b.pow > obj[j].pow; j--)
        		obj[j+1] = obj[j] ;
        	obj[j+1] = b ;
        }  	
    }
    public void printResult() {
    	
    	int tp = 0 ;
   		System.out.println("이익 무게 x[i] ");
    	for (int i=1; i<=ObjSize; i++){
    		System.out.print(i+": "+obj[i].profit+"   "+obj[i].weight+ "    "+ x[i]);
    		tp += obj[i].profit * x[i] ;   // 총 이익을 위한 누적계산
    		System.out.println();
    	}
    	System.out.println("총 이익  = "+tp) ;
    }
    public void GreedyKnapsack(float m, int n) {
    // p[1:n] and w[1:n] contain the profits and weights
    // respectively of the n objects ordered such that
    // p[i]/w[i] >= p[i+1]/w[i+1]. m is the knapsack
    // size and x[1:n] is the solution vector.
	for (int i=1; i<=n; i++) x[i]= 0; // Initialize x.
	    float U = m;
	    int i ;
	    for (i=1; i<=n; i++) {
	        if (obj[i].weight > U) break;
	            x[i] = 1;
	            U -= obj[i].weight ;
	    }
	    if (i <= n) x[i] = U / obj[i].weight;
    }
}
