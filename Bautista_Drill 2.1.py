age = int(input("What is your age? "))

license = input("Do you have a fishing license in MN (yes/no)? ").lower() == "yes"

parents = input("Does your parent have a fishing license (yes/no)? ").lower() == "yes"

is_legal = (age <= 15 and parents) or (age >= 16 and license) 

if is_legal:
    print("You are legal to fish in MN.")
else:
    print("You are not legal to fish in MN.")
