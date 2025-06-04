
i = 0
j = 0
def pattern(no):
    global i,j
    if(i<no):
        
        if(j<=i):
            print(" * ",end=" ")
            j = j + 1
            pattern(no)
        else:    
            print('\n')    
            i = i + 1
            j = 0
            pattern(no)    

def main():

    print("enter number")
    no = int(input())

    pattern(no)

if __name__ == "__main__":
    main()    
