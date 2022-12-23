# check if prime or not

def main():
    num = int(input("enter the number: "))
    prime(num)


def prime(n):
    flag = False
    for i in range(2,n):
        if n%i == 0:
            flag = True
            break
        
    if flag:
        print(n, "is not a prime number")
    else:
      print(n, "is a prime number")

if __name__ == "__main__":
    main()
