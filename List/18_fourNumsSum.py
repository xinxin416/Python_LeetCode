# 四数之和，在给定n个数的数组中，找出不连续且不重复的4个数的和等于目标值的四元数组
# 关键是不重复
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 想复杂了，不必用滑动窗口，直接循环
        # 在循环基础上进行优化
        # 关键是避免元祖重复，因此每层循环元素在前一个元素往后移一位
        # 1.4层循环减到3层，第四层用双指针
        # 循环基础上再做修剪，预估后三/两个值是否大/小于目标值
        # 对输入值进行排序
        i,j = 0,0
        out = list()
        n = len(nums)
        if n<4 :
            return out
        nums.sort()
        for i in range(n-3):  # 可以写成range(n-3)
            # 下一轮开始前需和前一个数比较是否重复遍历
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 如果前i之后3个数和>target，直接退出
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target :
                break
                #如果i之后倒数3个数和<target,进入下一轮循环
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target:
                continue
            for j in range(i+1,n-2):
                # 下一轮开始前需和前一个数比较是否重复遍历
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                left,right = j + 1,n -1
                while left < right :
                    total = nums[i]+nums[j]+nums[left]+nums[right]
                    if total == target:
                        out.append([nums[i],nums[j],nums[left],nums[right]])
                        # 后两个元素相等直接进行下一轮，在这之前再次判断是否重复
                        while left < right  and nums[left] == nums[left +1]:
                            left += 1
                        left += 1
                        while left < right  and nums[right] == nums[right -1]:
                            right -= 1
                        right -= 1
                    elif total<target :
                        left += 1
                    else:
                        right -= 1

        return out