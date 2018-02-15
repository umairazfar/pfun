#reads file
room = open("project2.txt","r")
empty=""
file=room.readlines()
for i in file:
    empty+=i
#print(empty)

#converts string to list
empty1=empty.split("\n")
print(empty1)



#removes empty lines
ind=[]
for i in range(len(empty1)):
    if empty1[i] == "":
        ind.append(i)
print("index=",ind)
for x in range(len(ind)):
    del empty1[ind[x]-x]
    index1=ind[x]-x
print("empty1=",empty1)

#makes new list with furniture 
furniture=[]
for i in range(index1,len(empty1)):
    furniture.append(empty1[i])
print("furniture=",furniture)
print(empty1)

#new list without furniture
del empty1[index1:]
print("empty1=",empty1)

#checks the room size
if len(empty1)<=4:
    print("Furniture can not be added.")
    quit()

#removes horizontal walls
lst1=[]
for y in range(1,len(empty1)):
    if empty1[y]==empty1[0]:
        lst1.append(y)
print("ls1=",lst1)

walls=[]
walls.append(empty1[0])
for i in lst1:
    #i=int(i)
    walls.append(empty1[i])
    del empty1[i]
del empty1[0]

print("walls=",walls)
print("empty1=",empty1)

#removes vertical walls and spaces next to walls
walls.append(empty1[0])
walls.append(empty1[0])
del empty1[0:2]

print("walls=",walls)


spaces=[]
for x in empty1:
    spaces.append(x[2:len(x)-2])
print("spaces=",spaces)


#makes list of furniture
h=[]
T=[]
D=[]
for x in furniture:
    if x[0]=="h":
        for y in range(len(x)):
            h.append("h")
    if x[0]=="T":
        for y in range(len(x)):
            T.append("T")
    if x[0]=="D":
        for y in range(len(x)):
            D.append("D")

print(h,T,D)

#arranging furniture
'''
new=[]
for x in spaces:
    new1=[]
    for y in range(len(x)):
        new1.append(x[y])
    new.append(new1)
print(new)
'''

limit=len(h)
limit1=0
string=''
for x in spaces:
    if limit>=2:
        y=((len(x)-2)*"_")
        string=string+"h"+str(y)+"h"+"\n"
        limit-=2
        limit1+=2
        continue
    if limit==1:
        y=((len(x)-1)*"_")
        string=string+"h"+str(y)+"\n"
        limit-=1
        limit1+=1
        continue
    if limit==0:
        string=string+x+"\n"
print(string)

remaining=len(h)-limit1
print(remaining)


new=[]
new1=[]
new=string.split("\n")
print(new)
del new[len(new)-1]
print(new)
new2=[]
for x in new:
    new1=[]
    for y in range(len(x)):
        new1.append(x[y])
    new2.append(new1)
print(new2)
tables=len(T)
tables1=0

for i in new2:
    for y in range(len(i)):
        if tables>=0:
            if i[y]=='h':
                i[y+1]="T"
                tables-=1
                tables1+=1
                break


tables2=len(T)-tables1
print(new2)
list1=[]
for i in new2:
    for y in i:
        list1.append(y)
print(list1)

temp1=''
temp1+=walls[0]+"\n"+walls[2]+"\n"
for i in new2:
    temp1+="w_"
    for y in i:
        temp1+=y
    temp1+="_w"+"\n"    
temp1+=walls[3]+"\n"+walls[1]

        
print(temp1)

room.close()

#creating new file

files = open('New room.txt','w')

files.write(temp1)
files.write('\n')
files.write('\n')
files.write("there are "+str(remaining)+" chairs left.")
files.write('\n')
files.write("there are "+str(tables2)+" tables left.")


files.close()

'''


            
  
remaining=len(h)-limit1
print(remaining)


'''
            

