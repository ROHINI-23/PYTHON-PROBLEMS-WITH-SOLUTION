n = int(input())
lst =[]
for i in range(n):
    l = []
    inp = input()
    inpsplt = inp.split(" ")
    for i in inpsplt:
        l.append(int(i))
    lst.append(l)

d1 = []
d2 = []
for i in range(0,n):
    d1.append(lst[i][i])
print(d1)

for i in range(0,n):
    d2.append(lst[i][(n-1)-i])
print(d2)

s1 = sum(d1)
s2 = sum(d2)
mod = abs(s1-s2)
print(mod)
"""
Input (stdin)

Download
3
11 2 4
4 5 6
10 8 -12
Your Output (stdout)
15
Expected Output

Download
15
"""
