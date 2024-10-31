for a in range(1, int(input())+1):
    b = a * a
    c = a * b
    print ("""{} {} {}\n{} {} {}""".format(a,b,c,a,b+1,c+1))