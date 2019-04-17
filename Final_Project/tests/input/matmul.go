package maie;

import "fmt";

func main(){
	var n1,m1,n2,m2,i,j,t,k int_t;
	var a[100][100] int_t;
	var b[100][100] int_t;
	var result[100][100] int_t;
	scan(n1);
	scan(m1);
	for i=0; i<n1; i++{
		for j=0; j<m1; j++{
			scan(t);
			a[i][j] = t;
		};
	};
	scan(n2);
	scan(m2);
	if(n2 != m1){
		print(0);
		return 0;
	};
	for i=0; i<n2; i++{
		for j=0; j<m2; j++{
			scan(t);
			b[i][j] = t;
		};
	};
	var sum int_t = 0;
	for i=0; i<n1; i++{
		for j=0; j<m2; j++{
			for k=0; k<m1; k++{
				sum = sum + a[i][k]*b[k][j];
			};
			result[i][j] = sum;
			sum = 0;
		};
	};
	for i=0; i<n1; i++{
		for j=0; j<m2; j++{
			print(result[i][j]);
		};
	};
	return 0;
};