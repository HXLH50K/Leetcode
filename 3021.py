class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_odds = n // 2 + 1 if n & 1 else n // 2
        n_evens = n - n_odds
        m_odds = m // 2 + 1 if m & 1 else m // 2
        m_evens = m - m_odds
        return n_odds * m_evens + n_evens * m_odds
