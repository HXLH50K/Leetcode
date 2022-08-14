/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function (version1, version2) {
  let v1 = version1.split('.'),
    v2 = version2.split('.'),
    x,
    y
  n = Math.max(v1.length, v2.length)
  for (let i = 0; i < n; i++) {
    x = i >= v1.length ? 0 : parseInt(v1[i])
    y = i >= v2.length ? 0 : parseInt(v2[i])
    if (x > y) {
      return 1
    } else if (x < y) {
      return -1
    }
  }
  return 0
}

console.log(compareVersion((version1 = '7.5.2.4'), (version2 = '7.5.3')))
