public static class QuickSortClass {           //QuickSort Class

	private int a[];
	private int aSize;

	public QuickSortClass1(int arr[], int n) {   //QuickSort Class 생성자
		a = arr;
		aSize = n;
		a[n + 1] = Integer.MAX_VALUE;              //배열의 마지막+1 index에 Integer 최댓값 입력
	}

	public int[] QuickSortCall() {               //인덱스 1부터 a[]의 크기까지를 정렬하는 QuickSort 호출 함수
		QuickSort(1, aSize);
		return a;
	}

	void QuickSort(int p, int q) {               //QuickSort 함수
		if (p < q) {
			int j = Partition(a, p, q + 1);          //j를 기준 앞에는 j보다 작읍값, 뒤에는 j보다 큰값으로 분류
			QuickSort(p, j - 1);                     //j를 기준 p부터 j-1까지 정렬
			QuickSort(j + 1, q);                     //j를 기준 j+1부터 q까지 정렬
		}
	}

	int Partition(int a[], int m, int p) {       //a[]배열을 m부터 p까지 하여 j값 추출
		int v = a[m];                              //m의 index값을 v에 저장
		int i = m, j = p;                         
		do {
			do
				i++;                                   //a[m]보다 큰값을 찾을 때 까지 i를 m에서부터 증가
			while (a[i] < v);
			do
				j--;                                   //a[m]보다 작은값을 찾을 때 까지 j를 p에서부터 감소
			while (a[j] > v);
			if (i < j)
				swap(a, i, j);                         //i의 index가 j의 index보다 작으면 swap
		} while (i < j);                           //i가 j보다 크다면 반복문을 벗어남
    
    swap(a,m,j);                               //j의 index를 갖는 값과 기존 pivot값 swap
		return j;                                  //j의 index return
	}

	void swap(int a[], int i, int j) {           //a[]배열의 i와 j인덱스를 갖는 값을 swap
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
}
