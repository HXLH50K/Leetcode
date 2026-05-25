class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[0] != '0' or s[n - 1] != '0':
            return False
        
        queue = [0]
        while queue:
            idx = queue.pop(0)
            if idx == n - 1:
                return True
            
            for i in range(idx + minJump, min(idx + maxJump + 1, n)):
                if s[i] == '0':
                    queue.append(i)
                    s = s[:i] + '1' + s[i + 1:]
        return False
            
            
