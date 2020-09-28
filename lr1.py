inp=input("Input Nickname:")
fl=0
file = open("Data/telegram_clear_data.txt", "r")
for line in file:
    l1=line.split('|')
    if l1[6] == inp:
        print("Name: "+l1[2]+" \nFname: "+l1[3]+" \nNumber: "+l1[4])
        fl=1
        break
file.close()
if fl==0:
    print ("Not Found")

#WeB_BackenD
#Ali656500