##B351
l1 = [1, 5, 5, 3, 2, 6, 2]
##Question5
def function1(l):
    tmp = 0
    for i in range(0,(len(l))):
        for j in range(0,len(l)):
            if l[i] <= l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
                tmp = 0
    print l


##Question 6
def function2(l,num):
    c = 0
    for i in l:
        if i == num:
            c += 1
    return c
        
##Question 7
def function3(n):
    line = [1]
    print "\t" * (n - 1),
    print "%d\n" % line[-1],
    for i in range(n - 1):
        new_line = [1]
        for j in range(i):
            new_line.append(line[j] + line[j + 1])
        new_line.append(1)
        line = new_line
        print "\t" * (n - i - 2),
        for each in line[:-1]:
            print "%d\t\t" % each,
        print "%d\n" % line[-1],
 
