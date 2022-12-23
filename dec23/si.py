#calculate simple interest si = ptr/100

def main():
    p = int(input("enter principle: "))
    t = int(input("enter time: "))
    r = int(input("enter rate of interest: "))
    print(si(p,t,r))


def si(p,t,r):
    si = (p*t*r)/100
    return si


if __name__ == "__main__":
    main()

