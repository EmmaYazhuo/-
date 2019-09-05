import sys
# sCount = int(input())
# for line in sys.stdin:
    # start of a new sheet
# while True:
# line = input()
#     if len(line.strip().split(' ')) != 2:
#         break
#     else:
#         h,w = line.strip().split(' ')
#         h,w = int(h),int(w)
#         sheet = [[0 for _ in range(w)] for _ in range(h)]
#         dirs = [[0,1],[0,-1],[1,0],[-1,0]]
#         dotNum = int(input())
#         queue = []
#         for i in range(dotNum):
#             dotLine = input()
#             # dotLine = list(map(int,dotLine.strip().split(' ')))
#             x,y,darkness = list(map(int,dotLine.strip().split(' ')))
#             sheet[x][y] = max(sheet[x][y],darkness)
#             if[x,y] not in queue:
#                 queue.append([x,y])
#         queue.sort(key = lambda x: -sheet[x[0]][x[1]])
#         while queue:
#             curPos = queue.pop(0)
#             x,y = curPos[0],curPos[1]
#             darkness = sheet[x][y]
#             for dir in dirs:
#                 newx = x + dir[0]
#                 newy = y + dir[1]
#                 newdarkness = darkness - 1
#                 if newx >= 0 and newy >= 0 and newx < h and newy < w and newdarkness > sheet[newx][newy]:
#                     queue.append([newx,newy,newdarkness])
#                     sheet[newx][newy] = newdarkness
#         print(sum(sheet[x][y] for x in range(h) for y in range(w)))

def Int_Bleed(number_of_sheets, line, dotNum, dotLines): #line: h and w
    if len(line.strip().split(' ')) != 2:
        return -1 ##return what?
    else:
        h, w = line.strip().split(' ')
        h, w = int(h), int(w)
        sheet = [[0 for _ in range(w)] for _ in range(h)]
        # print(sheet)
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = []
        #enqueue first dotNum
        for dotLine in dotLines:
            # for i in range(dotNum):
            x, y, darkness = list(map(int, dotLine.strip().split(' ')))
            # print(x, y, darkness)
            sheet[x][y] = max(sheet[x][y], darkness)
            if [x, y] not in queue:
                queue.append([x, y])
        queue.sort(key = lambda x: -sheet[x[0]][x[1]])
        # print(sheet)
        # print(queue)
        while queue:

            curPos = queue.pop()
            # print(curPos)
            x, y = curPos[0], curPos[1]
            # print(x, y)
            darkness = sheet[x][y]
            newdarkness = darkness - 1
            # print(darkness)
            for dir in dirs:
                newx = x + dir[0]
                newy = y + dir[1]
                # print(newx, newy)
                # print(sheet[newx][newy])
                if newx >= 0 and newy >= 0 and newx < h and newy < w and newdarkness > sheet[newx][newy]:
                    queue.append([newx, newy, newdarkness])
                    sheet[newx][newy] = newdarkness
        print(sum(sheet[x][y] for x in range(h) for y in range(w)))
        # print(sheet)
        return sum(sheet[x][y] for x in range(h) for y in range(w))
# sum = Int_Bleed(2, '3 4', 2, ['0 0 225', '1 2 255'])
# sum = Int_Bleed(2, '5 6', 4, ['1 0 10', '2 2 9', '2 3 5', '4 2 9'])
sum = Int_Bleed(1, '500 500', 1, ['0 0 4000'])


# 时间复杂度还是O(Height*Width*n)
# 空间复杂度 O(H*W)
#?priority queue
#墨水的值不能为负
#看是OA几？ 大概率是这道题？



# input
# 2 number of sheets
# 3 4 height&width
# 2 number of dots
# 0 0 255
# 1 2 255
# 5 6
# 4
# 1 0 10
# 2 2 9
# 2 3 5
# 4 2 9
# output
# 3046
# 217


# 3
# 3 4
# 2
# 0 0 255
# 1 2 255
# 5 6
# 4
# 1 0 10
# 2 2 9
# 2 3 5
# 4 2 9
# 500 500
# 1
# 0 0 4000

# import sys
# sCount = int(input())
# # for line in sys.stdin:
#     # start of a new sheet
# while True:
#     line = input()
#     if len(line.strip().split(' ')) != 2:
#         break
#     else:
#         h,w = line.strip().split(' ')
#         h,w = int(h),int(w)
#         sheet = [[0 for _ in range(w)] for _ in range(h)]
#         dirs = [[0,1],[0,-1],[1,0],[-1,0]]
#         dotNum = int(input())
#         queue = []
#         for i in range(dotNum):
#             dotLine = input()
#             # dotLine = list(map(int,dotLine.strip().split(' ')))
#             x,y,darkness = list(map(int,dotLine.strip().split(' ')))
#             sheet[x][y] = max(sheet[x][y],darkness)
#             if[x,y] not in queue:
#                 queue.append([x,y])
#         queue.sort(key = lambda x: -sheet[x[0]][x[1]])
#         while queue:
#             curPos = queue.pop(0)
#             x,y = curPos[0],curPos[1]
#             darkness = sheet[x][y]
#             for dir in dirs:
#                 newx = x + dir[0]
#                 newy = y + dir[1]
#                 newdarkness = darkness - 1
#                 if newx >= 0 and newy >= 0 and newx < h and newy < w and newdarkness > sheet[newx][newy]:
#                     queue.append([newx,newy,newdarkness])
#                     sheet[newx][newy] = newdarkness
#         print(sum(sheet[x][y] for x in range(h) for y in range(w)))
#
#

# 我test case过了，是用priority queue 做bfs，每次只dequeue 目前扩散的ink value最大那个queue，这样可以避免重复计算grid cell的值



2013-01-01
2013-01-01
[34.38, 34.36, 34.74, 35.26, 35.23, 35.29, 35.64, 36.02, 36.1, 36.98, 37.01, 36.75, 36.01, 35.66, 34.72, 33.9, 32.62, 31.51, 30.73, 29.5, 26.94, 25.47, 23.84, 22.55]
24
1