import json 

def parser():
    f = open("names.txt", "r")
    new = open("new.txt", "w")

    a = f.read()
    a = a.split(" ")
    b = a[0].split("\n")


    length = len(b)
    i = 0

    new.write("{ \n")
    new.write("    ")
    new.write('"array": [\n')
    while i < length:
        new.write('        "')
        new.write(b[i])
        if i != (length - 1):
            new.write('",\n')
        else:
            new.write('"\n')
        i += 1
    
    new.write("    ]\n")
    new.write("}")

parser()