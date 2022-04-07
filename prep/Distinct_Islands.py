grid = [
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1], 
    [1, 1, 0, 0, 0]]

import collections

def distinct_islands(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    

    def dfs(r, c, origin_r, origin_c):
        nonlocal island_size
        nonlocal island
        if (0 <= r < rows) and (0 <= c < cols) and grid[r][c] == 1:
            grid[r][c] = "#" 
            island_size += 1
            island.append((r - origin_r, c - origin_c))

            for x, y in directions:
                new_r, new_c = r + x, c + y
                dfs(new_r, new_c, origin_r, origin_c)

    all_islands = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                origin_r, origin_c = r, c
                island, island_size = [], 0
                dfs(r, c, origin_r, origin_c)
                all_islands.append((island, island_size))

    size_to_island = collections.defaultdict(list)
    for island, island_size in all_islands:
        if island not in size_to_island[island_size]:
            size_to_island[island_size].append(island)
   
    # print(f'Total Groups: {total_unique_groups}')

    total = 0
    for key, val in size_to_island.items():
        group_size = len(val)
        total += group_size
        print(f'Groups of {key}: {group_size}')
    print(f'Total Groups: {total}')
  
  

print(distinct_islands(grid))

