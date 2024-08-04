## 2数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## 字典存储已遍历数值及其索引。preNums
        # 判断目标值是否在已遍历字典内
        # 键不存在时，设置默认值
        preNums = {}

        for j in range(0,len(nums)):
            targetNum = target-nums[j]
            targetNumIndex = preNums.setdefault(targetNum,'undefined')
            # preNums[targetNum]
            if targetNumIndex != 'undefined':
                return [targetNumIndex,j]
            else:
                preNums[nums[j]] = j

