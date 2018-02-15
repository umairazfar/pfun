file = open('room.txt','r')
text = file.readlines()
s = text[0].strip()
num_lines = sum(1 for line in open('room.txt'))
if num_lines <= 3 or len(s) <= 4:
    print('this room is invalid')
    quit()
lst=[]
for i in text:
    lst.append(i.strip())
h=['h','h','h','h','h','h','h','h','h']
T=['T','T']
D=[]
a=[]
for m in range(2,len(lst)-2):
    s=''
    for y in range(2,len(lst[m])-2):
        s=s+lst[m][y]
    a.append(list(s))
num=0
for i in a:
    num = num + len(i)
if len(D) == 0 and len(h)!= 0 and len(T) != 0:
    for i in a:
        b = 0
        while b <= len(i):
            if len(h) == 0:
                break
            else:
                i[b] = h.pop(0)
                b = b + (len(i)-1)
                
    for i in a:
        b = 0
        while b <= len(i)-1:
            if len(T) == 0:
                break
            elif b == len(i)-1 and i[b] == 'h':
                i[b-1] = T.pop(0)
                break
            elif i[b] == 'h':
                i[b+1] = T.pop(0)
                
            b = b + 1
elif len(D)!=0 and len(h)!= 0:
    for i in range(0,len(a),2):
        b = 0
        while b <= len(a[i]):
            if len(h) == 0:
                break
            else:
                a[i][b] = h.pop(0)
                b = b + (len(a[i])-1)
                
    for i in a:
        b = 0
        while b <= len(i)-1:
            if len(T) == 0:
                break
            elif b == len(i)-1 and i[b] == 'h':
                i[b-1] = T.pop(0)
                break
            elif i[b] == 'h':
                i[b+1] = T.pop(0)
                
            b = b + 1
    for i in range(len(a)):
        if 'T' in a[i] and i!=0:
            c = [i for i, x in enumerate(a[i]) if x == 'T']
            for x in c:
                if len(D) == 0:
                    break
                else:
                    a[i-1][x] = D.pop(0)
elif len(h) == 0 and len(D) == 0:
    for i in a:
        b = 0
        while b <= len(i)-1:
            if len(T) == 0:
                break
            else:
                i[b] = T.pop(0)
                b = b + (len(i)-1)
    for i in a:
        if len(T) != 0 and '_' in i:
            b = 0
            while b <= len(i)-1:
                if len(T) == 0:
                    break
                elif i[b] == '_' :
                    i[b] = T.pop(0)
                else:
                    pass
                b = b + 1
        elif '_' not in i:
            pass
elif len(h) == 0 and len(D)!= 0 and len(T)!= 0:
    for i in range(len(a)-1,0,-1):
        b = 0
        while b <= len(a[i])-1:
            if len(T) == 0:
                break
            else:
                a[i][b] = T.pop(0)
                b = b + (len(a[i])-1)
    for i in range(len(a)):
        if 'T' in a[i] and i!=0:
            c = [i for i, x in enumerate(a[i]) if x == 'T']
            for x in c:
                if len(D) == 0:
                    break
                elif '_' in a[i-1][x] :
                    a[i-1][x] = D.pop(0)
    for i in range(len(a)-1,0,-1):
        if len(T) != 0 and '_' in a[i]:
            b = 0
            while b <= len(a[i])-1:
                if len(T) == 0:
                    break
                elif a[i][b] == '_':
                    a[i][b] = T.pop(0)
                b = b + 1
                
    for i in range(len(a)):
        if len(D) != 0 and '_' in a[i]:
            if i != len(a)-1:
                c = [i for i, x in enumerate(a[i+1]) if x == 'T']
                for x in c:
                    if len(D) == 0:
                        break
                    elif a[i][x] == '_':
                        a[i][x] = D.pop(0)
            else:
                break
            
elif len(h) != 0 and len(T) == 0 and (len(D) == 0 or len(D) != 0) :
    for i in range(0,len(a),2):
        b = 0
        while b <= len(a[i])-1:
            if len(h) == 0 :
                break
            else:
                a[i][b] = h.pop(0)
                b = b + (len(a[i])-1)
    for i in a:
        if len(h) != 0 and '_' in i:
            b = 0
            while b <= len(i)-1:
                if len(h) == 0 :
                    break
                elif i[b] == '_' and i[b+1] != 'h' and i[b-1] != 'h':
                    i[b] = h.pop(0)    
                b = b + 1
                if b == len(i)-1:
                    if i[b-1] != 'h' and i[b] == '_' and len(h) != 0:
                        i[b] = h.pop(0)
                        break
for i in a:
    if '_' in i and len(h)!=0 :
        b=0
        while b < len(i)-1:
            if i[b] == '_' and i[b+1] != 'h' and i[b-1] != 'h' and len(h) != 0:
                i[b] = h.pop(0)
            else:
                pass
            b = b + 1
            if b == len(i) - 1 :
                break
print(h)            
str1=''
str2 = ''
x = 2
for i in range(len(a)):
    str1 = 'w_' + ''.join(a[i]) + '_w'
    if x > len(lst)-3:
        break
    else:
        lst[x] = str1
    x = x + 1
    
for i in lst:
    str2 = str2 + i + '\n'
file.close()
file1 = open('arranged room.txt','w')
file1.write('There are ' + str(num) + ' empty spaces' + '\n')
file1.write('\n')
file1.write(str2)
file1.write('\n')
valid = False
if len(h)!=0 :
    file1.write(str(len(h)) + ' seats cannot be arranged') 
if len(T)!=0 :
    file1.write(str(len(T)) + ' tables cannot be arranged')
if len(D)!=0 :
    file1.write(str(len(D)) + ' computers cannot be arranged')
file1.close()    
print(lst)

