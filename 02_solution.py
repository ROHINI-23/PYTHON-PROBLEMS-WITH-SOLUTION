n = int(input())
inp = input()
inpsplt = inp.split(" ")
lst = []
for i in inpsplt:
    lst.append(int(i))

sum1 = 0
for i in lst:
    sum1 = sum1 + i
print(sum1)


"""
Input (stdin)
5
1000000001 1000000002 1000000003 1000000004 1000000005

Your Output (stdout)
5000000015

Expected Output
5000000015
"""