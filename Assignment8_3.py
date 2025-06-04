
import threading

def AddEvenNumber(Data):
    sum = 0
    for i in Data:
        if(i % 2 == 0):
            sum = sum + i
    print("Add even factor is :",sum)     

def AddOddNumber(Data):
    sum = 0
    for i in Data:
        if(i % 2 != 0):
            sum = sum + i
    print("Add Odd factor is :",sum) 

def main():

    print("enter size")
    size = int(input())

    Data = []

    print("enter the element")

    for i in range(size):
        Data.append(int(input()))

    T1 = threading.Thread(target=AddEvenNumber,args=(Data,))
    T2 = threading.Thread(target=AddOddNumber,args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("main thread end")

if __name__ == "__main__":
    main()    
