x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter a third integer: "))

maxNum = x
if y > maxNum:
    maxNum = y
if z > maxNum:
    maxNum = z


if maxNum % 2 != 0:
    print(maxNum, "is the largest odd number.")
else:
    print("None of the numbers are odd.")
