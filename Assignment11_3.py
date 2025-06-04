
sum = 0
i = 1
def SumofDigit(no):
    global i,sum
    if(i<=no):
        sum = sum + i
        i = i + 1
        SumofDigit(no)
    return sum        

def main():

    print("enter number")
    no = int(input())

    iret = SumofDigit(no)

    print("Sum of Digit is:",iret)

if __name__ == "__main__":
    main()    
