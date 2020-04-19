const {performance} = require('perf_hooks');

function fib(n) {
	if (n == 0 || n == 1) {
		return 1
	}
	return fib(n - 1) + fib(n - 2)
}

let start = performance.now()
fib(40)
let end = performance.now()

console.log(end - start) //ms

