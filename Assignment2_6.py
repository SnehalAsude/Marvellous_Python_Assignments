def print_pattern(num):
    for i in range(num, 0, -1):
        for j in range(num):
            if j<i:
                print("*", end = " ")
        print('\n')  
num = int(input("Enter a number:"))
print_pattern(num)