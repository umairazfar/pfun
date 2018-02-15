lst=[]
c=[]
file=open("TEXT.txt","r")
f=file.readlines()
file.close()
for line in f:
     if line[0]=='w':
          line=line.split()               ##number of lines to work on
          lst.append(line)
p=lst
p=(lst[2:len(lst)-2])
#print(p)


x=[]
b=[]
for i in p:
     for j in i:
          c.append(j)
#print(c)
for i in c:                                    ##finding available spaces
     for j in i:
          b.append(j)
     x.append(b)
     b  =[]
#print(x)
#print(len(x))
     
spaces=0
for i in x:
     for j in i:                            ##number of spaces
          if j=='_':
               spaces+=1
#print(spaces)


y=[]
a=[]
lst2=[]               
for line in f:
     if line[0]!='w':                  ##adding furnitures in a list
          line=line.split()
          lst2.append(line)
lst2=(lst2[1:len(lst2)])
for i in lst2:
     for j in i:                   
          for k in j:
               y.append(k)
     a.append(y)
     y  =[]
#print(a)


h=0
t=0
d=0
for i in a:
     for j in i:
          if j=='h':
               h+=1                    ##number of each furniture
          elif j=='T':
               t+=1
          elif j=='D':
               d+=1
               
total=h+t+d
#print(total)


s=spaces//total
                       #best fit 'steps' 
po=spaces-total
#print(po)


if po>15 and len(x)>4:
     if len(x)%2==1:
          for line in range(len(x)-1,-1,-1):
               if line%2 == 0:     
                    for i in range(2, len(x[line])-2, 4):
                         if x[line][i] == '_' and h != 0:
                              x[line][i] = 'h'                         ##aranging furniture in spaces
                              h -= 1
                    for i in range(3, len(x[line])-2, 2):
                         if x[line][i] == '_' and t != 0:
                              x[line][i] = 'T'
                              t -= 1

               else:
                    for i in range(len(x[line])):
                         if x[line+1][i] == 'T' and d!=0:
                              x[line][i] = 'D'
                              d -= 1
     else:
          for line in range(len(x)-1,-1,-1):
               if line%2 == 1:     
                    for i in range(2, len(x[line])-2, 4):
                         if x[line][i] == '_' and h != 0:
                              x[line][i] = 'h'                         ##aranging furniture in spaces
                              h -= 1
                    for i in range(3, len(x[line])-2, 2):
                         if x[line][i] == '_' and t != 0:
                              x[line][i] = 'T'
                              t -= 1

               else:
                    for i in range(len(x[line])):
                         if x[line+1][i] == 'T' and d!=0:
                              x[line][i] = 'D'
                              d -= 1          
else:
     if len(x)%2==1:
          for line in range(len(x)-1,-1,-1):
               if line%2 == 0:     
                    for i in range(2, len(x[line])-2, 2):
                         if x[line][i] == '_' and h != 0:
                              x[line][i] = 'h'                         ##aranging furniture in spaces
                              h -= 1
                    for i in range(3, len(x[line])-2, 2):
                         if x[line][i] == '_' and t != 0:
                              x[line][i] = 'T'
                              t -= 1

               else:
                    for i in range(len(x[line])):
                         if x[line+1][i] == 'T' and d!=0:
                              x[line][i] = 'D'
                              d -= 1
     else:
          for line in range(len(x)-1,-1,-1):
               if line%2 == 1:     
                    for i in range(2, len(x[line])-2, 2):
                         if x[line][i] == '_' and h != 0:
                              x[line][i] = 'h'                         ##aranging furniture in spaces
                              h -= 1
                    for i in range(3, len(x[line])-2, 2):
                         if x[line][i] == '_' and t != 0:
                              x[line][i] = 'T'
                              t -= 1

               else:
                    for i in range(len(x[line])):
                         if x[line+1][i] == 'T' and d!=0:
                              x[line][i] = 'D'
                              d -= 1   
      
for a in lst[0:2]:
     u=(''.join(a))                       ##making the room
     print(u)
     
for l in x:
     q=(''.join(l))
     print(q)
     
for b in lst[-2:]:
     r=(''.join(b))
     print(r)
     
print()
print('number of chairs(h) left:',h)
print('number of tables(T) left:',t)
print('number of computers(D) left:',d)


file=open("Final_Room.txt","w")
      
for a in lst[0:2]:
     u=(''.join(a))                       
     file.write(u+'\n')
     
for l in x:
     q=(''.join(l))
     file.write(q+'\n')
     
for b in lst[-2:]:
     r=(''.join(b))
     file.write(r+'\n')
file.write('\n'+'number of chairs(h) left: '+str(h)+'\n')
file.write('number of tables(T) left: '+str(t)+'\n')
file.write('number of computers(D) left: '+str(d)+'\n')
file.close()









                                                                           

