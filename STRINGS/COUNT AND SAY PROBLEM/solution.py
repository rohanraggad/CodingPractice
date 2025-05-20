n = eval(input())
s1 = ""
if n == 1:
    print("1")
elif n == 2:
    print("11")
else:
    s = "11"
    # t = "11"
    for i in range(2,n):
        count = 1
        L = []
        for j in range(1,len(s)):
            if s[j]==s[j-1]:
                count+=1
            else:
                L.append(str(count))
                L.append(s[j-1])
                count = 1
        
        L.append(str(count))
        L.append(s[-1])
        s = ''.join(L)
    print(s)
    
# BEST SOLUTION
n = eval(input())
if n == 1:
    print("1")
elif n == 2:
    print("11")
else:
    s = "11"
    for i in range(2,n):
        s+="$"
        t = ""
        c = 1
        for j in range(1,len(s)):
            if s[j] == s[j-1]:
                c+=1
            elif s[j] != s[j-1]:
                t += str(c)+str(s[j-1])
                c = 1
        s = t
    print(s)    


