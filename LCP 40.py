# %%
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        n = len(cards)
        scores = cards[:cnt]
        res = sum(scores)
        if res % 2 == 0:
            return res

        scores_even = [i for i in scores if i % 2 == 0]
        scores_odd = [i for i in scores if i % 2 == 1]
        min_even_in_scores = min(scores_even) if scores_even else None
        min_odd_in_cards = min(scores_odd) if scores_odd else None

        rest_even = [i for i in cards[cnt:] if i % 2 == 0]
        rest_odd = [i for i in cards[cnt:] if i % 2 == 1]
        max_even_in_rest = max(rest_even) if rest_even else None
        max_odd_in_rest = max(rest_odd) if rest_odd else None

        res_1 = (
            res - min_even_in_scores + max_odd_in_rest
            if min_even_in_scores and max_odd_in_rest
            else 0
        )
        res_2 = (
            res - min_odd_in_cards + max_even_in_rest
            if min_odd_in_cards and max_even_in_rest
            else 0
        )
        return max(res_1, res_2)
