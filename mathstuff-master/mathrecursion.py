# function 1
# Take 1 away from the number, function done to updated count number another time
# until number is 0
def rprint(number):
    if number > 0:
        rprint(number-1)  # Does Another recursion
        print(number)  # Prints the number for that iteration
    return number  # Returns the last number when value of number is 0


# function 2
# Two arguments accepted
# Product of the two int arguments where first argument is added to itself the number of times of the second argument
def rmult(number, y):
    if y > 1:
        number += rmult(number, y-1)
    return number  # Returns the sum of value number after iteration when y == 1


# function 3
# Prints a series of asterisks for each iteration
# Counts down from the set value of n
def rlines(n):
    if n != 0:
        # Returns the amount of asterisks (plus 1) on a new line
        print('*' * rlines(n-1))  # Multiplies the string asterisk by the number of times iteration n in recursion
        return n+1
    else:
        return 1  # returns a new line of one asterisk when n == 0


# function 4
def rMultList(wholelist):
    if len(wholelist) == 1:
        return wholelist[0]  # Only if list is length 1 the product is just that one number in the list
    else:
        # Slice through list of numbers from position 1 to last number
        # Multiply the first number with all other numbers in the list
        return wholelist[0] * rMultList(wholelist[1:])


# function 5
def rLargestList(entireList):
    if len(entireList) == 1:
        return entireList[0]  # Only if there is one number in the list return that number
    else:
        x = rLargestList(entireList[1:])  # Slice through and inspect each number
        if x > entireList[0]:  # If next number is greater than the other
            return x
        else:
            return entireList[0]  # Return that number if no other numbers are greater


# function 6
def rSum(number):
    if number == 1:
        return 1  # Adds or returns 1
    else:
        return number + rSum(number-1)  # adds onto and updates the sum of the number value


# function 7
def rPower(base, power):
    if power == 0:  # base number to 0th power is always 1 where the base number is not 0
        return 1
    else:
        # taking the power of a number is multiplying the base by the base^(power - 1)
        return base * rPower(base, power - 1)


def main():
    x = 4  # Initialized values
    y = 7
    rprint(x)  # for function 1
    print()
    print(rmult(x, y), "\n")  # for function 2
    rlines(y)  # for function 3
    print()

    listItems = [1,2,5,6,8,69,10,42]  # List used for functions in the multiplication and largest items list
    print(rMultList(listItems), '\n')  # for function 4
    print(rLargestList(listItems), '\n')  # for function 5

    # Number used is 50
    print(rSum(50), '\n')  # for function 6

    # Base number is 100, power is 2
    print(rPower(100, 2))  # for function 7


main()
