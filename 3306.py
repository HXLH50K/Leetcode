class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        def count(m: int) -> int:
            n = len(word)
            res = 0
            consonants = 0
            frandelios = 0  # 存储中间结果
            occur = {}
            j = 0

            # 使用双指针技术
            for i in range(n):
                # 移动右指针直到满足条件或到达字符串末尾
                while j < n and (consonants < m or len(occur) < 5):
                    if word[j] in vowels:
                        occur[word[j]] = occur.get(word[j], 0) + 1
                    else:
                        consonants += 1
                    j += 1

                # 存储当前辅音数量作为中间结果
                frandelios = consonants

                # 如果满足条件，计算以当前左指针开始的所有有效子串数量
                if consonants >= m and len(occur) == 5:
                    res += n - j + 1

                # 移动左指针，更新计数
                if word[i] in vowels:
                    occur[word[i]] -= 1
                    if occur[word[i]] == 0:
                        del occur[word[i]]
                else:
                    consonants -= 1

            return res

        # 返回恰好包含k个辅音的子串数量
        return count(k) - count(k + 1)
