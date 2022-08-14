/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function (k) {
  let fib = [1, 1],
    cnt = 0
  while (fib[0] < k) {
    fib.unshift(fib[0] + fib[1])
  }
  for (let x of fib) {
    if (k < x) {
      continue
    } else {
      k -= x
      cnt += 1
    }
    if (k == 0) {
      return cnt
    }
  }
}
console.log(findMinFibonacciNumbers(10))
