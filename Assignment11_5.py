
idigit = 0
icnt = 0
def countDigit(no):
    global idigit,icnt
    if(no != 0):
        digit = no % 10
        if(digit == 0):
            icnt = icnt + 1
        no = no // 10
        countDigit(no) 
    return icnt        
def main():

    print("enter number")
    no = int(input())

    iret = countDigit(no)

    print("zero count is:",iret)

if __name__ == "__main__":
    main()    
