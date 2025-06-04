
def Palindrome(string):    
    reversed_string = ""

    i = len(string) -1
    while (i >= 0):
        reversed_string = reversed_string + string[i]
        i = i - 1

    # print(reversed_string) 
    i = 0
    while i < len(string):
        if(string[i] != reversed_string[i]):
            return False
            i = i + 1
        return True    


def main():

    print("enter the name")
    string = input()

    iret = Palindrome(string)

    if(iret == True):
        print("number is palidrom")
    else:
        print("number is not palidrom")    

if __name__ == "__main__":
    main()