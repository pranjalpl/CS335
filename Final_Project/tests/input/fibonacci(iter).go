package mai;
import "fmt";
func fib(n int_t) int_t {
	if(n==1){
		return 0;
	};
	if(n==2){
		return 1;
	};
	var prev,curr,next,i int_t;
	prev = 0;
	curr = 1;
	next = 1;
	for i=2; i<n; i++{
		next = prev + curr;
		prev = curr;
		curr = next;
	};
	return next;
};

func main(){
	var n int_t;
	scan(n);
	print(fib(n));
};
