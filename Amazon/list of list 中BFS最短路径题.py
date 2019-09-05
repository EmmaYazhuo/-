# 0，1，9组成grid。从（0，0）出发，4个方向走。0能走，1不能走。到达9的最小步数。
# 给一个二维数组，里面有1，0，9，找从左上到有9的最小距离


#总结
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=476743


#小土刀    Maze????
# https://wdxtub.com/interview/14520850399861.html

# class Point:
#     int x;
# int y;
# public Point(int x, int y) {this.x = x;
# this.y = y;}}

def wallsAndGates(numRows, numColumns, lot):
    if numRows == 0 or numColumns == 0 or lot is None: return -1
    queue, visited = [], []
    queue.append([0,0])
    visited.append([0,0])
    step = 0
    deltaX = [0,1,0,-1]
    deltaY = [1,0,-1,0]
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            for i in range(4):
                nextX = curr[0] + deltaX[i]
                nextY = curr[1] + deltaY[i]
                if nextX < 0 or nextX >= numRows or nextY<0 or nextY>=numColumns or [nextX, nextY] in visited or lot[nextX][nextY] == 1:
                    continue
                if lot[nextX][nextY] == 9:
                    print([nextX, nextY])
                    print(step+1)
                    return step
                    break
                if lot[nextX][nextY] == 0 and [nextX, nextY] not in visited:
                    queue.append([nextX,nextY])
                    visited.append([nextX, nextY])
        step += 1

    return -1



def main():
    lot = [[1,0,0],[1,0,0],[1,9,1]]
    wallsAndGates(3,3,lot)

    # print("test case 2")
    # lot = [[9,0,0],[1,0,0],[1,0,0]]
    # wallsAndGates(3,3,lot)
    #
    # print("test case 3")
    # lot = [[1,0,0],[1,1,1],[1,1,9]]
    # wallsAndGates(3,3,lot) #4

    print("test case 4")
    lot = [[1,0,0],[1,1,0],[1,1,9]]
    wallsAndGates(3,3,lot) #4


main()
