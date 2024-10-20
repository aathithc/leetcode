class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for i in s:
            if i == "(":
                count += 1
                res.append(i)
            elif i == ")" and count > 0:
                count -= 1
                res.append(i)
            elif i != ")":
                res.append(i)
        filtered = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])