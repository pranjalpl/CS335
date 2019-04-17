package mai;

import "fmt";

var g int_t;
var h int_t;
var k int_t;


func main() {
	var i [9] int_t;
	var d int_t;
	var c int_t = 9;
	var e int_t;
	var t int_t;

	for d = 0; d < c ;d++{
		scan(e);
		i[d] = e;
	};
	
	for d = 0; d < c-1; d++{
		for e = 0; e < c-1; e++{
			if(i[e] > i[e+1]){
				t = i[e];
				i[e] = i[e+1];
				i[e+1] = t;
			};
		};
	};

	for d = 0; d < c ;d++{	
		print(i[d]);
	};
};
