no_of_students = int(input())
lst = []
for i in range(no_of_students):
    inp = input()
    lst.append(inp)
l = []
for i in range(len(lst)):
    if lst[i] < "35":
        l.append(lst[i])
    elif lst[i][-1] == "3":
        l.append(str(int(lst[i])+2))
    elif lst[i][-1] == "8":
        l.append(str(int(lst[i])+2))
    else:
        l.append(lst[i])

for i in l:
    print(int(i))