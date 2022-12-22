def main():
    num = int(input("enter the radius: "))
    area = area_circle(num)
    print(area)


# circle area calculate function
def area_circle(r):
    # formula is radius square times pi(3.14)
    area =  (3.14 * r * r)
    return area

if __name__ == "__main__":
    main()
