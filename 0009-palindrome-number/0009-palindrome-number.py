class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            reverse = int(str(x)[::-1]) # get the reverse of the number
            if reverse == x: # if reverse is equal return true
                return True
            return False
        else:
            return False

        