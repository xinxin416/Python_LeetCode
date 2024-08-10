import math
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ## 循环不变量方法，遍历每一条边
        ## 考虑奇数的中间值情况
        # 遵循左闭右开原则
        circle = math.floor(n/2)
        startx,starty = 0,0
        count  = 1
        side = 1 # 留出最后一条边
        mid = int(math.floor(n/2))

        result = [[0 for _ in range(n)] for _ in range(n)]
        while circle > 0 :
            i,j = startx,starty
            while j < n-side : # 遍历第一条横边
                result[startx][j] = count
                j += 1
                count += 1
            while i < n-side : # 遍历第一条竖边
                result[i][j] = count
                i += 1
                count += 1
            while j > starty : # 遍历第二条横边
                result[i][j] = count
                j -= 1
                count += 1
            while i > startx: # 遍历第二条竖边
                result[i][starty] = count
                i -= 1
                count += 1

            ## 第一层循环遍历结束，重置起始位置
            startx += 1
            starty += 1
            side += 1
            circle -= 1
        if n % 2 != 0 :
            result[mid][mid] = count
        return result