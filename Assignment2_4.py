def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print("num not prime")
        else:
            print("num is prime")
        
    
