#!/usr/bin/python3
'''
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 10**4
    -10**9 <= nums[i] <= 10**9
    -10**9 <= target <= 10**9
    Only one valid answer exists.
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print('nums=', nums, ' target=', target)
        if( len(nums) < 2) | (len(nums) > 10**4):
            print('nums.length < 2 or length > 10**4')
            return []
        # setNums = set(nums)
        # if( len(nums) != len(setNums)):
        #     print('list include same element twice')
        #     return []
        if( (min(nums) < -10**9) | (max(nums) > 10**9)):
            print('nums < -10**9 or nums > 10**9')
            return []
        if( (target < -10**9) | (target > 10**9)):
            print('target < -10**9 or target > 10**9')
            return []
        for i in nums:
            x = nums.index(i)
            # print('x=', x)
            for y in range(x+1, len(nums)):
                # print('y=', y)
                j = nums[y]
                if( i+j == target ):
                    return [x, y]
        return []
    
sol = Solution()
print(sol.twoSum([1], 1))
print(sol.twoSum([1,1], 2))
print(sol.twoSum([-10**9-1, 10**9], 3))
print(sol.twoSum([10**9+1, -10**9], 4))
print(sol.twoSum([1,2,3,4], 5))
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
print(sol.twoSum([-1,-2,-3,-4,-5,-6], -8))
print(sol.twoSum([0, 3, -3, 4, -1], -1))
