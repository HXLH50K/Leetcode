# %%
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.codes = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.codes:
            self.codes[tokenId] = currentTime + self.timeToLive
        else:
            self.codes.update({tokenId: currentTime + self.timeToLive})

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.codes and self.codes[tokenId] > currentTime:
            self.codes[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        remove_tokens = []
        for tokenId in self.codes:
            expire_time = self.codes[tokenId]
            if expire_time <= currentTime:
                remove_tokens.append(tokenId)
            else:
                cnt += 1
        for x in remove_tokens:
            del self.codes[x]
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
timeToLive = 5
obj = AuthenticationManager(timeToLive)
obj.renew("aaa", 1)
obj.generate("aaa", 2)
a = obj.countUnexpiredTokens(6)
obj.generate("bbb", 7)
obj.renew("aaa", 8)
obj.renew("bbb", 10)
b = obj.countUnexpiredTokens(15)

# %%
