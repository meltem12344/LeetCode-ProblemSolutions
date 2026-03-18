class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split() # seperate the words with split()
        lastWord = words[-1] #  get the last word from the list of words
        return len(lastWord) # length of last word is returned
        