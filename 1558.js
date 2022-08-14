var minOperations = function (nums) {
  nums.sort(function (a, b) {
    return a - b
  })
  console.log(nums)
  var n = nums.length
  var cnt = 0
  while (nums[n - 1] > 0) {
    for (var i = 0; i < n; i++) {
      if (nums[i] % 2 != 0) {
        nums[i] -= 1
        cnt += 1
      }
      nums[i] /= 2
    }
    cnt += 1
    console.log(nums)
  }

  return Math.max(cnt - 1, 0)
}

console.log(minOperations([7, 4, 3, 2, 0, 2]))
