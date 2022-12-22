#  program which accepts the user's first and last name and print them in reverse order

def main():
    name = name_a()
    print((name[0]+" "+name[1]).title())



def name_a():
    n = input("enter you full name: ").split(" ")
    return n[1],n[0]  # returns a tuple with user input as each value in tuple

if __name__ == "__main__":
    main()