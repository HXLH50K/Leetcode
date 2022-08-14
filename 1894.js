/**
 * @param {number[]} chalk
 * @param {number} k
 * @return {number}
 */
var chalkReplacer = function (chalk, k) {
  let pre_sum = [chalk[0]]
  for (let i = 1; i < chalk.length; i++) {
    pre_sum.push(chalk[i] + pre_sum[i - 1])
  }
  k = k % pre_sum[pre_sum.length - 1]
  let low = 0,
    high = chalk.length - 1
  while (low < high) {
    let mid = Math.floor((low + high) / 2)
    if (pre_sum[mid] <= k) {
      low = mid + 1
    } else {
      high = mid
    }
  }
  return low
}

console.log(chalkReplacer([22, 25, 39, 3, 45, 45, 12, 17, 32, 9], 835))
