/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
// var corpFlightBookings = function (bookings, n) {
//   res = new Array(n).fill(0)
//   let l, r, s
//   for (let x of bookings) {
//     ;[l, r, s] = x
//     for (let i = l - 1; i < r; i++) {
//       res[i] += s
//     }
//   }
//   return res
// }
var corpFlightBookings = function (bookings, n) {
  let suf_diff = new Array(n).fill(0),
    l,
    r,
    s
  res = new Array(n).fill(0)
  for (let x of bookings) {
    ;[l, r, s] = x
    suf_diff[l - 1] += s
    suf_diff[r] -= s
  }
  res[0] = suf_diff[0]
  for (let i = 1; i < n; i++) {
    res[i] = res[i - 1] + suf_diff[i]
  }
  return res
}
let bookings = [
    [1, 2, 10],
    [2, 2, 15]
  ],
  n = 2
console.log(corpFlightBookings(bookings, n))
