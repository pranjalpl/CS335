package mai;

import "fmt";

func fib(n int_t) int_t {
	if(n<3){
		return n;
	};
	return fib(n-1) + fib(n-2)+fib(n-3);
};

func main() {
	var i,j int_t;
	scan(i);
	print(fib(i));
};
