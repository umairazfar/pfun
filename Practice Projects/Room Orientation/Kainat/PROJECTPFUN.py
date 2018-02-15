file=open('room.txt', 'r')
text=file.readlines()
lst1=[]
tables=0
chairs=0
computers=0
tables1=0
chairs1=0
computers1=0
finallst=[]
pol=''
for line in text:
     if line[0]=='w':
          line=line.split()
          lst1.append(line)
     else:
          if line[0]=='h':
               print('Chairs =',line.count('h'))
               chairs=line.count('h')
               ct=chairs
          elif line[0]=='T':
               print('Tables =',line.count('T'))
               tables=line.count('T')
               oT=tables
          elif line[0]=='D':
               print('Computers =',line.count('D'))
               computers=line.count('D')
               cot=computers
               break
lst1=lst1[2:len(lst1)-2]
#print(lst1)
#print(lst1)
lst2=[]
for sublist in lst1:
     for line in sublist:
          rline=line[2:len(line)-2]
          rline=rline.split()
          lst2.append(rline)
#print(lst2)

initialcount=0
lst3=[]

for sublist in lst2:
     x=''
     if initialcount%2==0:
          #print('ji')
          for j in sublist:
               j=list(j)
               #print(j)
               semifinal=[]
               count=0
               jump1=0
               jump2=3
               lst4=[]
               
               if chairs<tables or chairs>tables or chairs==tables:
                    for space in range(0, len(j), 3):
                         select=(j[jump1:jump2])
                         lst4.append(select)
                         jump1=jump1+3
                         jump2=jump2+3
                         #print('ja')

                    if len(lst4[len(lst4)-1])==1:
                         for j in lst4[0:len(lst4)-1]:
                              if count%2==0 and chairs>=0 and tables>0:
                                   j[0]='h'
                                   j[1]='T'
                              elif count%2==0 and chairs>0 and tables<=0:
                                   j[0]='h'
                                   tables=tables+1
                              elif count%2==0 and chairs<=0 and tables>0:

                                   j[1]='T'
                                   chairs=chairs+1     
                              elif count%2==1 and chairs>0 and tables>0:
                                   j[1]='h'
                                   j[0]='T'
                              elif count%2==1 and chairs>0 and tables<=0:
                                   j[1]='h'
                                   tables=tables+1

                              elif count%2==1 and chairs<=0 and tables>0:
                                   j[0]='T'
                                   chairs=chairs+1
                              if chairs>0:
                                   chairs=chairs-1
                              if tables>0:
                                   tables=tables-1
                              count=count+1
                         
                         for k in lst4[len(lst4)-1]:
                              if (len(lst4)-1)%2==1 and tables>0:
                                   lst4[len(lst4)-1]=list('T')
                                   if tables>0:
                                        tables=tables-1
                              elif (len(lst4)-1)%2==0 and chairs>0:
                                   lst4[len(lst4)-1]=list('h')
                                   if chairs>0:
                                        chairs=chairs-1
                              finallst.append(lst4)
                              #print(finallst)
                              v=lst4
                              #print(v)
                              po=''
                              for i in v:
                                   for j in i:
                                        po=po+j
                              #print(po)
                              pol=po
                    else:
                         #print('p')
                         for j in lst4:
                              if count%2==0 and chairs>0 and tables>0:
                                   j[0]='h'
                                   j[1]='T'
                              elif count%2==0 and chairs>0 and tables<=0:
                                   j[0]='h'
                                   tables=tables+1
                              elif count%2==0 and chairs<=0 and tables>0:
                                   j[1]='T'
                                   chairs=chairs+1     
                              elif count%2==1 and chairs>0 and tables>0:
                                   j[1]='h'
                                   j[0]='T'
                              elif count%2==1 and chairs>0 and tables<=0:
                                   j[1]='h'
                                   tables=tables+1

                              elif count%2==1 and chairs<=0 and tables>0:
                                   j[0]='T'
                                   chairs=chairs+1
                              if chairs>0:
                                   chairs=chairs-1
                              if tables>0:
                                   tables=tables-1
                              count=count+1
                         finallst.append(lst4)

                         
     elif initialcount%2==1:
          '''
          for j in sublist:
               j=list(j)
          ii=0
          for i in pol:
               if i=='T' and computers>=0:
                    j[ii]='D'
                    computers=computers-1
               ii=ii+1
          #print(j)
          '''
          finallst.append(sublist)
     initialcount=initialcount+1
          
p=''
#print(finallst)
for j in finallst:
     for i in j:
          for k in i:
               p=p+k
     p=p+'\n'
#print(p)
#print(tables)
#print(chairs)
p=p.strip('\n').split('\n')
#print(len(p))
if len(p)%2==0:
     pi=p[0:len(p)-1]
else:
     pi=p
#print(pi)
#print(p)
puo=[]
for j in pi:
     j=list(j)
     #print(j)
     puo.append(j)
#print(puo)
#print(len(puo))
for o in range(0,len(puo)):
     if o%2==1:
          for u in range(0,len(puo[o+1])):
               #print(u)
               if puo[o+1][u]=='T' and computers>0:
                    puo[o][u]='D'
                    computers=computers-1
          #print(puo[o])
#print(puo)
#print(finallst)
if len(p)%2==0 or len(p)%2==1:
     kjh='w_'
     for uj in puo:
          for j in uj:
               kjh=kjh+j
          #print('k',kjh)
          #break
          kjh=kjh+'_w'+'\n'+'w_'
     if len(p)%2==1:
          kjh=(kjh[0:len(kjh)-2]).strip()
     else:
          kjh=kjh.strip()

     
if len(p)%2==0:
     kjh=kjh+p[len(p)-1]+'_w'
#print(kjh)
for i in lst1[0]:
     yu=(len(i))
finalresult=('\n'+yu*'w'+'\n'+('w'+(yu-2)*'_'+'w')+'\n'+kjh+'\n'+('w'+(yu-2)*'_'+'w')+'\n'+yu*'w')
print(finalresult)
print('\nRemaining Furniture')
print('tables =',tables)
print('computers =',computers)
print('chairs =', chairs)


filepro=open('kabbasi.txt', 'w')
filepro.write(finalresult+'\n')
filepro.write('\n'+'Remaining Furniture'+'\n')
filepro.write('tables = '+str(tables)+'\n')
filepro.write('computers = '+str(computers)+'\n')
filepro.write('chairs = '+str(chairs)+'\n')
filepro.close()
