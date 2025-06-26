class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            number = nums[i]
            difference = target - number
            if difference in seen:
                return [seen[difference], i]
            else:
                seen[number] = i

# Explanation: 
# 1. we create an empty dictionary *seen{}* to store the numbers we have already seen
# 2. we then run a for loop to go throgh each indexes
# 3. then we fetch the number at the current index
# 4. we calculate the difference between the fetched number and the target required
# 5. we check if that difference number is in the seen dictionary
# 6. if it exists in the seen dictionary we will return that difference aswell as the number at that current index
# 7. if the difference is not found, then we will add that difference in the seen dictionary and will move to the next index
# Time Complexity: O(n)
