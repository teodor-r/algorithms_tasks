from collections import deque
deque = deque()
rooms = [[1],[2],[3],[]]
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        g = self.generate_graph(rooms)

        for neibs in g:
            if len(neibs) == 0:
                #print("false")
                return
        print("true")
    def generate_graph(self, rooms):
        g = [set() for i in range(len(rooms))]
        deque.append(0)
        used  = set()
        used.add(0)
        while deque:
            crnt_rm  = deque.popleft()
            for room in rooms[crnt_rm]:
                if  room not in used:
                    deque.append(room)
                    used.add(room)
                g[crnt_rm].add(room)
                g[room].add(crnt_rm)
        return g
    def bfs(self, vertex,g,used):
        used.add(vertex)
        for vrt in g[vertex]:
            if  vrt not in used:
                self.bfs(vrt,g,used)
inst = Solution()
inst.canVisitAllRooms(rooms)

