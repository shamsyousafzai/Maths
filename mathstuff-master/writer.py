stuffToWrite = ["bear", "apple", "chicken", "money", "car"]


def main():

    print("Welcome to this testing program for inputting samples. ")
    openFile = open("stuff.txt", "w")

    newList = []
    for eachWord in stuffToWrite:
        newList.append(eachWord)
        openFile.write(eachWord)
        openFile.write("\n")

    # print(openFile) # used to test and see the junk printed out
    # also used to verify that the text was written into the text file
    print(newList)


main()
