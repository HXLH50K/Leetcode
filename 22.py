class Solution:
    def DFS(self, l, r, re):
        if r>l or l>self.n or r>self.n:
            return
        if l==self.n and r==self.n:
            self.res.append(re)
            return
        self.DFS(l+1, r, re+"(")
        self.DFS(l, r+1, re+")")
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = []
        self.DFS(0,0,"")
        return self.res