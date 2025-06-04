
sum = 1
i = 1
def factorial(no):
    global i,sum
    if(i<=no):
        sum = sum * i
        i = i + 1
        factorial(no)
    return sum        

def main():

    print("enter number")
    no = int(input())

    iret = factorial(no)

    print("factorial is:",iret)

if __name__ == "__main__":
    main()    
