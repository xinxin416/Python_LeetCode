class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0,len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else :
                if len(stack) == 0 : return False
                if stack.pop() != s[i] : return False
        return len(stack) == 0