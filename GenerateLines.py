import re

print("Welcome to code line generator.")
print("This is a tool for generating a large number of identical lines of code, using multiple variables.")
print("to start, please enter a string format. Use an asterisk to note where you'd like your variable input. You may use up to 3 asterisks.")
print("Example: ")
print(" -> public string *; <- ")
print("When the operation is completed, you can copy the content by highlighting and pressing Ctrl + Shift + C.")
formatConfirmed = False

#collect formatted string
while formatConfirmed == False:
    formatString = input("Enter format string...")
    print()
    formatStringConfirm = input("enter y to confirm or n to try again.")
    if formatStringConfirm == "y" or "Y":
        if formatString.__contains__("*"):
            formatStringList = formatString.split("*")
            numberOfVariableSpots = len(formatStringList) - 1
            if numberOfVariableSpots < 4 and numberOfVariableSpots > 0:
                formatConfirmed = True
            else:
                print("the number of variables must be between 1 and 3. Please try again.")
        else:
            print("that string didn't contain an asterisk ( * ) delimiter. Please try again.")

if numberOfVariableSpots > 1:
    print("Please enter the list of variables you would like inserted into the formatted string. If you have more than one list of variables, then the items of the first list will be inserted in place of the first asterisk, the second list will be for the second asterisk, and so on. Note that multiple lists must have the same number of variables, and the number of lists must match the number of asterisks. Enter the first list, with each value separated by either a comma or a newline.")
else:
    print("Please enter the list of variables you would like inserted into the formatted string. Then the items of the list will be inserted in place of the asterisk. Enter the list, with each value separated by a comma, or a comma and a space.")

#collect variables
#[v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v] will split by comma with optional trailing spaces ' ,\s* ', or by any space/tab/etc ' \s+ ' , and v.strip() for v in ... if v will remove any extra whitespace or empty values
listsOfVariables = {}
numberOfVariables = 0
if numberOfVariableSpots == 1:
    listOfVariables = input("Enter variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list1'] = splitListOfVariables
    locals().update(listsOfVariables)
elif numberOfVariableSpots == 2:
    listOfVariables = input("Enter variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list1'] = splitListOfVariables
    locals().update(listsOfVariables)
    listOfVariables = input("Enter next set of variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list2'] = splitListOfVariables
    locals().update(listsOfVariables)
elif numberOfVariableSpots == 3:
    listOfVariables = input("Enter variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list1'] = splitListOfVariables
    locals().update(listsOfVariables)
    listOfVariables = input("Enter next set of variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list2'] = splitListOfVariables
    locals().update(listsOfVariables)
    listOfVariables = input("Enter next set of variables here...")
    splitListOfVariables = [v.strip() for v in re.split(r',\s*|\s+',listOfVariables) if v]
    numberOfVariables = len(splitListOfVariables)
    listsOfVariables['list3'] = splitListOfVariables
    locals().update(listsOfVariables)
else:
    print("Zero or four-plus variables.")

#create list of strings
completedStrings = []
if numberOfVariableSpots == 1:
    for a in range(numberOfVariables):
        newString = formatStringList[0] + listsOfVariables["list1"][a] + formatStringList[1]
        completedStrings.append(newString)
elif numberOfVariableSpots == 2:
    for a in range(numberOfVariables):
        newString = formatStringList[0] + listsOfVariables["list1"][a] + formatStringList[1] + listsOfVariables["list2"][a] + formatStringList[2]
        completedStrings.append(newString)
elif numberOfVariableSpots == 3:
    for a in range(numberOfVariables):
        newString = formatStringList[0] + listsOfVariables["list1"][a] + formatStringList[1] + listsOfVariables["list2"][a] + formatStringList[2] + listsOfVariables["list3"][a] + formatStringList[3]
        completedStrings.append(newString)

for completedString in completedStrings:
    print(completedString)

close = input("Press any key to close...")