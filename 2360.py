class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n = len(edges)
        longest = -1
        visited = set()

        # For each node, store distance from current start node
        def dfs(node: int, dist: dict) -> None:
            nonlocal longest

            # Mark current node as visited for this iteration
            visited.add(node)
            curr_dist = dist[node]

            # Get next node from edges
            next_node = edges[node]

            # No outgoing edge case
            if next_node == -1:
                return

            if next_node in dist:
                # Found a cycle - calculate length
                cycle_len = curr_dist - dist[next_node] + 1
                longest = max(longest, cycle_len)
            elif next_node not in visited:
                # Continue DFS with updated distance
                dist[next_node] = curr_dist + 1
                dfs(next_node, dist)

        # Try each unvisited node as start of potential cycle
        for start in range(n):
            if start not in visited:
                dfs(start, {start: 0})

        return longest
