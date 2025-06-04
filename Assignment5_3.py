
def Eligiblity(age):

    if age >= 18:
        return True
    else :
        return False    

def main():

    print("enter age")
    age = int(input())

    iret = Eligiblity(age)

    if(iret == True):
        print("Eligible to vote")
    else :
        print(" not Eligible to vote")  


if __name__ == "__main__":
    main()    
