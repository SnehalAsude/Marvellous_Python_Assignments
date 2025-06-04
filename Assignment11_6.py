
sum = 0    
i = 0
def naturalNumber(no):
    global i, sum
    if no == 0:
        return False
    if(i <= no):
        sum = sum + i
        i = i + 1
        naturalNumber(no)
    return sum    


def main():

    print("enter number")
    no = int(input())

    iret = naturalNumber(no)

    print("Natural number sum is:",iret)

if __name__ == "__main__":
    main()    
