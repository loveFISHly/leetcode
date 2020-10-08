"""

Runtime: 32 ms, faster than 99.56% of Python3 online submissions for Integer to Roman.
Memory Usage: 14 MB, less than 27.19% of Python3 online submissions for Integer to Roman.

"""

def intToRoman(self, num: int) -> str:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
