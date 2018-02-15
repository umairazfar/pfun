file = open('project wall1.txt')
text = file.readlines()
lst = []
y = []
lst1 = []
lst2 = []
str1 = ''
str2 = ''
str3 = []
final = ''
leftovers = ''
spaces = []
h = ''
d = ''
t = ''
space = ""
counth = 0
countt = 0
countd = 0
n_khali_jagha = 0

q = 0


for i in range(len(text)):
    if text[i][0]=="w":
        lst = lst + [text[i].strip()]
    elif text[i][0]=="\n":
        continue
    else:
        y = y + list(text[i].strip())

for i in lst[2:-2]:
    spaces.append(list(i[2:-2]))
lst1 = lst1 + lst[0:2]
lst2 = lst1[::-1]
#print(lst1)
#print(lst2)
for i in y:
    if i == "h":
        h = h + i
        counth += 1
    elif i == "D":
        d = d + i
        countd += 1
    elif i == "T":
        t = t + i
        countt += 1
for i in spaces:
    for j in i:
        n_khali_jagha += 1
    break
h_ke_liye = n_khali_jagha - 1

a = 0
b = 1
c = 0
d = 0
e = 0
if countt > 0:
    if counth > 0:
        while a < len(spaces):
            while b < n_khali_jagha and countt != 0:
                spaces[a][b] = "T"
                b = b + 3
                countt = countt - 1
            a = a + 2
            b = 1
        a = 0
        while a < len(spaces):
            while e < n_khali_jagha and counth != 0:
                if spaces[a][e] == "T":
                    spaces[a][e-1] = "h"
                    counth = counth - 1
                    if e != h_ke_liye:
                         spaces[a][e+1] = "h"
                         counth = counth - 1
                e = e + 1
            a = a + 1
            e = 0    


        for u in spaces:
            for t in range(len(u)):
                if t != h_ke_liye and u[t] == u[t+1]:
                    u[t+1] = "_"
                else:
                    continue
            
    elif counth == 0:
        while a < len(spaces):
            while c < n_khali_jagha and countt != 0:
                spaces[a][c] = "T"
                c = c + 2
                countt = countt - 1
                
            a = a + 2
            c = 0
    
    a = 0
    while a < len(spaces):
        while d < n_khali_jagha and countd != 0:
            if spaces[a][d] == "T" and a != len(spaces) - 1:
                spaces[a+1][d] = "D"
                countd = countd - 1
            d = d + 1
        a = a + 1      
        d = 0
elif countt == 0:
    a = 0
    c = 0
    while a < len(spaces):
            while c < n_khali_jagha and counth != 0:
                spaces[a][c] = "h"
                c = c + 2
                counth = counth - 1
            a = a + 2
            c = 0


            
spaces = spaces[::-1]
for i in spaces:
    q = "".join(i)
    space += q + "\n"


for j in space:
    str1 += j
s = str1.split("\n")
t = s[0:len(s)-1]
for j in range(len(t)):
    str2 = str2 + "w_" + t[j] + "_w "
o = str2.split()
for k in o:
    lst1.append(k)
lst1.extend(lst2)
for i in lst1:
    final += i + "\n"

leftovers += ("The following are the number of furniture which is left:" + "\n"
              + "Tables: " + str(countt) + "\n" + "Chairs: " + str(counth) + "\n" + "Computers: " + str(countd)) 


file = open('Muhammad Shaheer.txt', 'w')
file.write(final)
file.write("\n")
file.write(leftovers)
file.close()















