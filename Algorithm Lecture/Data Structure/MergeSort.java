```java
public static class MergeSortClass {

		private int a[], b[];
		private int aSize;

	public MergeSortClass(int arr[], int n) { // 생성자 함수, 정렬할 데이터를 배열 a 에 받음
		a = arr;                  
		aSize = n;
		b = new int[aSize + 1];                 //pivot값 설정시 마지막 index를 벗어나는 오류를 막기 위해 가장 b[aSize+1]
	}
  
	public int[] MergeSortCall() {            // MergeSort 호출함수
		MergeSort(1, aSize);
		return a;
	}
  
	public void MergeSort(int low, int high) {  //MergeSort 함수
		if (low < high) {           
			int mid = (low + high) / 2;             //mid 값 설정
			MergeSort(low, mid);                    //low부터 mid까지 순환호출
			MergeSort(mid + 1, high);               //mid+1부터 high까지 순환호출
			Merge(low, mid, high);                  //합병(정복) 부분
		}	
  }
  
	public void Merge(int low, int mid, int high) { //합병(정복) 부분
		int h = low, i = low, j = mid + 1, k;         //h는 low부터 출발, j는 mid+1부터 출발
		while ((h <= mid) && (j <= high)) {           //h가 mid까지 도달하거나, j가 high까지 도달할때까지 반복
			if (a[h] <= a[j]) {                         //a[h]가 a[j]보다 작으면 새로운 배열 b에 작은값 부터 합병
				b[i] = a[h];
				h++;                                      //작은 값의 index 증가
			}
      else {
				b[i] = a[j];                              //위의 조건을 만족하지 않다면 a[mid+1]이 처음 실행될
				j++;                                      //작은 값이 j였으므로 j값 index 증가
		  }
			i++;                                        //b배열의 index 1증가 
	  }
		if (h > mid) {                                //반복문을 빠져나왔을 때 low부터 시작한 h가 mid값을 넘어갔다면
			for (k = j; k <= high; k++) {               //남은 뒤의 값들(mid보다 뒤의 index) 값들을 배열에 채워줌
				b[i] = a[k];
				i++;                                      //b배열의 index 1증가 
			}
		}
    else {                                        //남은 앞의 값들(mid보다 앞의 index) 값들을 배열에 채워줌
			for (k = h; k <= mid; k++) {
				b[i] = a[k];
				i++;                                      //b배열의 index 1증가 
			}
		}
		for (k = low; k <= high; k++)                 //b배열을 이제 a배열에 전부 복사
			a[k] = b[k];
	}
}
