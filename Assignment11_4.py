
sum = 1
i = 0
def Power(no):
    global i,sum
    if(i<=no):
        sum = sum * no
        i = i + 1
        Power(no)
    return sum        

def main():

    print("enter number")
    no = int(input())

    iret = Power(no)

    print("Power Digit is:",iret)

if __name__ == "__main__":
    main()    
