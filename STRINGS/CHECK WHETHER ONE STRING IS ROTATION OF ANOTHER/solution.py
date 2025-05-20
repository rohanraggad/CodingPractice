# NAIVE SOLUTION
s1 = "ABACD"
s2 = "CDABA"
if(len(s1)!=len(s2)):
    print("NOT POSSIBLE")
else:
    if(s1 == s2):
        print("YES")
    else:    
        new_string = ''.join(list(s1))
        for i in range(len(s1)-1):
            L = list(new_string)
            first = L.pop(0)
            L.append(first)
            new_string = ''.join(L)
            if(new_string == s2):
                print("YES")
                break
        else:
            print("NO")

# BEST SOLUTION
s1 = "ABACD"
s2 = "CDABA"
if len(s1) != len(s2):
    print("NOT POSSIBLE")
else:
    if s1==s2:
        print("YES")
    else:
        s1+=s1 
        if s2 in s1:
            print("YES")
        else:
            print("NO")
