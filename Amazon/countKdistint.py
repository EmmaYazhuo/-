
def countkDist(str1, k):
    n = len(str1)
    count = 0
    for i in range(n):
        countdic = [0]*27
        countk = 0
        for j in range(i, n):
            if countdic[ord(str1[j])-97]==0:
                countk += 1
            countdic[ord(str1[j])-97] += 1
            if countk == k:
                count += 1
            if countk > k: break
    return count


# Driver Code
if __name__ == "__main__":
    str1 = "abcbaa"
    k = 3
    print("Total substrings with exactly", k,
           "distinct characters : ", end = "")
    print(countkDist(str1, k))