/**
 * @param {number[][]} points
 * @return {number}
 */
var distance = function (pointA, pointB) {
  return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2
}
var numberOfBoomerangs = function (points) {
  cnt = 0
  for (let i = 0; i < points.length; i++) {
    let dic_i = {},
      tmp = 0
    for (let j = 0; j < points.length; j++) {
      if (i == j) {
        continue
      }
      let dis = distance(points[i], points[j])
      dic_i[dis] ? ((tmp += dic_i[dis].length * 2), dic_i[dis].push(points[j])) : (dic_i[dis] = [points[j]])
    }
    cnt += tmp
  }
  return cnt
}

console.log(
  numberOfBoomerangs([
    [1, 1],
    [2, 2],
    [3, 3]
  ])
)
