#BRUTE FORCE : O(n3) NOT ACCEPTABLE
def is_palindrome(string,i,j):
    while i<j:
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True
    
string = input()
max_length,start,end = 0,0,0
for i in range(len(string)):
    for j in range(i,len(string)):
        if is_palindrome(string,i,j):
            if j-i+1 > max_length:
                max_length = j-i+1
                start = i
                end = j+1

print(string[start:end])

# DYNAMIC PROGRAMMING
string = input()
max_length = 0
final_string = ""
DP = [[0 for j in range(len(string))] for i in range(len(string))]
for diff in range(len(string)):
    i,j = 0,i+diff
    for i in range(len(string)-diff):
        j = i+diff
        if i == j:
            DP[i][j] = 1
        elif diff == 1:
            DP[i][j] = 2 if string[i] == string[j] else 0
        else:
            if string[i] == string[j] and DP[i+1][j-1]:
                DP[i][j] = DP[i+1][j-1]+2
        if DP[i][j] and j-i+1 > max_length:
            max_length = j-i+1
            final_string = string[i:j+1]
        
# for i in range(len(string)):
#     for j in range(len(string)):
#         print(DP[i][j],end=" ")
#     print()

print(final_string) 
           
