#function 
def balance(arr) :

    if not arr :
        return False
#main  lists to use
    stack = []
    match = ['[','{','(']
    opp = [']','}',')']
#for loop to determine the char in string and remove its oppiste
    for ch in arr :
        if ch in match :
            stack.append(ch)
        elif ch in opp:
            stack.pop()

    if not stack :
        return True
    else :
        return False
            





lists = []
#enter number of strings

number = int(input("Enter number of strings = "))

#reading the strings

for x in range(number) :
    line = input("Enter a string = ").strip()
    lists.append(line)

#check the string
for x in lists :
    if balance(x) :
        print("The string is balanced")
    else :
        print("The string is not balanced")

