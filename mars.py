"""A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, s ,
 determine how many letters of the SOS message have been changed by radiation. Given input s = 'SOSSPSSQSSOR' .
"""

#Answer

s = 'SOSSPSSQSSOR'
a1 = s[0:3]
a2 = s[3:6]
a3 = s[6:9]
a4 = s[9:12]
print(a1, a2, a3, a4)

total = int(len(s)/3)
print(total)

value = 0
if a1 == 'SOS' or a2 == 'SOS' or a3 == 'SOS' or a4 == 'SOS' :
    value = value + 1
print("Number of Expected signal", value)
print("Total Number of Difference", total - value)

