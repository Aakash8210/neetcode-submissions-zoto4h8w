class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=1
        high=num
        while low<=high:
            mid=low+((high-low)//2)
            sq=mid*mid
            if sq>num:
                high=mid-1
            elif sq<num:
                low=mid+1
            else:
                return True
        return False
        