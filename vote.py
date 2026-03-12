age = int(input("enter your age"))
citizen = input("are you indian ? y/n").lower()
if age>=18:
    if citizen=="y":
        print("eligible to vote")
    else :
        print("you must be citizen")
else:
        print("you are not over 18")

        
