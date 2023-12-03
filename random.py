import random
Cnumber=random.randrange(1,101)
userinput=int(input("Enter your number:--"))
print("Random Number is --", Cnumber)
if userinput>Cnumber:

    print("Your guess number is High",userinput)
elif Cnumber>userinput:
    print("Your guess number is Low", userinput)
else:
    print("Your guess number is Equel", userinput)

