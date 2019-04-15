package maie;

import "fmt";

func partition(a *int_t, low int_t, high int_t) int_t{
	var pivot int_t = *(a+4*high);
	var i int_t = low - 1;
	var j,t int_t;
	for j=low; j<high; j++{
		if(*(a+4*j) <= pivot){
			i++;
			t = *(a+4*i);
			*(a+4*i) = *(a+4*j);
			*(a+4*j) = t;
		};
	};
	t = *(a+4*(i+1));
	*(a+4*(i+1)) = *(a+4*high);
	*(a+4*high) = t;
	return i+1;
};

func qsort(a *int_t, low int_t, high int_t) int_t {
	if(low<high){
		var pi int_t = partition(a,low, high);
		qsort(a, low, pi-1);
		qsort(a, pi+1, high);
	};
	return 1;
};

func main(){
	var a[10] int_t;
	var i,e int_t;
	for i=0; i<10; i++{
		scan(e);
		a[i] = e;
	};
	qsort(&a,0,9);
	for i=0; i<10; i++{
		print(a[i]);
	};
};