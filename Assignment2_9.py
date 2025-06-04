
def CountDigit(no):
    icnt = 0
    while (no != 0):
        digit = no % 10
        icnt = icnt + 1
        no = no // 10  

    return  icnt
 
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = CountDigit(no)

    print("Count of digit is :",sum)

if __name__ == "__main__":
    main()