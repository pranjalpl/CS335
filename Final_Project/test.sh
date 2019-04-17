rm out || true
rm output.S || true
echo -e "\e[33mStarting the compiler\e[39m"
python3 src/codeGenerator.py --input=tests/input/$1
if [[ $? -ne 0 ]]; then echo -e "\e[31mCompiling failed. Exiting...\e[39m"; exit $?; fi
echo -e "\e[32mCompilation completed. Creating executable...\e[39m"
gcc -m32 -o out output.S
if [[ $? -ne 0 ]]; then echo -e "\e[31mCreating executable failed. Exiting...\e[39m"; exit $?; fi
echo -e "\e[32mExecutable built. Running the program...\e[39m"
./out
