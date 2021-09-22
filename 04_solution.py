n = int(input())
inp = input()
inpsplt = inp.split(" ")
lst = []
for i in inpsplt:
    lst.append(int(i))
positive = 0
negative = 0
zero = 0

for i in range(n):
    if lst[i] > 0:
        positive = positive + 1
    elif lst[i] < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print(positive/n)
print(negative/n)
print(zero/n)


"""
Input (stdin)

Download
6
-4 3 -9 0 4 1
Your Output (stdout)
0.5
0.3333333333333333
0.16666666666666666
Expected Output

Download
0.500000
0.333333
0.166667
"""