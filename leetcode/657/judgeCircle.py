class Solution:
    def judgeCircle1(self, moves: str) -> bool:
        movesList = list(moves)
        tmpList = []
        dd = {
            "U": "D",
            "D": "U",
            "L": "R",
            "R": "L"
        }
        for i in range(len(moves)):
            other = dd[moves[i]]
            if other in tmpList:
                tmpList.remove(other)
            else:
                tmpList.append(moves[i])
        if not tmpList:
            return True
        else:
            return False

    def judgeCircle2(self, moves: str) -> bool:
        x = y = 0
        for i in moves:
            if i == "U":
                y += 1
            elif i == "D":
                y -= 1
            elif i == "L":
                x -= 1
            elif i == "R":
                x += 1
        return x == 0 and y == 0

a = Solution()
res = a.judgeCircle2("RLUURDDDLU")
print(res)
