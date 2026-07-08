class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while que and fresh > 0:
            length = len(que)
            for i in range(length):
                row, col = que.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        que.append((r, c))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1