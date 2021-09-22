n = int(input())
l = input()
lsplt = l.split(" ")
lst = []
for i in lsplt:
    lst.append(int(i))

for i in range(0,len(lst)-1):
    if lst[i]> lst[i+1]:
        lst[i],lst[i+1] = lst[i+1],lst[i]

high = lst[-1]
print(lst.count(high))

"""
Input (stdin)

Download
4
3 2 1 3
Your Output (stdout)
2
Expected Output

Download
2
"""