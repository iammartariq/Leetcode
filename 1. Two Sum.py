class Solution(object):
  def twosum(self, nums, target):
    seen = {} #creating an empty dictionary to store the numbers which are seen before
    for i in range(len(nums)): #going through each indexs
      number = nums[i] #getting the number of the current index
      difference = target - number #checking the difference between the required target and the number we get from the index
      if difference in seen: #if the difference calculated exists in the seen dictionary
        return [seen(difference), i] # we will return the difference aswell as the number found
      else:
        seeen[number] = i #else if difference doesnt exist in seen then we will add this difference in the seen

# the code runs in O(N) time complexity
# i added comments with each line explaining the working and need of each line
# feel free to reach out to me if you need help or there is some error or need of modifications
