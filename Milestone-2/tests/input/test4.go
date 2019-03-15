package math;
import "fmt";

type Vertex struct{
	i int_t;
	j int_t;
};

type Node struct{
	i int_t;
	j int_t;
};

func temp() int_t {
	return 0;
};
func main() {
	var a[33] int_t;
	a[3] = 3;
	var d,e type Vertex;
	var n,m type Vertex;
	var i int_t = 2;
	d.i = a[3];
	e.i = 1;
	n = d;
	print(d.i);
	print(e.i);
	print(i);
};
