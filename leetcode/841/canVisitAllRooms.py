class Solution:
    def canVisitAllRooms(self, rooms: list) -> bool:
        N = len(rooms)
        have = [0 for i in range(N)]
        have[0] = 1
        l = rooms[0]
        flag = True
        while flag:
            tmp = []
            flag = False
            for i in l:
                if have[i] != 1:
                    have[i] = 1
                    flag = True
                    for j in rooms[i]:
                        if have[j] != 1:
                            flag = True
                            have[j] = 2  # 还没走过的房间标记2
                            tmp.append(j)
            l = tmp
        return 0 not in have

a = [[1],[2],[3],[]]
s = Solution()
res = s.canVisitAllRooms(a)
print(res)
