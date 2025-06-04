
i = 1
def Display(no):
    global i
    if(i <= no):
        print(i)
        i = i + 1
        Display(no)

def main():

    print("enter number")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()    
