package mai;

import "fmt";

func fib(n1 int_t , n2 int_t ,n3 int_t,n4 int_t,n5 int_t , n6 int_t ,n7 int_t,n8 int_t) int_t {
	return n1+n2+n3+n4+n5+n6+n7+n8;
};

func main() {
	var i1,i2,i3,i4,i5,i6,i7,i8 int_t;
	scan(i1);
	scan(i2);
	scan(i3);
	scan(i4);
	scan(i5);
	scan(i6);
	scan(i7);
	scan(i8);
	print(fib(i1,i2,i3,i4,i5,i6,i7,i8));
};
