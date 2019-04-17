package mai;

import "fmt";

func main() {
	var i [10] int_t;
	var d int_t;
	var c int_t = 10;
	var l int_t = 0;
	var r int_t = 10;
	var m int_t;
	var n int_t;
	var idx int_t = -1;
	for d = 0; d < c ;d++{
		scan(n);
		i[d] = n;
	};
	scan(n);
	for ;l <= r;{
		m = l + (r-l)/2;
		if(i[m] == n){
			idx = m;
		};
		if(i[m] < n){
			l = m + 1;
		}else{
			r = m - 1;
		};
	};
	print(idx);
};
