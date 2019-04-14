package math;

import "fmt";

func even(n int_t) int_t;

func odd(n int_t) int_t {
	if(n==0){
		return 0;
	}else{
		return even(n-1);
	};
};

func even(n int_t) int_t {
	if(n==0){
		return 1;
	}else{
		return odd(n-1);
	};
};

func main() {
	var n int_t;
	scan(n);
	print(even(n));
	print(odd(n));
};
