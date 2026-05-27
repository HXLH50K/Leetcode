class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low_alpha_last_index  = [-1] * 26
        up_alpha_first_index   = [-1] * 26
        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                low_alpha_last_index[ord(ch) - ord('a')] = i
            elif 'A' <= ch <= 'Z':
                if up_alpha_first_index[ord(ch) - ord('A')] == -1:
                    up_alpha_first_index[ord(ch) - ord('A')] = i
        count = 0
        for i in range(26):
            if low_alpha_last_index[i] != -1 and up_alpha_first_index[i] != -1 and low_alpha_last_index[i] < up_alpha_first_index[i]:
                count += 1
        return count