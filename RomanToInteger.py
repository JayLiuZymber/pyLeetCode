#!/usr/bin/python3
'''
https://leetcode.com/problems/roman-to-integer/
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        # print('len(s)=', len(s))
        length = len(s)
        if( (length<1) | (length>15) ):
            print('s.length < 1 or s.length > 15')
            return 0
        setS = { x for x in s if x not in "IVXLCDM" }
        # print('setS=', setS)
        if( len(setS) > 0 ):
            print('s contains illegal characters')
            return 0
        
        i = ans = 0
        while i<length:
            j = i+1
            if j >= length:
                j = i
            match s[i]:
                case 'I':
                    if s[j] == 'V':
                        ans += 4
                        i += 1
                    elif s[j] == 'X':
                        ans += 9
                        i += 1
                    else:
                        ans += 1
                case 'V':
                    ans += 5
                case 'X':
                    if s[j] == 'L':
                        ans += 40
                        i += 1
                    elif s[j] == 'C':
                        ans += 90
                        i += 1
                    else:
                        ans += 10
                case 'L':
                    ans += 50
                case 'C':
                    if s[j] == 'D':
                        ans += 400
                        i += 1
                    elif s[j] == 'M':
                        ans += 900
                        i += 1
                    else:
                        ans += 100
                case 'D':
                    ans += 500
                case 'M':
                    ans += 1000
            i+=1
        return ans
    
sol = Solution()
print(sol.romanToInt(''))
print(sol.romanToInt(""))
print(sol.romanToInt("1234567890123456"))
print(sol.romanToInt("IJK"))
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
