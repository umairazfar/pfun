#counting lines
wall=[]
file = open('room.txt','r')
lst=[]
count = 0
furniture = []
tables=''
chairs=''
computers=''
for line in file:
    if line[0]=='w' and line[1]=='w':
        w = line.strip('\n')
        wall.append(w)
        count = count+0                              #getting seperated lines of w and spaces
    elif line[0] == 'w' and line[1]=='_':
        count = count+1
        l= line.strip('\n')
        lst.append(l)
##print(line)
#counting furniture
    if line[0] == 'h':
        line = line.strip('\n')
        furniture.append(line)
        h = line.count('h')
        chairs=h
    elif line[0] == 'T':
        line = line.strip('\n')                    #counting furnitures
        furniture.append(line)
        t = line.count('T')
        tables = t
    elif line[0] == 'D':
        line = line.strip('\n')
        furniture.append(line)
        d = line.count('D')
        computers = d
total_number_of_lines = count+2
#print(total_number_of_lines)
#print(furniture)
#print('Number of chairs = ',a,'\n'+'Number of Tables = ',b,'\n'+'Number of Computers = ',c)
lst1=[]                              
for spaces in lst: 
    a = spaces[1:len(spaces)-3]                      #getting rows without w
    lst1.append(a)
#print(lst1)
j=[]
for i in lst1[1:len(lst)-1]:
    list(i)
##    i=i.split()
##    print(i)
    j.append(i)         #getting rows in which furniture can be placed
#print(j)
temp2 = []
count = 1
temp = []
jh=[]
for i in j[0::2]:
    #print(i)
    i = list(i)
    for k in range(len(i)):
        if i[k] == '_' and count%2 ==1 and t != 0:
            i[k] = 'T'
            t = t-1                                   #placing tables and chairs together in alternate lines
        if i[k]=='_' and count%2 == 0 and h >= 1:
            i[k]= 'h'
            h = h-1
        count = count + 1
    temp.append(i)
    jh.append(i)
#print(temp)
    #print(i)
count_2 = 1
if total_number_of_lines%2 == 1:
    temp1 = []
    for a in j[1::2]:
        a = list(a)
        for b in range(len(a)):
            if tables > d:
                if a[b] == '_' and count_2%2 ==1 and d!=0:
                    #print(d)                                      
                    a[b] = 'D'
                    d= d-1                                       #placing computers in accordance with the count of tables on alternate lines
                    tables = tables - 1
                    
                if a[b] == '_' and count_2%2 == 0 :
                    a[b] = '_'
                count_2 = count_2+1
            elif d > tables:
                if a[b] == '_' and count_2%2 == 1 and tables != 0:
                    #print(d)
                     a[b] = 'D'
                     d= d-1
                     tables = tables - 1
                if a[b] == '_' and count_2%2 == 0 :
                    a[b] = '_'
                    
                count_2 = count_2+1
                
        #print(a)
        temp1.append(a)
        jh.append(a)
    #print(temp1)
    count_3=0
    k=0
    o=0
    kj=[]
    for i in range(len(jh)):
        if count_3%2==0 and k!=len(temp1):
            kj.append(temp1[k])
            k=k+1                                  #arranging the lines and tables alternately
            count_3=count_3+1
        else:
            kj.append(temp[o])
            o=o+1
            count_3=count+1
#print(kj)
elif total_number_of_lines %2 == 0:
     temp1 = []
     for a in j[1::2]:
        a = list(a)
        for b in range(len(a)):
            if tables > d:
                if a[b] == '_' and count_2%2 == 1 and d!= 0:
                    #print(d)
                    a[b] = 'D'
                    tables = tables - 1
                    d= d-1
                if a[b] == '_' and count_2%2 == 0 :
                    a[b] = '_'                                              #arranging computers
                count_2 = count_2+1
            elif d > tables:
                if a[b] == '_' and count_2%2 == 1 and tables!= 0:
                    #print(d)
                    a[b] = 'D'
                    tables = tables - 1
                    d= d-1
                if a[b] == '_' and count_2%2 == 0 :
                    a[b] = '_'
                count_2 = count_2+1
        temp1.append(a)
        jh.append(a)
     #print(temp1)
     count_3=0
     k=0
     o=0
     kj=[]
     for i in range(len(jh)):
        if count_3%2==0 and k!=len(temp1):                                  #arranging the lines and tables alternately
            kj.append(temp1[k])
            k=k+1
            count_3=count_3+1
        else:
            kj.append(temp[o])
            o=o+1
            count_3=count_3+1
##print(kj)
file1 = open('anusha.txt','w')
file1.write(w+'\n')
file1.write(l+'\n')
print(w)
print(l)
for s in kj:
    s = ['w_']+s+['_w']
    room = ''.join(s)                                   #comdining walls and eliminated spaces
    file1.write(room+'\n')
    print(room)
print(l)
print(w)
file1.write(l+'\n')
file1.write(w+'\n')
file1.write('Numbers of computers left: '+str(d)+'\n')
file1.write('Numbers of tables left: '+str(t)+'\n')
file1.write('Numbers of chairs left: '+str(h)+'\n')
file1.close()
print('Numbers of computers left: ',d)
print('Numbers of tables left: ',t)
print('Numbers of chairs left: ',h)



