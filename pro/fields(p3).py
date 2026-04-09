#This program is of Extracting fields from a roll number

roll_no = input("Enter your roll number: ")
branch = roll_no[0:2]
year = int(roll_no[2:4])
degree = roll_no[4]
position = roll_no[5:8]

print(branch,"20%02d" %year,degree,position,sep='\n')