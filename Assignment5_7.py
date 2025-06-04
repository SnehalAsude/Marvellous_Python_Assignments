
def Area(length,width):
    Area = length * width
    return Area

def perimeter(length,width):
    perimeter = 2 *(length + width)
    return perimeter

def main():

    print("enter length")
    length = int(input())
    print("enter width")
    width = int(input())

    iret = Area(length,width)

    print("Area of Rectangle  is:",iret)

    iret = perimeter(length,width)
    print("Perimeter of Rectangle  is:",iret)


if __name__ == "__main__":
    main()    
