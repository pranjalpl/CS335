package mai;

import "fmt";

func binsearch(a *int_t, low int_t, high int_t, n int_t) int_t{
	if(low > high){
		return -1;
	};
	var middle int_t = low + (high - low)/2;
	if(*(a+4*middle) == n){
		return middle;
	};
	if(*(a+4*middle) > n){
		return binsearch(a,middle+1,high,n);
	}else{
		return binsearch(a,low,middle-1,n);
	};
};

func main() {
	var a[10] int_t;
	var d int_t;
	var c int_t = 10;
	var n int_t;
	for d = 0; d < c ;d++{
		scan(n);
		a[d] = n;
	};
	scan(n);
	print(binsearch(&a,0,9,n));
};
