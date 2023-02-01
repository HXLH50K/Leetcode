# %%
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_set = []
        for c in key:
            if c in key_set or c == " ":
                continue
            key_set.append(c)
            if len(key_set) == 26:
                break
        mmap = dict({" ": " "})
        for i in range(26):
            mmap.update({key_set[i]: chr(ord("a") + i)})
        return "".join(map(lambda x: mmap[x], [c for c in message]))
