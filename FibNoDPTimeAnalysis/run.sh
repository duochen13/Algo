# complie
g++ -std=c++11 fib.cpp -o fib.exe
javac Fib.java

# execute
for N in 27 29 31 33 34 36
do
	echo "===> N = $N:"
	./fib.exe $N
	go run fib.go $N
	java Fib $N
	node fib.js $N
	python3 fib.py $N
done
