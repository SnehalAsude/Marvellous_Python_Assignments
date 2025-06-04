
def Vowel(ch):

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else :
        return False    

def main():

    print("enter Character")
    ch = input()

    iret = Vowel(ch)

    if(iret == True):
        print("Character is vowel")
    else :
        print("Character is consonant")    


if __name__ == "__main__":
    main()    
