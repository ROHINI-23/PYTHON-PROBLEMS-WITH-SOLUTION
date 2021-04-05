"""Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive)."""

#Answer

low = int(input("low number :"))
high = int(input("high number : "))
count = 0
for x in range(low, high):
    if x % 2 != 0:
        print(x)
        count = count + 1
print("Total number of odd numbers between low and high", count)


