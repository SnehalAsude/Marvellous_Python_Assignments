
from FMR import filterX,reduceX,mapX
def PrimeChck(Data):
    if(Data % 2 == 0):
        return False
    return True     

def Multiply(Data):
    sum = 0
    sum = Data * 2
    return sum

def GreaterNumber(Data,sum):
    if(sum < Data):
        sum = Data
    
    return sum

def main():

    print("enter size")
    size = int(input())

    Data = []

    print("enter the element")
    for i in range(size):
        Data.append(int(input()))


    FData = list(filterX(PrimeChck,Data))
    print(FData)    
    MData = list(mapX(Multiply,FData))
    print(MData)
    RData = reduceX(GreaterNumber,MData)
    print(RData)

if __name__ == "__main__":
    main()    
