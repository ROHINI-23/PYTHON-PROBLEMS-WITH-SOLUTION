matrix_value= [[-1,-8,9],[2,-8,6],[4,-4,4]]

value = 0

for x in matrix_value:
    for y in x:
        if y < 0:
            value +=1
print("Total negative numbers in matrix: ",value)






