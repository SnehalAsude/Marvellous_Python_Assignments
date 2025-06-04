
from functools import reduce

def Check(Data):
    Result = []
    if(Data >= 70) and (Data <= 90):
        return True

         
def Increment(Data):
    sum = 0
    sum = Data + 10

    return sum

def Multi(Data,sum):
    sum = sum * Data
    return sum

def filterX(Task,Data):
    Result = []
    for i in range(len(Data)):
        iret = Task(Data[i])
        if iret == True:
            Result.append(Data[i])
    return Result
  
def mapX(Task,Data):

    Result =[]

    for i in range(len(Data)):
        iret = Task(Data[i])
        Result.append(iret)

    return Result

def reduceX(Task,Data):
    result = 1
    for i in Data:
        result = Task(result,i)

    return result        

def main():
    print("enter the size ")
    size = int(input()) 

    Data = list()

    print("enter the element")

    for no in range(size):
        Data.append(int(input()))

    FData = list(filterX(Check,Data))
    print(FData)

    MData = list(mapX(Increment,FData))
    print(MData)

    RData = reduceX(Multi,MData)
    print(RData)


if __name__ == "__main__":
    main()