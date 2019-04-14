python3 src/codeGenerator.py --input=tests/input/$1
gcc -m32 -o out output.S
./out
