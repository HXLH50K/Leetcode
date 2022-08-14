var numberOfArithmeticSlices = function (nums) {
  var res = 0,
    add = 0
  for (var i = 2; i < nums.length; i++) {
    if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
      add++
      res += add
    } else {
      add = 0
    }
  }
  return res
}
console.log(numberOfArithmeticSlices([1, 2, 3, 4]))
