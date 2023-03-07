#!/usr/bin/python3
'''
https://leetcode.com/problems/palindrome-number/
9. Palindrome Number
Given an integer x, return true if x is a
palindrome
, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -231 <= x <= 231 - 1
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        print('x=', x)
        if( x < -2**31 ):
            print('x < -2**31')
            return False
        if( x >= 2**31 ):
            print('x >= 2**31')
            return False
        if( x < 0 ):
            return False
        # if( (x >= 0) & (x <= 9) ):
        if( x//10 == 0 ):
            return True
        lenX = len(str(x))
        for i in range(lenX-1, lenX//2-1, -1):
            n = x//(10**(lenX-i-1))%10 #from back
            m = x//(10**i) #form forward
            x %= (10**i)
            if m == n:
                continue
            else:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(-2**31-1))
print(sol.isPalindrome(2**31))
print(sol.isPalindrome(0))
print(sol.isPalindrome(9))
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
print(sol.isPalindrome(123454321))
