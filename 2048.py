# %%
from typing import List
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        BeautifulNumbers = [
            1,
            22,
            122,
            212,
            221,
            333,
            1333,
            3133,
            3313,
            3331,
            4444,
            14444,
            22333,
            23233,
            23323,
            23332,
            32233,
            32323,
            32332,
            33223,
            33232,
            33322,
            41444,
            44144,
            44414,
            44441,
            55555,
            122333,
            123233,
            123323,
            123332,
            132233,
            132323,
            132332,
            133223,
            133232,
            133322,
            155555,
            212333,
            213233,
            213323,
            213332,
            221333,
            223133,
            223313,
            223331,
            224444,
            231233,
            231323,
            231332,
            232133,
            232313,
            232331,
            233123,
            233132,
            233213,
            233231,
            233312,
            233321,
            242444,
            244244,
            244424,
            244442,
            312233,
            312323,
            312332,
            313223,
            313232,
            313322,
            321233,
            321323,
            321332,
            322133,
            322313,
            322331,
            323123,
            323132,
            323213,
            323231,
            323312,
            323321,
            331223,
            331232,
            331322,
            332123,
            332132,
            332213,
            332231,
            332312,
            332321,
            333122,
            333212,
            333221,
            422444,
            424244,
            424424,
            424442,
            442244,
            442424,
            442442,
            444224,
            444242,
            444422,
            515555,
            551555,
            555155,
            555515,
            555551,
            666666,
            1224444,
        ]
        for x in BeautifulNumbers:
            if x > n:
                return x
        return -1  # Should not be reached given the constraints


class Helper:
    def generate_all_beautiful_numbers_less_than_2M(self):
        from itertools import permutations

        beautiful_numbers = set()

        # The length of a beautiful number is the sum of its constituent digits.
        # e.g., for 122333, the digits are 1, 2, 3. The length is 1+2+3=6.
        # We can find partitions of a number L (length) into distinct digits d_i.

        # Partitions of lengths up to 7 (since n <= 10^6, the next beautiful number won't be excessively large)
        # L=1: {1}
        # L=2: {2}
        # L=3: {3}, {1,2}
        # L=4: {4}, {1,3}
        # L=5: {5}, {1,4}, {2,3}
        # L=6: {6}, {1,5}, {2,4}, {1,2,3}
        # L=7: {7}, {1,6}, {2,5}, {3,4}, {1,2,4}

        digit_groups = [
            [1],
            [2],
            [3],
            [1, 2],
            [4],
            [1, 3],
            [5],
            [1, 4],
            [2, 3],
            [6],
            [1, 5],
            [2, 4],
            [1, 2, 3],
            [7],
            [1, 6],
            [2, 5],
            [3, 4],
            [1, 2, 4],
        ]

        for group in digit_groups:
            s = ""
            for digit in group:
                s += str(digit) * digit

            # Generate all unique permutations for the string s
            for p in set(permutations(s)):
                # Exclude numbers with leading zeros, though our groups avoid this.
                if p[0] != "0":
                    beautiful_numbers.add(int("".join(p)))

        return sorted(list(beautiful_numbers))


HelperInstance = Helper()
BeautifulNumbers = HelperInstance.generate_all_beautiful_numbers_less_than_2M()

# %%
