#The Distance 
# Given a password string S of lowercase letters (a-z) and digits (0-9), the distance between two characters is the absolute difference of their
# indices. Return the maximum distance between two non-similar (different) characters. Adjacent characters have distance 1. INPUT / OUTPUT 
# input1: string S. Output: maximum distance between two non-similar characters. EXAMPLE Input: abc10 Output: 4 Input: bbbb Output: 0
s=input().strip()
n=len(s)
ans=0
#comparing first character
for i in range(n-1,-1,-1):
    if s[i]!=s[0]:
        ans=max(ans,i)
        break
#comparing last character
for i in range(n):
    if s[i]!=s[n-1]:
        ans=max(ans,n-1-i)
        break
print(ans)