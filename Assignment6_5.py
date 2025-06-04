
def ChckPrime(no):
    if(no == 2):
        return True

    if(no % 2 == 0):
        return False
    else :
        return True 

def main():
    print("Enter the number")
    no = int(input())
    iret = ChckPrime(no)
    
    if iret == True:
        print("Number is Prime")
    else:
        print("Number is not Prime")
    
if __name__ == "__main__":
    main()    
