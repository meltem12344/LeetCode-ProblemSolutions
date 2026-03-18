class Solution(object):
    def twoSum(self, nums, target):   # constructor method
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            for j, numx in enumerate(nums[i+1:], start=i+1):  # bu mantığı yeni öğrendim 
                if (num + numx == target):
                    return [i, j]

# enumerate içinde ilk ögeden başlayıp dönmek istiyorsan tüm listeyi argümanında aldığın listenin istediğin kısmından kesip ondan sonra kullanacabilirsin. İkinci bir argüman olan startı da o karar verdiğin indexten başlatacaksın. 

# genel testte geçtik ayrıntılısını geçemedik çünkü ikinci döngüdeki nums[1:] kısmı her yeni üst döngüde eklenecek sayıyı getirirken ikinci elemandan başlatıyor bu da yanlış sonuca götürür. 

# Şunu istiyorum: ikinci döngüde üst döngüde her yeni sayıya geçtiğimizde o sayının bir sonraki indexindeki elemanından başlayarak kontolü sağlamak.