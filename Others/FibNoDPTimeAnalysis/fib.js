const {performance} = require('perf_hooks');
const process = require('process');

var args = process.argv
N = parseInt(args[2])

function fib(n) {
	if (n == 0 || n == 1) {
		return 1
	}
	return fib(n - 1) + fib(n - 2)
}

let start = performance.now()
fib(N)
let end = performance.now()

console.log("js ", end - start) //ms

