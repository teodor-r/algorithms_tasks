"""
Description
Задачка на подсчёт компонент связности в неорентированном графе
Решена на основе dfs
"""
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
class Solution(object):
    def __init__(self):
        pass
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]] # матрица смежности
        :rtype: int
        """
        # подсчёт компонент сильной связности
        self.ln = len(isConnected)
        N = 0
        used = set()
        G = isConnected
        for vertex in range(self.ln):
            if vertex not in used:
                self.dfs(vertex, G, used)
                N += 1
        return N

    def dfs(self, vertex, G, used):
        used.add(vertex)
        for neib in range(self.ln):
            if G[vertex][neib] !=0  and neib not in used:
                self.dfs(neib, G, used)
#inst = Solution()
#print(inst.findCircleNum(isConnected))
