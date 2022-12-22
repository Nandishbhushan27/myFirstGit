# Calculate the multiplication and sum of two numbers
#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def main():
    n = int(input("first number: "))
    m = int(input("second number: "))
    if mul(n,m) <= 1000:
        print(mul(n,m))
    else:
        print(sum(n,m))
        

def sum(n,m):
    return(n+m)

def mul(n,m):
    return (n*m)

if __name__ == "__main__":
    main()