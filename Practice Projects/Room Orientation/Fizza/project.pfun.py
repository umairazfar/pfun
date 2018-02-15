file=open("project_fizza.txt")
lst=file.readlines()
lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst5=[]
chair=0
comp=0
T=0
#lst2 is furniture
#lst1 is room with walls
for i in lst:
    if  i.startswith("w"):
        lst1.append(i.strip())
    elif i.startswith("h") or i.startswith("D") or i.startswith("T"):
        lst2.append(i.strip())
#Now we count the number of tables,chairs and computers.
for i in lst2:
    if i.startswith("T"):
        for j in i:
            T=i.count(j)
    elif i.startswith("h"):
        for j in i:
            chair=i.count(j)
    elif i.startswith("D"):
        for j in i:
            comp=i.count(j)
#Now we will make lst3 which doesnt have first two and last two lines.
for i in range(len(lst1)):
    if i!=1 and i!=0 and i!=len(lst1)-1 and i!=len(lst1)-2:
        lst3.append(lst1[i])
#lst3 is without the top and bottom walls and also exclude the first lines after top wall and before last wall.
#now we make lst4 which provides the available space in the room after chopping all the walls and places exactly next to the walls
for i in lst3:
    for j in range(len(i)):
        lst4.append(i[2:len(i)-2])
        break
for i in lst4:
    lst5.append(list(i))
#Emty room is avaialable.
#Arranging the furniture.
for i in range(1,len(lst5),2):
    for j in range(len(lst5[i])):
        if lst5[i][j]=="_" and lst5[i-1][j]!="h" and lst5[i-1][j]!="T" and j+1<len(lst5[i]):
            if lst5[i][j+1]=="_" and (lst5[i][j-1]=="_" or lst5[i][j-1]=="T") and chair>0:
                 lst5[i][j]="h"
                 chair=chair-1
        if lst5[i][j]=="h"  and j+2<len(lst5[i]):
            if lst5[i][j+1]=="_" and lst5[i][j+2]!="D" and lst5[i-1][j]!="h" and T>0:
                lst5[i][j+1]="T"
                T=T-1

for i in range(len(lst5)):
    for j in range(len(lst5[i])):
        if lst5[i][j]=="T" and lst5[i-1][j]=="_" and comp>0:
            lst5[i-1][j]="D"
            comp=comp-1
            
#Placing extra tables

for i in range(1,len(lst5)):
    for j in range(len(lst5[i])-1):
        if lst5[i-1][j]!="h" and lst5[i-1][j]!="T" and T>0:
            if lst5[i][j]=="_" and lst5[i][j-1]!="T" and lst5[i][j+1]!="T" and j+1<len(lst5[i]):
                lst5[i][j]="T"
#converting into a string
file1=open("pfun.txt","w")
empty="w_"
c=len(lst5[0])+4
wall=("w"*c+"\n"+"w"+"_"*(c-2)+"w")
file1.write(wall+"\n")
for i in lst5:
    for j in i:
        empty=empty+j
    file1.write(empty+"_w"+"\n")
    empty="w_"
file1.write(wall[::-1])


file1.write("\n"+"Number of Tables left: "+str(T)+"\n")
file1.write("Number of Chairs left: "+str(chair)+"\n")
file1.write("Number of Computers left: "+str(comp))

file1.close()
