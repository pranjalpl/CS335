package maie;

import "fmt";

func ack(m, n int_t) int_t {
	if(m==0){
		return n+1;
	};
	if((m>0) && (n==0)){
		return ack(m-1,1);
	};
	if((m>0) && (n>0)){
		return ack(m-1,ack(m,n-1));
	};
};

func main() {
	var a int_t;
	var b int_t;
	scan(a);
	scan(b);
	print(ack(a,b));
	return 0;
};


