###############################################################################
A GOlang Compiler written in Python (for x86) 
Authors: Akash Kumar Dutta, Prakhar Agarwal, Swarnadeep Mandal 
Group 11
###############################################################################

# Language Features:
    a.  Data Types - int, bool, rune and multi dimensional arrays of int, bool and rune
    b.  Operators
            int:
                - Unary -> !,-,~,+
                - Relational ->  <, >, ==, !=
                - Arithmetic -> +,-,/,%
                - Bitwise -> <<,>>,&,|,^
                - Logical ops -> &&,||
                - Assignment -> = 
            bool (realized as int 0 and 1):
                - Unary-> !
                - Logical -> &&,||
                - Assignment -> =
            Arrays:
            	- Same as int

    c.  Loops -> for, while
    d.  Selection Statements -> if, if-else
    e.  Multiple Declarations and Sequential Assignments
        - Multiple Declarations  -> int a,b,c=3;
        - Sequential Assignments -> a=b=c=3;
    f.  Arrays -> 1-D arrays of types - {int,char,bool}
    g.  Classes
    	- Only one class allowed in the program
        - Data members can only be of simple or array of simple types.
    h.  Functions
        - Allowed return types -> int
        - Allowed argument types -> int, char, bool
    i.  Scoping
    	- Imlemented as a tree of symbol tables
    j.  boolean expressions realized as integer 0 and 1 with relational operators
    k.	pre increment/decrement
    l.	RECURSION
    m.  struct
    n.  type checking

# Features not supported:
    b. float and double type


###############################################################################


USAGE:
> make
> ./GOtham test

To Clean:
> make clean
