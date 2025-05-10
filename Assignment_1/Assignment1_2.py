def ChkNum(number):
    
    if number % 2 == 0:
        print("number is even number")
    else :
        print("number is odd number")
    

def main():
    print("enter the number")
    value = int(input())

    ChkNum(value)
    ChkNum() 


if __name__=="__main__":
    main()