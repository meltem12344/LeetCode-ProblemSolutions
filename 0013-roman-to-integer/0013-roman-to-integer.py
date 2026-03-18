class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # etkisiz eleman
        total=0
  


        # istisnai olanlar
        patternDict ={
            'IV' : -2,
            'IX' : -2,
            'XL' : -20,
            'XC' : -20,
            'CD' : -200,
            'CM' : -200,
        }

        # her harfin değeri için dict oluştur
        dict ={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        # her harfin karşılık geldiği sayısal değeri total değişkenine ekle

        patternList = []
        listOfs = list(s)

        for i in range(len(s)-1):

            pattern = s[i]+s[i+1] # her bir ikiliyi alamak için 
            if pattern in ['IV','IX','XL','XC','CD','CM']:
                patternList.append(pattern)
            else:
                continue

        for i in listOfs:
            total = total + dict[i]
        
        for i in patternList:
            total = total + patternDict[i]
        


        return total
            



        