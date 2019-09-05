s = "babad"
out = "bab"

i = 0
j = 0
print(s[i+1: j])


def longestPalindrome(self, s: str) -> str:
    #Even and odd cases
    res=""
    for i in range(len(s)):
        tmp=self.isPalindrome(s, i, i)
        if len(tmp) > len(res):
            res=tmp
        tmp=self.isPalindrome(s, i, i + 1)
        if len(tmp) > len(res):
            res=tmp
    return res


def isPalindrome(self, s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i-=1
        j+=1
    return s[i + 1: j]