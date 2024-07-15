# %%
from typing import List
from collections import defaultdict


class Solution:
    def dfs(self, email, emails):
        if email not in self.visited:
            self.visited.add(email)
            emails.add(email)
            for next_email in self.email_graph[email]:
                self.dfs(next_email, emails)
        return emails

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create a graph where each email points to its self.owner and connected emails
        self.email_graph = defaultdict(set)
        self.owner = {}
        for account in accounts:
            for email in account[1:]:
                self.email_graph[account[1]].add(email)
                self.email_graph[email].add(account[1])
                self.owner[email] = account[0]

        self.visited = set()
        merged_accounts = []
        for email in self.email_graph:
            if email not in self.visited:
                emails = self.dfs(email, set())
                merged_accounts.append([self.owner[email]] + sorted(emails))

        return merged_accounts


# Example usage
accounts = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"],
]
solution = Solution()
print(solution.accountsMerge(accounts))

# %%
