/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function (a, b) {
  while (b != 0) {
    ;[a, b] = [a ^ b, (a & b) << 1]
  }
  return a
}
console.log(getSum(2, 3))
