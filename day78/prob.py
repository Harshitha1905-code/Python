class Sloution:
    def bitwiseComplement(self,n,int)-> int:
        if n ==0:
            return 1
        b = bin(n)[2:]
        comp =''
        for bit in b:
            if bit == '0':
                comp +='1'
            else:
                comp +='0'
        return int(comp,2)
    

 #reverse a string
    def reverseString(self,s):
        left,right = 0,len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1
        return s   