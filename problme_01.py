class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 , len2 = len(word1), len(word2)
        i, j = 0,0
        merged = ""
        while i < len1 and j < len2:
            merged+= word1[i] + word2[j]
            i+=1
            j+=1
        while i < len1:
            merged+= word1[i]
            i+=1
        while j < len2:
            merged+= word2[j]
            j+=1
        return merged
