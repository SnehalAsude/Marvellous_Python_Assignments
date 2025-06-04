
def pattern(no):

    for i in range(no):
        for j in range(no):
            if(j<=i):
                print(" * ",end ="")
        print("\n")

def main():
    print("Enter the number")
    no = int(input())
    pattern(no)
    
if __name__ == "__main__":
    main()    
