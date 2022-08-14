/**
 * @param {number[]} w
 */
var Solution = function (w) {
  this.weights = w
  this.nums = []
  for (let i = 0; i < this.weights.length; i++) {
    this.nums.push(...new Array(this.weights[i]).fill(i))
  }
}

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function () {
  return this.weights[Math.floor(Math.random() * this.weights.length)]
}

/**
 * Your Solution object will be instantiated and called as such:
 *
 * var param_1 = obj.pickIndex()
 */
w = [1, 2, 3]
var obj = new Solution(w)
console.log(obj.pickIndex())
