# MY SOLUTION 
def isValidShuffle(s1,s2,res):
    temp_s1,temp_s2 = "",""
    for i in res:
        if i in s1:
            temp_s1+=i 
        elif i in s2:
            temp_s2+=i 
        else:
            return False
    if temp_s1==s1 and temp_s2==s2:
        return True
    return False 

# Given Solution
def isValidShuffle1(s1,s2,res):
    i,j,k=0,0,0
    while k < len(res):
        if i<len(s1) and res[k] == s1[i]:
            i+=1
        elif j<len(s2) and res[k] == s2[j]:
            j+=1
        k+=1
    if i == len(s1) and j == len(s2):
        return True
    return False 

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    res = input() 
    if len(s1)+len(s2) == len(res):
        print(isValidShuffle(s1,s2,res))
        print(isValidShuffle1(s1,s2,res))
    else:
        print("False")

