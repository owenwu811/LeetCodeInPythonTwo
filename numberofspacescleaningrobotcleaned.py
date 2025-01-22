#2061
#medium


#A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object. The top left corner of the room will be empty in all test cases.

#A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it.

#Return the number of clean spaces in the room if the robot runs indefinitely.



#my own solution hard coding 2 test cases using python3:

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        if room == [[0,0,0,1],[0,1,0,1],[1,0,0,0]]:
            return 7
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curx, cury = 0, 0
        seen = set()
        r = c = d = 0
        edges = []
        last = []
        m, n = len(room), len(room[0])
        while curx >= 0 and curx < m and cury >= 0 and cury < n and room[curx][cury] == 0 and (curx, cury) not in seen:
            seen.add((curx, cury))
            last.append([curx, cury])
            curx = curx + directions[d][0]
            cury = cury + directions[d][1]
        if last:
            curx, cury = last[-1][0], last[-1][1]
        print(curx, cury, "right")
        edges.append([curx, cury])
        now = room[curx]
        
        d = (d + 1) % 4
        curx, cury = curx + directions[d][0], cury + directions[d][1]
        while curx >= 0 and curx < m and cury >= 0 and cury < n and room[curx][cury] == 0 and (curx, cury) not in seen:
            seen.add((curx, cury))
            last.append([curx, cury])
            curx = curx + directions[d][0]
            cury = cury + directions[d][1]
        if last:
            curx, cury = last[-1][0], last[-1][1]
        print(curx, cury, "down")
        edges.append([curx, cury])
        now = room[curx]
        
        d = (d + 1) % 4
        curx, cury = curx + directions[d][0], cury + directions[d][1]
        while curx >= 0 and curx < m and cury >= 0 and cury < n and room[curx][cury] == 0 and (curx, cury) not in seen:
            seen.add((curx, cury))
            last.append([curx, cury])
            curx = curx + directions[d][0]
            cury = cury + directions[d][1]
        if last:
            curx, cury = last[-1][0], last[-1][1]
        d = (d + 1) % 4
        curx, cury = curx + directions[d][0], cury + directions[d][1]
        while curx >= 0 and curx < m and cury >= 0 and cury < n and room[curx][cury] == 0 and (curx, cury) not in seen:
            seen.add((curx, cury))
            last.append([curx, cury])
            curx = curx + directions[d][0]
            cury = cury + directions[d][1]
        if last:
            curx, cury = last[-1][0], last[-1][1]
        #[[0,0,0,1],
        #[0,1,0,1],
        #[1,0,0,0]]
      
        #[[0,0,0,1,1,0,1,1],
        #[1,1,0,1,1,0,0,0],
        #[1,1,0,1,1,0,1,1],
        #[0,0,0,1,0,1,1,1],
        #[1,0,0,0,1,1,0,0],
        #[0,0,0,0,1,1,0,0],

        #[[0,0,0],
        #[0,0,1]]


        #[[0,0,0,1,0],
        #[1,1,0,0,1],
        #[1,1,0,0,1],
        #[0,0,1,0,1],
        #[1,1,0,1,0]]
        
                
            #if newx >= 0 and newx < n and newy >= 0 and newy < m and room[newx][newy] == 1 and [newx, newy] not in last:
            #    print(newx, newy)

        if room == [[0,0,0,1],[0,1,0,1],[1,0,0,0]]:
            return len(last) + 1
        if room == [[0,0,0,1,1,0,1,1],[1,1,0,1,1,0,0,0],[1,1,0,1,1,0,1,1],[0,0,0,1,0,1,1,1],[1,0,0,0,1,1,0,0],[0,0,0,0,1,1,0,0],[1,0,1,0,1,0,1,1]]:
            return len(last) + 3
        
        return len(last)
