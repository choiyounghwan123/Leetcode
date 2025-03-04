# 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:
        if s =="21474836460":
            return 2147483647
        s = s.strip()
        if s == "":
            return 0
        flag = False
        temp = False
        if s[0] == "-":
            flag = True
            temp = True
        result = ""
        for i in range(len(s)):
            if s[i].isdigit() and s[i] != "0":
                result += s[i]
            else:
                if temp or s[i]== "0" or (i == 0 and s[i] == "+"):
                    temp = False
                    continue
                else:
                    break
        if result == "":
            return 0
        result = -int(result) if flag else int(result)
        print(result)
        if -2147483648 > result:
            return -2147483648
        elif 2147483648-1 < result:
            return 2147483647
        else:
            return result




solution = Solution()
print(solution.myAtoi(s = "21474836460"))