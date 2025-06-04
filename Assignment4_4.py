
from FMR import filterX,mapX,reduceX
def CheckEven(Data):
    if(Data % 2 == 0):
        return True

def Square(Data):
    sum = 0
    sum = Data ** 2

    return sum

def Addition(Data,sum):
    sum = sum + Data
    return sum

def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filterX(CheckEven,Data))
    print(FData)

    MData = list(mapX(Square,FData))
    print(MData)

    RData = reduceX(Addition,MData)
    print(RData)

if __name__ == "__main__":
    main()