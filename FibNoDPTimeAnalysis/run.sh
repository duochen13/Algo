# complie
g++ -std=c++11 fib.cpp -o fib.exe
javac Fib.java

# execute
for N in 27 28 29 30 31 32
do
	echo "=> N = $N"
	./fib.exe $N
	go run fib.go $N
	java Fib $N
	node fib.js $N
	python3 fib.py $N
done
