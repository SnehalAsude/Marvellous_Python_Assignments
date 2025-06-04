
Power = lambda A: A ** 2
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    sum = Power(no)

    print("Power of Number  is :",sum)

if __name__ == "__main__":
    main()