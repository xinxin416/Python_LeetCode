
class Solution(object):
    def bitSquareSum(self,n):
        sum = 0
        while n > 0 :
            bit = n % 10
            sum += bit*bit
            n = n // 10

        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## 不能使用集合，利用数值位数计算
        # 适用快慢指针，慢指针走一步，快指针走两步?
        # 当slow == fast 时，回到起点，一个循环周期结束
        slow ,fast = n, n
        while True :
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            if slow == fast :
                break
        return slow == 1

s = Solution()
print(s.isHappy(19))