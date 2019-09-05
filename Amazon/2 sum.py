# https://www.1point3acres.com/bbs/interview/amazon-software-engineer-453412.html

target = 20
input = ([[1,8],[3,9], [2,15]],  [[1,8], [2,11], [3,12]] )
output = [[1, 3], [3, 2]]

def twosumclosest(nums, target):
    dic={}
    res=[]
    for i, num in enumerate(nums):
        if target - num in dic.keys():
            res.append(dic[target - num])
            res.append(i)

        else:
            dic[num]=i
    return res