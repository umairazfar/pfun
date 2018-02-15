lst=[]
lst2=[]
lst3=[]
lst4=[]
table=0
computer=0
chair=0
space=0
wall=0
computer_string=""
table_string=""
chair_string=""
file=open("Project_PFun.txt","r")
for line in file:
    for ch in line:
        if ch=="w":
            lst.append(ch)
            wall=wall+1
        elif ch=="_":
            lst.append(ch)
            space=space+1
        elif ch=="T":
            lst2.append(ch)
            table=table+1
        elif ch=="D":
            lst3.append(ch)
            computer=computer+1
        elif ch=="h":
            lst4.append(ch)
            chair=chair+1
        else:
            pass
file.close()

text_file = open("Output.txt", "w")
text_file.write("Furniture Positioning: \n")
text_file.close()

print(lst)
print("Spaces:", space)
print("Wall:", wall)
print("Computer:", computer)
print("Table:",table)
print("Chair:",chair)
print(lst2)
print(lst3)
print(lst4)
text_file = open("Output.txt", "a")
text_file.write("Spaces: " +str(space)+ " \n")
text_file.close()
text_file = open("Output.txt", "a")
text_file.write("Chairs: " +str(chair)+ " \n")
text_file.close()
text_file = open("Output.txt", "a")
text_file.write("Computers: " +str(computer)+ " \n")
text_file.close()

file=open("Project_PFun.txt","r")
temp=file.readline()
file.close()
width=len(temp)-1

file=open("Project_PFun.txt","r")
temp=file.readlines()
file.close()
height=len(temp)-3

for x in range(0,len(lst),width):
    print(lst[x:x+width])

if width<5 or height<5:
    text_file = open("Output.txt", "a")
    text_file.write("The room is too small for any furniture. \n")
    text_file.close()
else:
    if computer>0 and height>5:
        for x in range(0,len(lst)):
            if lst[x]=="_" and lst[x-1]=="_" and lst[x+1]=="_" and lst[x+width]=="_" and lst[x-(2*width)]=="_" and lst[x-width]=="_" and table>0:
                lst[x]="T"
                table=table-1
    else:
        for x in range(0,len(lst)):
            if lst[x]=="_" and lst[x-1]=="_" and lst[x+1]=="_" and lst[x+width]=="_" and lst[x-width]=="_" and table>0:
                lst[x]="T"
                table=table-1
        
    if table>0:        
        table_string=(str(table)+" tables are left, there's no more space.")
        text_file = open("Output.txt", "a")
        text_file.write(str(table_string)+"\n")
        text_file.close()
        
    for i in range(0,len(lst)):
        if lst[i]=="_" and (lst[i-1]=="_" or lst[i-1]=="T") and (lst[i+1]=="_" or lst[i+1]=="T") and lst[i+width]=="T" and lst[i-width]=="_" and computer>0:
            lst[i]="D"
            computer=computer-1
            
    if computer>0:
        computer_string=(str(computer)+" computers are left, there's no more space.")
        text_file = open("Output.txt", "a")
        text_file.write(str(computer_string)+"\n")
        text_file.close()
    for x in range(0,len(lst)):
        if lst[x]=="_" and (lst[x-1]=="_" or lst[x-1]=="T") and (lst[x+1]=="_" or lst[x+1]=="T") and lst[x+width]=="_" and (lst[x-width]=="_" or lst[x-width]=="T") and chair>0:
            lst[x]="h"
            chair=chair-1
    if chair>0:
        chair_string=(str(chair)+" chairs are left, there's no more space.")
        text_file = open("Output.txt", "a")
        text_file.write(str(chair_string)+"\n")
        text_file.close()
empty=""
for x in range(0,len(lst)):
    empty=empty+lst[x]

text_file = open("Output.txt", "a")
for i in range(0,len(empty), width):
    empty2=empty[i:i+width]+"\n"
    print("x")
    text_file.write(empty2)
print(empty)
text_file.close()



