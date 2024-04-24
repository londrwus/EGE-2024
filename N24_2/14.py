f = open('N24_2\\14.txt').read()

def isPalindrome(s):
    return s == s[::-1]

cnt = 0
for i in range(len(f) - 4):
    if isPalindrome(f[i] + f[i+1] + f[i+2] + f[i+3] + f[i+4]):
        cnt += 1

print(cnt)