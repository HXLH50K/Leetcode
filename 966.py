from collections import defaultdict
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        case_ignore_wordlist = defaultdict(list)
        vowel_ignore_wordlist = defaultdict(list)
        for word in wordlist:
            case_ignore_wordlist[word.lower()].append(word)
            vowel_ignore_wordlist[self._replace_vowels(word)].append(word)

        res = []
        for query in queries:
            if query in wordlist:
                res.append(query)
                continue
            if query.lower() in case_ignore_wordlist:
                res.append(case_ignore_wordlist[query.lower()][0])
                continue
            if self._replace_vowels(query) in vowel_ignore_wordlist:
                res.append(vowel_ignore_wordlist[self._replace_vowels(query)][0])
                continue
            res.append("")
        return res

    def _replace_vowels(self, word: str) -> str:
        vowels = "aeiou"
        return "".join(["*" if c in vowels else c for c in word.lower()])
