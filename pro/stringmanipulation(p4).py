# This is a program to find the word shuffle using string manipulation.

origi = "elven plus two"
first = origi[:6]
second = origi[6:12]
third = origi[12:]

fir_2 = first[:2]
fir_3 = first[2]
fir_45 = first[3:5]
fir_6 = first[-1]

thir_2 = third[:2]
thir_3 = third[-1]

origi = fir_2 + fir_3 + fir_45 + fir_6 + second + thir_2 + thir_3
modified = thir_2 + fir_2 + fir_45 + second + thir_3 + fir_6 + fir_3

print("This is the Original strirng:  ",origi)
print("This is the Modified string: ",modified)