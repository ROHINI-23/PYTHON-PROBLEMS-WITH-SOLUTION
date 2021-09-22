"""
first = input()
second = input()
fsplt = first.split(" ")
ssplt = second.split(" ")
l1 = []
l2 = []
for i in fsplt:
    l1.append(int(i))

for i in ssplt:
    l2.append(int(i))

suml1 = 0
suml2 = 0
sum1 = 0
for i in range(len(l1)):
    if l1[i] > l2[i]:
        suml1 = suml1 + 1
    elif l2[i] > l1[i]:
        suml2 = suml2 + 1
    else:
        sum1 = 0
print(suml1, suml2)


Input (stdin)
5 6 7
3 6 10

Your Output (stdout)
1 1

Expected Output
1 1
"""