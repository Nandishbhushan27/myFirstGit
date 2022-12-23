# reverse name without string slicing or builtin fns

name = input("enter name: ")
rev = ''

for i in range(len(name)):
    s = name[len(name)-(i+1)]
    rev = rev + s

print(rev)


