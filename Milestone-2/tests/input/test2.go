package maie;

func f(a int_t) int_t
{
	if(a==1 || a==0){
		return 1;
	};
	return f(a-1) + f(a-2);
};

func main() {
	var a int_t=5;
	print(f(a));
	a=a+1;
};
