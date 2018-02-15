file = open("room.txt", "r")

room = file.readlines()

for line in room:
    if line == "\n":
        print(line)
        room.remove(line)

roomm = []   #roomm is the modified room.

for line in room:
    roomm.append(line.strip("\n"))

width = len(roomm[0])-2
length = len(roomm)-5
area = width*length

fq = len(roomm[-1])+len(roomm[-2])+len(roomm[-3]) #fq is the furniture quantity

if area==4:
  print("The amount of furniture provided is too much for the considered room, please buy a bigger house or discard some of the furniture." +"\n"+ "Or what you can do is sell some of the furniture to buy a bigger house, but then you won't have the furniture to fill that house with. See? Paradoxical.")
  raise SystemExit
else:
  pass




print(roomm)

del roomm[0:2]
print(roomm)
del roomm[length-2:length]
furniture = []
teles = list(roomm.pop(length))
tables = list(roomm.pop(length-1))
chairs = list(roomm.pop(length-2))


spaces = []
for line in roomm:
  nline = line.replace("w_", "")
  nline = nline.replace("_w", "")
  nline = list(nline)
  spaces = spaces + nline




def chair():
  h = len(chairs)
  if h > 0:
    for q in range(len(spaces)):
      if q == 0:
        spaces[q] = "h"
        h = h -1
        ch = h
      elif q == width-3:
        spaces[q] = "h"
        h = h -1
        ch = h
      elif q>=(((width-2)*2)-1) and q%(width-2) == 0:
        spaces[q] = "h"
        h = h -1
        ch = h
        if h>0:
          spaces[-1] = "h"
          h = h-1
          ch = h
  
  print("Number of chairs left =" ,ch )

def table():
  T = len(tables)
  if T > 0:
    for e in range(len(spaces)-1):
      if spaces[e] == "h" and spaces[e+1] == "_" and e != width-3:
        spaces[e+1] = "T"
        T = T-1
        ta = T
      elif spaces[e] == "h" and spaces[e-1] == "_":
        spaces[e-1] = "T"
        T = T-1
        ta = T
      elif spaces[-1] == "h":
          spaces[-2] = "T"
          ta = T-1  
  print("Number of tables left =" ,ta )
def computer():
  co = 0
  D = len(teles)
  if D>0:
    for r in range(len(spaces)):
      if spaces[r] == "T" and spaces[r-(width-2)] == "_":
        spaces[r-(width-2)] = "D"
        D = D-1
        co = D
      
  print("Number of computers left =" ,co )
chair()
table()
computer()


first = "w" * (width+2) #first is also last
second = "w" + "_"*(width) + "w"

print()


def compiled():
  final = ""
  if length == 3:
    str1 = "W_" + "".join(spaces[0:width-2]) + "_W" + "\n"
    final = first + "\n" + second + "\n" + str1 + second+"\n" + first
  elif length == 4:
    str1 = "W_" + "".join(spaces[0:width-2]) + "_W" + "\n"
    str2 = "W_" + "".join(spaces[width-2:(width*2)-4]) + "_W" + "\n"
    final = first + "\n" + second + "\n" + str1 + str2 + second+"\n" + first
  elif length == 5:
    str1 = "W_" + "".join(spaces[0:width-2]) + "_W" + "\n"
    str2 = "W_" + "".join(spaces[width-2:(width*2)-4]) + "_W" + "\n"
    str3 = "W_" + "".join(spaces[(width*2)-4:(width*3)-6]) + "_W" + "\n"
    final = first + "\n" + second + "\n" + str1 + str2 + str3 +second+"\n" + first
  elif length == 6:
    str1 = "W_" + "".join(spaces[0:width-2]) + "_W" + "\n"
    str2 = "W_" + "".join(spaces[width-2:(width*2)-4]) + "_W" + "\n"
    str3 = "W_" + "".join(spaces[(width*2)-4:(width*3)-6]) + "_W" + "\n"
    str4 = "W_" + "".join(spaces[(width*3)-6:(width*4)-8]) + "_W" + "\n"
    final = first + "\n" + second + "\n" + str1 + str2 + str3 + str4  +second+"\n" + first
  elif length == 7:
    str1 = "W_" + "".join(spaces[0:width-2]) + "_W" + "\n"
    str2 = "W_" + "".join(spaces[width-2:(width*2)-4]) + "_W" + "\n"
    str3 = "W_" + "".join(spaces[(width*2)-4:(width*3)-6]) + "_W" + "\n"
    str4 = "W_" + "".join(spaces[(width*3)-6:(width*4)-8]) + "_W" + "\n"
    str5 = "W_" + "".join(spaces[(width*4)-8:]) + "_W" + "\n"
    final = first + "\n" + second + "\n" + str1 + str2 + str3 + str4 + str5 +second+"\n" + first
  print(final)

compiled()      


    




