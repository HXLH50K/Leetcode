/**
 * @param {number[]} arr
 * @return {number}
 */
function sum(nums) {
  summ = 0
  nums.forEach(x => {
    summ += x
  })
  return summ
}
var sumOddLengthSubarrays = function (arr) {
  let summ = 0
  for (let window = 1; window <= arr.length; window += 2) {
    for (let i = 0; i + window <= arr.length; i++) {
      summ += sum(arr.slice(i, i + window))
    }
  }
  return summ
}
console.log(sumOddLengthSubarrays([1, 4, 2, 5, 3]))
