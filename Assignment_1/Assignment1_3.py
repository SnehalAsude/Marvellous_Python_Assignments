def add(no1,no2):
    sum = no1 + no2
    return sum

def main():
   
    no1 = int(input("enter first number"))
    no2 = int(input("enter second number"))
    sum = add(no1,no2)
    print(sum)

     
if __name__ == "__main__":
    main()