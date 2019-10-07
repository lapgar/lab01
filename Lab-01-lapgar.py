# Lindsay Apgar
# Lab-01
# main

# variables
unlucky = 13             # integer
pi = 3.14                # float
iceCream = "strawberry"  # string (favorite ice cream flavor)
decimal = "5.6"          # string with decimal

# conversion
print(float(unlucky))    # convert unlucky to a float
print(int(pi))           # convert pi to an integer
print(str(pi))           # convert pi to a string
print(float(decimal))    # convert decimal to a float

# input
myInteger1 = int(input("Please enter a whole number"))
myInteger2 = int(input("Please enter another whole number"))

myFloat1 = float(input("Please enter a number with a decimal point"))
myFloat2 = float(input("What is pi to two decimal points?"))

# arithmetic
print(myFloat1 + myFloat2)         # add
print(myFloat1 - myFloat2)         # subtract
print(myFloat1 * myFloat2)         # multiply
print(myFloat1 / myFloat2)         # divide
print(myFloat1 ** myFloat2)        # raise to the power of
print(myInteger1 % myInteger2)     # remainder
print(myInteger1//myInteger2)      # integer division?

myInteger1 += myInteger2           # myInteger1 = myInteger1 + myInteger2
myFloat1 *= myFloat2
print(myInteger1)
print(myFloat1)
# print(myFloat1 *= myFloat2), doesn't work because you can't print an expression
# reminder: // is integer division, % calculates remainder

# working with strings
favCereal = input("What is your favorite kind of cereal?")
print("I like " + favCereal + " too!")
print(favCereal * 6)               # use the * operation to repeat favCereal 6 times

# comparison operations --- I do not think that I did this correctly
comp1 = myInteger1 - myInteger2
if comp1 > 0:
    myBool1 = True
    print("myInteger1 is greater than myInteger2")
else:
    myBool1 = False
    print("myInteger2 is greater than myInteger1")

if myFloat1 == myFloat2:
    myBool2 = True
    print(myBool2)
else:
    myBool2 = False
    print(myBool2)

# If...
value = int(input("Please enter a number between 1 and 12"))
if 3 <= value <= 5:                # between 3 and 5
    print("Spring")
elif 6 <= value <= 8:              # between 6 and 8
    print("Summer")
elif 9 <= value <= 11:             # between 9 and 11
    print("Fall")
elif value in [1, 2, 12]:          # if they put 1, 2, or 12 --- Initially tried to say elif value == 1 or 2 or 12, led to numbers outside of the 1 to 12 range also getting the output 'winter'
    print("Winter")
else:                              # if it is not between 1 and 12 -- also could do elif value != 1 <= value <= 12
    print("Wrong number!")

# While...

countdown = int(input("Please input a positive integer between 1 and 10: "))  # countdown from whatever number is input
while 0 <= countdown <= 10:
    print(countdown)
    countdown -= 1
