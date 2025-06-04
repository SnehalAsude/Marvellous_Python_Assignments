
import multiprocessing
import time

def Factorial(Data):
    sum = 1
    for i in range(1,Data+1):
        sum = sum * i
    return sum    

def main():

    print("enter size")
    size = int(input())

    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    result = []
    p1 = multiprocessing.Pool()
    result = p1.map(Factorial,Data)

    print(result)

    print("main thread end")

if __name__ == "__main__":
    main()    
