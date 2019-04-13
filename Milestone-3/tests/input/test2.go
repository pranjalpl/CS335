//  FIBOOO
// Look for recursion obv

package maie;

func f(a int_t) int_t
{
	if(a==1 || a==0){
		return 1;
	};
	if(a==1 || a==0){
		return 1;
	};
	return f(a-1) + f(a-2);
};

func main() {
	var a  int_t=5;
	var b [10]  int_t;
	print(f(a));
	a=a+1;
};
