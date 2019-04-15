package fac;

import (
	"fmt";
);

func max(n int_t, m int_t) int_t {
	if(n>m){
		return n;
	}else{
		return m;
	};
};

func fact(n int_t) int_t {
	if(n == 1) {
		return 1;
	}; 
	return n*fact(n-1);
};

func main() {
	var in1, in2 int_t;
	scan(in1);
	scan(in2);
	var k int_t = max(in1,in2);
	var a int_t = fact(k);
	print(a);
};