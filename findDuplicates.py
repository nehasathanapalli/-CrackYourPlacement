class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq_map = {}
        result = []

        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1 #defaults val of key(num) to 0 if it's not yet in the dictionary
        for key, val in freq_map.items():
            if val > 1:
                result.append(key)
        # if not result: #if no duplicates are found
        #         result.append(-1)

        result.sort()
        return result
