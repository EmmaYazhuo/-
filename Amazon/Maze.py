# 给个array,其中只有一格是9，其他格子是0或1，0表示此路不通，1表示可以走，判断从（0,0) 点开始上下左右移动能否找到这个是9的格子
# return 1 if yes else 0



def maze(matrix):
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    m, n = len(matrix), len(matrix[0])
    if not matrix or len(matrix)==0 or len(matrix[0])==0: return 0
    if matrix[0][0] == 9: return 1
    queue = []
    queue.append([0,0])
    matrix[0][0] = 1
    step = 0
    while queue:
        cur = queue.pop(0)
        count = 0
        for i in range(4):
            next = [cur[0]+dx[i], cur[1]+dy[i]]
            if next[0] >= 0 and next[0] < m and next[1] >= 0 and next[1] < n:
                if matrix[next[0]][next[1]] == 9: return step + 1
                elif matrix[next[0]][next[1]] == 0:
                    queue.append(next)
                    matrix[next[0]][next[1]] = 1
        step += 1
    return 0

def main():
    matrix = [[1,0,0],[1,0,0],[1,9,1]]
    print(maze(matrix))    ####Changes it to count the min steps



main()