package fac;

import (
	"fmt";
);

func fact(n int_t, m int_t, k int_t, l int_t) int_t {
	return n+m+k-l;
};

func main() {
	var k int_t = fact(1,5,3,4);
	print(k);
};