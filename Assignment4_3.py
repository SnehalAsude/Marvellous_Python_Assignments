from functools import reduce

def Check(Data):
    Result = []
    if(Data >= 70) and (Data <= 90):
        Result.append(Data)

    return Result        
    
def Increment(Data):
    sum = 0
    sum = Data + 10

    return sum

def Multi(Data,sum):
    sum = sum * Data
    return sum
    
def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filter(Check,Data))
    print(FData)

    MData = list(map(Increment,FData))
    print(MData)

    RData = reduce(Multi,MData)
    print(RData)

if __name__ == "__main__":
    main()