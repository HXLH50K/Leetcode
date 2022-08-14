/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {string}
 */
var findLongestWord = function (s, dictionary) {
  dictionary.sort()
  dictionary.sort((a, b) => b.length - a.length)
  let res = ''
  for (let x of dictionary) {
    let i = 0,
      j = 0
    while (i < s.length && j < x.length) {
      if (s[i] == x[j]) {
        i++
        j++
      } else {
        i++
      }
    }

    if (j == x.length) {
      res = res.length < x.length ? x : res
    }
  }
  return res
}
let a = findLongestWord((s = 'abpcplea'), (dictionary = ['ale', 'apple', 'monkey', 'plea']))
console.log(a)
