
def EvenNumber(Data):
    if (Data % 2 == 0):
        return Data


def main():
    print("enter the size")
    size = int(input())
    Data = []
    print("enter the element")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(EvenNumber,Data))

    print(FData)
if __name__ == "__main__":
    main()