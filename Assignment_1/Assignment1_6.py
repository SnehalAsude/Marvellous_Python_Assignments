def Check(number):
    if number > 0 :
        print(" The number is possitive")
    elif number < 0 :
        print("The number is negative")
    else :
        print("zero")

def main():
    print("enter number")
    number = int(input())
    Check(number)
if __name__ == "__main__":
    main()