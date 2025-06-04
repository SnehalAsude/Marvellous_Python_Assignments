
def main():
    print("Loop Starts")
    sum = 0
    i= 1
    while (i <= 100):
        if(i % 2 == 0):
            sum = sum + i
        i = i + 1
    print("Addition of all even number is :",sum)    

if __name__ == "__main__":
    main()    
