class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                for delta in (1, -1):
                    nd = (int(state[i]) + delta) % 10
                    nxt = state[:i] + str(nd) + state[i+1:]
                    if nxt not in deadends:
                        neighbors.append(nxt)
            return neighbors

        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            state, steps = q.popleft()
            if state == target:
                return steps
            for next_state in get_neighbors(state):
                if next_state not in visited:
                    visited.add(next_state)
                    q.append((next_state, steps + 1))
        return -1