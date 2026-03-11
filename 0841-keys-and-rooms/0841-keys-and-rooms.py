from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        ln = len(rooms)
        boolDoorCheck = [False for _ in range(ln)]
        keys = deque()
        keys.append(0)

        while keys:
            key = keys.popleft()
            if boolDoorCheck[key] == True:
                continue
            elif boolDoorCheck[key] == False:
                boolDoorCheck[key] = True
                keys +=rooms[key]

        
        if boolDoorCheck[0] == True and len(set(boolDoorCheck)) == 1:
            return True
        else:
            return False

        print("ln = ", ln)
        print("already opened: ",boolDoorCheck)
        print("keys: ", keys)


k = Solution()
rooms = rooms = [[1],[2],[3],[]]

print(k.canVisitAllRooms(rooms))
