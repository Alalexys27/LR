fl=0
print("1 - begin\n2 - end\n3 - time interval\n4 - login\n5 - mac ab\n6 - ULSK1\n7 - BRAS ip\n8 - start count\n9 - alive count\n10 - stop count\n11 - incoming\n12 - outcoming")
inp=input("Введите соответствующую цифру: ")
try:
    inp=int(inp)
    if 1<=inp<=12:
        inp2=input("Введите значение: ")
        i=1
        while i<=7:
            f = "les1/res_"+str(i)+".csv"
            file = open(f, "r")
            for line in file:
                l1=line.split(',')
                if l1[inp-1] == inp2:
                    print("____________________________\nFile name: "+f+"\n____________________________\n")
                    print(" begin: "+l1[0]+"\n end: "+l1[1]+"\n time interval: "+l1[2]+"\n login: "+l1[3]+"\n mac ab: "+l1[4]+"\n ULSK1: "+l1[5]+"\n BRAS ip: "+l1[6]+"\n start count: "+l1[7]+"\n alive count: "+l1[8]+"\n stop count: "+l1[9]+"\n incoming: "+l1[10]+"\n outcoming: "+l1[11]+"\n error_count: "+l1[12])
                    fl=1
            file.close()
            if fl==0:
                print ("Not Found in "+f)
            i=i+1
            fl=0
    else:
        print("Выбрано неверное значение!")
except:
    print("Выбрано неверное значение!")