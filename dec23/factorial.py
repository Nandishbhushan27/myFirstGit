# factorial 5!=5*4*3*2*1
def main():
    num = int(input("enter the number: "))
    print(fact(num))

def fact(num):
    fac = 1
    while(num>1):
        fac= fac*num
        num = num-1
    return fac

if __name__ == "__main__":
    main()


