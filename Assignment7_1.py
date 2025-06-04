
square = lambda A: A ** 2

cube = lambda A: A ** 3


def main():
    print("enter the number")
    no = int(input())

    value = square(no)

    print("Square of Number is:",value)
    
    value = cube(no)

    print("cube of Number is:",value)

if __name__ == "__main__":
    main()