
def ChckPrime(Data):
    if(Data == 2):
        return True

    if( Data % 2 == 0) or (Data % 3 == 0):
        return False
    return True    

def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(ChckPrime,Data))

    print(FData)
if __name__ == "__main__":
    main()