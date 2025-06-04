
Multi = lambda A , B: A * B

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter second number")
    no2 = int(input())


    if no1 == 0 and no2 == 0:
        print("Invalid Input ")
        return

    sum = Multi(no1,no2)

    print("Multiplication of digit is :",sum)

if __name__ == "__main__":
    main()