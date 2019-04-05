package mai;
import "fmt";

// Linked list and stuff like that
// If this works, tree shuld also work
type Node struct{
	value int_t;
	next *(type Node);
};

func main() {
	var head type Node;
	var next type Node;
	head.value = 10;
	head.next = &next;
	head.next.next = (&head) + 1;
	return;
};
