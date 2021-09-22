def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)
    if catA == catB:
        return "Mouse C"
    elif catA > catB:
        return "Cat B"
    else:
        return "Cat A"

n = int(input())
lst = []
for i in range(n):
    l = []
    inp = input()
    splt = inp.split(" ")
    for i in splt:
        l.append(int(i))
    lst.append(l)
for i in lst:
    print(i)
    a = catAndMouse(i[0],i[1],i[2])
    print(a)