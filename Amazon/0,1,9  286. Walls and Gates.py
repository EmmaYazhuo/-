import collections
# 给个array,其中只有一格是9，其他格子是0或1，0表示此路不通，1表示可以走，判断从（0,0) 点开始上下左右移动能否找到这个是9的格子
# return 1 if yes else 0
def wallsAndGates(rooms) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return
    if rooms[0][0] == 9: return 0
    r, c = len(rooms), len(rooms[0])
    queue=collections.deque([])
    queue.append((0,0,0))
    while queue:
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 1:
                    queue.append((i, j, 1))
                    visited = set()
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        if rooms[x][y] == 9:
                            print(min(rooms[x][y], val))
                            return min(rooms[x][y], val)
                        visited.add((x, y))
                        rooms[x][y] = min(rooms[x][y], val)
                        queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                        queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))

def main():
    lot = [[1,0,0],[1,0,0],[1,9,1]]
    wallsAndGates(lot)

    print("test case 2")
    lot = [[9,0,0],[1,0,0],[1,0,0]]
    wallsAndGates(lot)

    print("test case 3")
    lot = [[1,0,0],[1,1,1],[1,1,9]]
    wallsAndGates(lot) # 4


main()


