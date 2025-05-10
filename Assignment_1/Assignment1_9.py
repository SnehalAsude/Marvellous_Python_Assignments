def even(no1):
    i = 1
    while(i<=no1*2):
        if i % 2 == 0:
            print(i)    
        i = i + 1
    
def main():
    print("enter your number")
    no1 = int(input())
    even(no1)


if __name__=="__main__":
    main()