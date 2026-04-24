from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq = Counter(moves)
        cnt_L = freq.get('L', 0)
        cnt_R = freq.get('R', 0)
        cnt__ = freq.get('_', 0)
        if cnt_L > cnt_R:
            return cnt_L - cnt_R + cnt__
        elif cnt_R > cnt_L:
            return cnt_R - cnt_L + cnt__
        else:
            return cnt__
        