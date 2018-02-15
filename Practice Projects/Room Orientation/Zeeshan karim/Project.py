#Reading and extracting the data from a file in a list
file=open("work.txt",'r')
x=file.readlines()
a=[]  #List of the elements of the room
b=[]  #List of the furniture to be placed

for i in range(len(x)):
    if x[i][0]=="w":
        a+=[x[i].strip()]
    elif x[i][0]=="\n":
        continue
    else:
        b+=[x[i].strip()]

y=[list(i[2:-3]) for i in a[2:-2]] #Available spaces in which the furniture is to be placed


c=''
for l in b:
    c+=l
h=0 #Number of chairs
T=0 #Number of Tables
D=0 #Number of Desktops

for m in c:
    if m=="h":
        h+=1
    elif m=="T":
        T+=1
    elif m=="D":
        D+=1

#Placing the chairs close to the walls

if h == len(y):
    if len(y)%2==0:
        for i in range(1,len(y),2):
            y[i][0]='h'
            h=h-1
    elif len(y)%2!=0:
         for a in range(0,len(y),2):
            y[a][0]='h'
            h=h-1
        

elif h==2*len(y):
    if len(y)%2==0:
        for b in range(1,len(y),2):
            y[b][0]='h'
            h=h-1
    elif len(y)%2!=0:
         for c in range(0,len(y),2):
            y[c][0]='h'
            h=h-1
elif h>len(y):
    if len(y)%2==0:
        for n in range(1,len(y),2):
            if h==0:
                break
            elif h!=0:
                y[n][0]='h'
                h=h-1
    elif len(y)%2!=0:
        for d in range(0,len(y),2):
            if h==0:
                break
            elif h!=0:
                y[d][0]='h'
                h=h-1

elif h<len(y):
    if len(y)%2==0:
        for e in range(1,len(y),2):
            if h==0:
                break
            elif h!=0:
                y[e][0]='h'
                h=h-1
    elif len(y)%2!=0:
        for f in range(0,len(y),2):
            if h==0:
                break
            elif h!=0:
                y[f][0]='h'
                h=h-1
                

if len(y)%2==0:
        for g in range(1,len(y),2):
            if h==0:
                break
            elif y[g][0]=='h' and y[g][-1]!='h':
                y[g][-1]='h'
                h=h-1
elif len(y)%2!=0:
        for f in range(0,len(y),2):
            if h==0:
                break
            elif y[f][0]=='h' and y[f][-1]!='h':
                y[f][-1]='h'
                h=h-1

#To place the tables; if the number of available lines are even and there are desktops in the input:
if D>0:
    if len(y)%2==0:
        for p in range(1,len(y),2):
            for q in range(len(y[p])-1):
                if T==0:
                    break
                elif T!=0:
                    if y[p][q]=='h':
                        y[p][q+1]='T'
                        T=T-1
                    elif y[p][q+1]=='h':
                        y[p][q]='T'
                        T=T-1
#if the number of lines are odd:
    elif len (y)%2!=0 :
        for r in range(0,len(y),2):
            if T==0:
                break
            elif T!=0:
                for s in range(len(y[r])-1):
                    if y[r][s]=='h':
                        y[r][s+1]='T'
                        T=T-1
                    elif y[r][s+1]=='h':
                        y[r][s]='T'
                        T=T-1
#To place the tables; if there are no desktops in the input:
elif D<1:
    for t in range(len(y)):
            for s in range(len(y[t])-1):
                if T==0:
                    break
                elif T!=0:
                    if y[t][s]=='h':
                        y[t][s+1]='T'
                        T=T-1
                    elif y[t][s+1]=='h':
                        y[t][s]='T'
                        T=T-1

#Placing the Desktops if there are any!
if D>0:
    if len(y)%2==0:
        for v in range(0,len(y),2):
            for u in range(len(y[v])-1):
                if D==0:
                    break
                elif D!=0:
                    if y[v][u]=='_' and y[v+1][u]=='T':
                        y[v][u]='D'
                        D=D-1
    elif len(y)%2!=0:
        for w in range(1,len(y),2):
            for z in range(len(y[w])-1):
                if D==0:
                    break
                elif D!=0:
                    
                    if y[w][z]=='_' and y[w+1][z]=='T':
                        y[w][z]='D'
                        D=D-1

#Filling the remaining spaces to accomodate maximum furniture!
a=1
while h!=0 and a<len(y):
    z=y[a]
    if len(y)%2==0:
        for l in range(1,len(z),2):
            if h==0:
                break
            elif z[l-1]=='_' and z[l+1]=='_' and z[l]!='D' or z[l-1]=='T' and z[l+1]=='_'  :
                z[l]='h'
                h=h-1
                a=a+1
    
    elif len(y)%2!=0:
        for q in range(1,len(z),2):
            if h==0:
                break
            
            elif z[q-1]=='_' and z[q+1]=='_' and z[q]!='D' or z[q-1]=='T' and z[q+1]=='_' :
                z[q]='h'
                h=h-1
                a=a+1


#Re-forming the room again
for l in y:
    l.insert(0,'_')
    l.insert(0,'w')
    l.append('_')
    l.append('w')
y.insert(0,['w']+['_' for l in range(len(y[0])-2)]+['w'])
y.insert(0,['w']+['w' for l in range(len(y[0])-2)]+['w'])
y.append(['w']+['_' for l in range(len(y[0])-2)]+['w'])
y.append(['w']+['w' for l in range(len(y[0])-2)]+['w'])


#Extracting the data from the list and displaying the final output!
c=''
for z in y:
    c+=''.join(z)+"\n"

#Displaying the final result in a new file.
file=open('Final output.txt','w')
file.write('The Final Output:'+'\n'+'\n'+c+'\n')
file.write('Number of Furnitures remaining:'+'\n')
file.write('Chairs = '+str(h)+'\n'+'Tables = '+str(T)+'\n'+'Desktops= '+str(D)+'\n')
file.close()

print(c)
