class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds = []
        evens = []
        odd_first_gap = []
        even_first_gap = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
                if not even_first_gap or even_first_gap[-1] % 2 == 1:
                    even_first_gap.append(num)
                if odd_first_gap and odd_first_gap[-1] % 2 == 1:
                    odd_first_gap.append(num)
            else:
                odds.append(num)
                if not odd_first_gap or odd_first_gap[-1] % 2 == 0:
                    odd_first_gap.append(num)
                if even_first_gap and even_first_gap[-1] % 2 == 0:
                    even_first_gap.append(num)
        print(odds, evens, odd_first_gap, even_first_gap)
        return (
            max(len(odds), len(evens), len(odd_first_gap), len(even_first_gap))
            if nums
            else 0
        )
