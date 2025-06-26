# Leetcode
## Solution and Explanation to all leetcode problems in *PYTHON*

### 01. Two Sum
#### Code: https://github.com/iammartariq/Leetcode/blob/main/1.%20Two%20Sum.py
#### Explanation: 
1. we create an empty dictionary *seen{}* to store the numbers we have already seen
2. we then run a for loop to go throgh each indexes
3. then we fetch the number at the current index
4. we calculate the difference between the fetched number and the target required
5. we check if that difference number is in the seen dictionary
6. if it exists in the seen dictionary we will return that difference aswell as the number at that current index
7. if the difference is not found, then we will add that difference in the seen dictionary and will move to the next index
#### Time Complexity: O(n)
#### Space Complexity: O(n)

### 09. 
#### code: https://github.com/iammartariq/Leetcode/blob/main/9.%20Palindrome%20Number.py
#### Explanation:
1. palindrome is any number which remains same if we invert it: for example 121 
2. we cannot reverse a number directly using int, so we convert it into string
3. we then invert the string 
4. then we compare both, for a number to be palindrome it should be equal to its reversed form
#### Time Complexity: O(n)
#### Space Complexity: O(n)
