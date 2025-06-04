
def Fahrenheit(no):
    F = (no * 9/5) + 32
    return F

def main():

    print("enter Number")
    no = int(input())

    iret = Fahrenheit(no)

    print("Tempareture Fahrenheit is:",iret)



if __name__ == "__main__":
    main()    
