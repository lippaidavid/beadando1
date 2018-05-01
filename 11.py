def Palindrome (n):
    s = str(n)
    return s == s[::-1]

def legnagyobbPalindrome(a, b):
    legnagyobb = 0
    for i in range(b, a, -1):
        for j in range(b, a, -1):
            if Palindrome(i*j):
                if i*j > legnagyobb:
                    legnagyobb = i*j
    return legnagyobb

print(legnagyobbPalindrome(100,999)) #993*913=906609