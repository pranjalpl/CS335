make
python ./bin/parser.py ./test/newtest/$1.go > /dev/null
python ./bin/codegen.py $1.ir
gcc -m32 -o output output.S
./output
