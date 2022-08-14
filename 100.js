function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
var flag = true
var preOrder = function(p, q){
    if (!flag) {
        return
    }
    if (p == null && q == null) {
        return 
    }
    if (p == null || q == null) {
        flag = false
        return 
    }
    if (p.val != q.val) {
        flag = false
        return 
    }
    preOrder(p.left, q.left)
    preOrder(p.right, q.right)
}
var isSameTree = function(p, q) {
    preOrder(p,q)
    return flag
};
