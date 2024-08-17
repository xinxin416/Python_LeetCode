# 是否字母异位词
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 题干字母异位词定义：长度相等、每个字符出现次数相等
        # 判断是否字母异位词，长度是否相等，字符排序后每个位置是否相等
        ns = len(s)
        nt = len(t)
        s1 = sorted(s)
        t1 = sorted(t)
        if ns != nt  or   s==t :
            return False
        elif  s1 == t1 :
            return True
        else:
            return False


s = 'anagram'
t = 'nagaram'
p = Solution()
print(p.isAnagram(s,t))