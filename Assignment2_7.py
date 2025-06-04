
def pattern(no):
    for i in range(no):
        var = 1
        for j in range(no):
            print(var,end=" ")
            var = var + 1
        print("\n")    

    
def main():
    print("Enter the number")
    no = int(input())

    if no == 0:
        print("Invalid Input ")
        return

    pattern(no)
if __name__ == "__main__":
    main()