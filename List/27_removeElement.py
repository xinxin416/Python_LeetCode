# 原地删除元素，赋值元素
# 直接删除，会导致索引变化
# 直接对数组赋值
# 输入： [0,1,3,0,4],2
def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    ans = 0
    for num in nums:
        if num != val:
            nums[ans] = num
            ans += 1
    return ans

'''
方法二：修改指针长度，并交换元素。
    ans = len(nums)
    i = 0
    while i <= ans :
        if nums[i] == val:
            nums[i] = nums[ans-1] # 交换元素，i 下标替换为最后一个元素
            ans -= 1
        else:
            i += 1
    return ans 
'''
