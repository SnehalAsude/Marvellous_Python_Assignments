
def ChckEvenOdd(no):
    if no % 2 == 0:
        return True
    else :
        return False    

def main():

    print("enter Number")
    no = int(input())

    iret = ChckEvenOdd(no)
    if iret == True:
        print("Number is even Number")
    else :
        print("Number is Odd Number")


if __name__ == "__main__":
    main()    
