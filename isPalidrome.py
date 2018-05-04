def isPalidrome(s):
    i = 0
    while i < len(s)/2:
        if s[i] != s[-1-i]:
            return False
        i += 1
    return True


str1 = 'anana'
str2 = 'banana'
str3 = 'dada'
str4 = 'dadad'
str5 = 'ab'
print isPalidrome(str1)
print isPalidrome(str2)
print isPalidrome(str3)
print isPalidrome(str4)
print isPalidrome(str5)
