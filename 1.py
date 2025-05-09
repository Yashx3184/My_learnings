import pdb
pdb.set_trace()
# This is a simple program to find the number of lines in a file
Number_of_lines = int(input("Enter the number of lines of X: "))

for row_number in range(lines):
    for column_number in range(lines):
        if row_number == column_number or column_number+1 == lines - row_number:
            print("*", end="")
        else:
            print(" ", end="")
    print()
