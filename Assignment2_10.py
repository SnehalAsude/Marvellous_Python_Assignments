
def AdditionDigit(no):
    sum = 0
    while (no != 0):
        digit = no % 10
        sum = sum + digit
        no = no // 10   

    return  sum
    
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = AdditionDigit(no)

    print("Count of digit is :",sum)

if __name__ == "__main__":
    main()