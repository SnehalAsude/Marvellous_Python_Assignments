
import multiprocessing
import threading
import time

def Display(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print(sum)    

def main():

    print("enter number")
    no = int(input())

    start_time = time.time()
    Display(no)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for normal function",execution_time)


    start_time = time.time()
    T1 = threading.Thread(target=Display,args=(no,))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for Thread function",execution_time)


    start_time = time.time()
    P1= multiprocessing.Process(target=Display,args=(no,))
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time for Multiprocessing function",execution_time)


    print("main thread end")

if __name__ == "__main__":
    main()    
