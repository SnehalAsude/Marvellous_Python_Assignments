def addition():
    iN0_1 = 10
    iNo_2 = 20

    print("Addition : ",iNo_1+iNo_2)

def substraction():
    iNo_1 = 20
    iNo_2 = 30

    print("Substraction : ",iNo_2-iNo_1)

def Multiplication():
    iNo_1 = 10
    iNo_2 = 20

    print("Mutiplication : ",iNo_1*iNo_2)



def main():

    print("pls enter what you want : ")
    Count = int(input())

    if(Count == 1):
        addition()
    elif(Count == 2):
        substraction()
    elif(Count == 3):
        Multiplication()        


if __name__ == "__main__":
    main()