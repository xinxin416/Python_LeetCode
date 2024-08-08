# 子数组之和大于等于目标值，取最下子数组
# 双指针方式，右指针等于左指针
# 子数组长度在右指针-左指针时+1
# 如果子数组长度等于数组长度，取0，否则取最小结果
# 注意循环退出条件
# 返回结果初始值需大于数组长度本身

def minSubList(nums,target):
    left = 0
    n = len(nums)
    result = n + 1
    while left < n :
        tmp = 0
        right = left
        while right < n :
            tmp += nums[right]
            if tmp >= target:
                result = min( result, right - left +1 )
                break
            else:
                right += 1
        left += 1
    return 0 if result==n+1 else result

nums =[1,4,4]
target = 4
print(minSubList(nums,target))

