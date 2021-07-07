class Solution(object):
    def isValid(self, s):
        
        a = 0 # ()
        b = 0 # {}
        c = 0 # []
        last_open = [" "]
        for i in s:
            print(i)
            if a < 0 or b < 0 or c < 0:
                return False
            elif i == "(":
                a += 1
                last_open.append("(")
            elif i == ")":
                a -= 1
                if last_open[-1] != "(":
                    return False
                else:
                    last_open.pop()
            elif i == "{" :
                b += 1
                last_open.append("{")
            elif i == "}":
                b -= 1
                if last_open[-1] != "{":
                    return False
                else:
                    last_open.pop()
            elif i == "[" :
                c += 1
                last_open.append("[")
            elif i == "]":
                c -= 1
                if last_open[-1] != "[":
                    return False
                else:
                    last_open.pop()
            
        if a == 0 and b == 0 and c == 0:
                return True
        else:
                return False
