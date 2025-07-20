class Solution:
    def makeFancyString(self, s: str) -> str:

        import re

        return re.sub(r"(.)\1{2,}", r"\1\1", s)
