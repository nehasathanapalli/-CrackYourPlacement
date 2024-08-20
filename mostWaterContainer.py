class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = max(area, min(height[i],height[j])*(j-i))
        return area
