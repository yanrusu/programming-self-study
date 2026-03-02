import sys
sys.setrecursionlimit(50000)
def explore(row, col):
    # Mark the current square as visited
    grid[row][col] = '#'
    
    # Explore the adjacent floor squares (up, down, left, right)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == '.':
            explore(new_row, new_col)

# Read the input values
n, m = map(int, input().split())

# Read the map and create the grid
grid = [list(input()) for _ in range(n)]

# Initialize the room count
room_count = 0

# Iterate through each square in the grid
for row in range(n):
    for col in range(m):
        if grid[row][col] == '.':
            # Perform DFS from unvisited floor squares
            explore(row, col)
            room_count += 1

# Print the room count
print(room_count)
