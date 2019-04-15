package maie;

import "fmt";

func ack(n, m int_t) int_t {
	var temp1, temp2 int_t;
	if(m==0){
		return n+1;
	};
	if(m>0){
		if(n==0){
			temp1 = ack(m-1,1);
			return temp1;
		};
	};
	if(m>0){
		if(n>0){
			temp1 = ack(m,n-1);
			temp2 = ack(m-1,temp1);
			return temp2;
		};
	};
};

func main() {
	var a int_t = 1;
	var b int_t = 1;
	print(ack(a,b));
	return 0;
};


