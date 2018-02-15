file = open("Project_2.txt", 'r')
lines = file.readlines()
lines1=[]
for i in lines:
    lines1.append(i.strip())
for i in range(len(lines1)):
    if lines1[i].startswith("www") and lines1[i].endswith("www"):
        room1=lines1[i:]
        break
for x in range(len(room1)):
    if room1[x].startswith("www") and lines1[i].endswith("www") and x>0:
        room=room1[0:x+1]
        break       
chair=[]
table=[]
computer=[]
for x in lines1:
    if x.startswith("h") and x.endswith("h"):
        for h in x:
            chair.append(h)
for x in lines1:
    if x.startswith("T") and x.endswith("T"):
        for T in x:
            table.append(T)
for x in lines1:
    if x.startswith("D") and x.endswith("D"):
        for D in x:
            computer.append(D)

def furnitureplacement(room,chair,table,computer):
    room_change=room[2:len(room)-2]
    if len(room_change)<3:
        print("No furniture can be placed inside this room.")
        string=''
        for i in room:
            string+=i+'\n'
        print(string)
        print("Total number of furniture remaining:"+"\n"+str(chair.count('h')+table.count('T')+computer.count('D'))+'\n')
        print("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chair.count('h'))+'\n'+"Tables:"+str(table.count('T'))+'\n'+"Computers:"+str(computer.count("D")))

        file=open("Solution_Final_Room.txt","w")
        file.write("No furniture can be placed inside this room."+"\n\n"+string+'\n')
        file.write("Total number of furniture remaining:"+"\n"+str(chair.count('h')+table.count('T')+computer.count('D'))+'\n')
        file.write("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chair.count('h'))+'\n'+"Tables:"+str(table.count('T'))+'\n'+"Computers:"+str(computer.count("D")))
        file.close()
            
    elif len(room_change[0])<5:
        print("No furniture can be placed inside this room.")
        string=''
        for i in room:
            string+=i+'\n'
        print(string)
        print("Total number of furniture remaining:"+"\n"+str(chair.count('h')+table.count('T')+computer.count('D'))+'\n')
        print("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chair.count('h'))+'\n'+"Tables:"+str(table.count('T'))+'\n'+"Computers:"+str(computer.count("D")))

        file=open("Solution_Final_Room.txt","w")
        file.write("No furniture can be placed inside this room."+"\n\n"+string+'\n')
        file.write("Total number of furniture remaining:"+"\n"+str(chair.count('h')+table.count('T')+computer.count('D'))+'\n')
        file.write("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chair.count('h'))+'\n'+"Tables:"+str(table.count('T'))+'\n'+"Computers:"+str(computer.count("D")))
        file.close()

    else:
        new=[]
        for k in range(len(room_change)):
            new.append(room_change[k][2:len(room_change[k])-2])
        wholespace="".join(new)
        spaceavailable=[]
        for j in new:
            spaceavailable.append(list(j))
        
        if len(spaceavailable)%2!=0:
            
            for j in range(0,len(spaceavailable),2):
                for k in range(len(spaceavailable[j])):
                    for x in range(len(table)):
                        if table[x]=="T" and (k==1 or k==len(spaceavailable[j])-2):
                            spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]                                       
                                    
                
            for j in range(0,len(spaceavailable),2):
                for k in range(len(spaceavailable[j])-1):
                    for x in range(len(chair)):
                        if chair[x]=="h" and spaceavailable[j][k]=='T':
                            spaceavailable[j][k+1],chair[x]=chair[x],spaceavailable[j][k+1]
                            spaceavailable[j][k-1],chair[x]=chair[x],spaceavailable[j][k-1]

            if len(spaceavailable[0])>5:
                for j in range(0,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])):
                        for x in range(len(table)):
                            if table[x]=="T" and (k==len(spaceavailable[j])//2):
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]
                                
                for j in range(0,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])-1):
                        if spaceavailable[j][k]=="h" and spaceavailable[j][k-1]=="T":
                            for y in range(k,len(spaceavailable[j])-1):
                                if spaceavailable[j][y]=='T' and spaceavailable[j][y+1]=="_":
                                    for x in range(len(table)):
                                        if table[x]=='T':
                                            spaceavailable[j][k+y//2+2],table[x]=table[x],spaceavailable[j][k+y//2+2]

            
            chairleft=""
            for h in chair:
                chairleft+=h

            tableleft=""
            for T in table:
                tableleft+=T
            

            if chairleft.count('h')!=0 and tableleft.count('T')==0:
                for j in range(0,len(spaceavailable),2):
                    for k in range(2,len(spaceavailable[j])-1):
                        for x in range(len(chair)):
                            if (spaceavailable[j][k]=='_') and (spaceavailable[j][k-1]=='T'or spaceavailable[j][k+1]=='T') and chair[x]=='h':
                                spaceavailable[j][k],chair[x]=chair[x],spaceavailable[j][k]

            elif chairleft.count('h')==0 and tableleft.count('T')!=0:
                for j in range(0,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])-1):
                        for x in range(len(table)):
                            if spaceavailable[j][k]=='_' and (spaceavailable[j][k+1]=='_' or spaceavailable[j][k-1]=='_') and table[x]=='T':
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]

                            

            elif chairleft.count('h')!=0 and tableleft.count('T')!=0:
                for j in range(0,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])):
                        for x in range(len(chair)):
                            if (spaceavailable[j][k-1]=='T' or spaceavailable[j][k+1]=='T') and (spaceavailable[j][k]=='_') and chair[x]=='h':
                                   spaceavailable[j][k],chair[x]=chair[x],spaceavailable[j][k]

                for j in range(0,len(spaceavailable),2):
                    for k in range(1,len(spaceavailable[j])-1):
                        for x in range(len(table)):
                            if spaceavailable[j][k-1]=='h' and spaceavailable[j][k+1]=='h' and spaceavailable[j][k]=='_' and table[x]=='T':
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]                                               

        else:
            for j in range(1,len(spaceavailable),2):
                for k in range(len(spaceavailable[j])):
                    for x in range(len(table)):
                        if table[x]=="T" and (k==1 or k==len(spaceavailable[j])-2):
                            spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]                                       
                                    
                
            for j in range(1,len(spaceavailable),2):
                for k in range(len(spaceavailable[j])-1):
                    for x in range(len(chair)):
                        if chair[x]=="h" and spaceavailable[j][k]=='T':
                            spaceavailable[j][k+1],chair[x]=chair[x],spaceavailable[j][k+1]
                            spaceavailable[j][k-1],chair[x]=chair[x],spaceavailable[j][k-1]

            if len(spaceavailable[0])>5:
                for j in range(1,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])):
                        for x in range(len(table)):
                            if table[x]=="T" and (k==len(spaceavailable[j])//2):
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]
                                
                for j in range(1,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])-1):
                        if spaceavailable[j][k]=="h" and spaceavailable[j][k-1]=="T":
                            for y in range(k,len(spaceavailable[j])-1):
                                if spaceavailable[j][y]=='T' and spaceavailable[j][y+1]=="_":
                                    for x in range(len(table)):
                                        if table[x]=='T':
                                            spaceavailable[j][k+y//2+2],table[x]=table[x],spaceavailable[j][k+y//2+2]
                                            break

            
            chairleft=""
            for h in chair:
                chairleft+=h

            tableleft=""
            for T in table:
                tableleft+=T
            

            if chairleft.count('h')!=0 and tableleft.count('T')==0:
                for j in range(1,len(spaceavailable),2):
                    for k in range(2,len(spaceavailable[j])-1):
                        for x in range(len(chair)):
                            if (spaceavailable[j][k]=='_') and (spaceavailable[j][k-1]=='T'or spaceavailable[j][k+1]=='T') and chair[x]=='h':
                                spaceavailable[j][k],chair[x]=chair[x],spaceavailable[j][k]

            elif chairleft.count('h')==0 and tableleft.count('T')!=0:
                for j in range(1,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])-1):
                        for x in range(len(table)):
                            if spaceavailable[j][k]=='_' and (spaceavailable[j][k+1]=='_' or spaceavailable[j][k-1]=='_') and table[x]=='T':
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]

                            

            elif chairleft.count('h')!=0 and tableleft.count('T')!=0:
                for j in range(1,len(spaceavailable),2):
                    for k in range(len(spaceavailable[j])):
                        for x in range(len(chair)):
                            if (spaceavailable[j][k-1]=='T' or spaceavailable[j][k+1]=='T') and (spaceavailable[j][k]=='_') and chair[x]=='h':
                                   spaceavailable[j][k],chair[x]=chair[x],spaceavailable[j][k]

                for j in range(1,len(spaceavailable),2):
                    for k in range(1,len(spaceavailable[j])-1):
                        for x in range(len(table)):
                            if spaceavailable[j][k-1]=='h' and spaceavailable[j][k+1]=='h' and spaceavailable[j][k]=='_' and table[x]=='T':
                                spaceavailable[j][k],table[x]=table[x],spaceavailable[j][k]                                               


                      
        for j in range(len(spaceavailable)-1):
            for k in range(len(spaceavailable[j])):
                for x in range(len(computer)):
                    if spaceavailable[j+1][k]=='T' and computer[x]=="D":
                        spaceavailable[j][k],computer[x]=computer[x],spaceavailable[j][k]
        

        for j in range(len(spaceavailable)):
            for k in range(len(spaceavailable[j])-1):
                if spaceavailable[j][k]=='h' and (spaceavailable[j][k-1]!='T' and spaceavailable[j][k+1]!='T'):
                    spaceavailable[j][k],chair[0]=chair[0],spaceavailable[j][k]           

        chairleft=""
        for h in chair:
            chairleft+=h

        tableleft=""
        for T in table:
            tableleft+=T        

        computerleft=""
        for D in computer:
            computerleft+=D        
        
        front=["w","_"]
        last=["_","w"]
        temp=[]
        for j in range(len(spaceavailable)):
            temp.append(front+spaceavailable[j]+last)
            
        filledspace=[]
        for i in range(len(temp)):
            filledspace.append("".join(temp[i]))

        finalroomlst=room[0:2]+filledspace+room[len(room)-2:]

        finalroom=""
        for i in finalroomlst:
            finalroom+=i+"\n"

        print("Room with Furniture:"+"\n\n"+finalroom+"\n")
        print("Total number of furniture remaining:"+"\n"+str(chairleft.count('h')+tableleft.count('T')+computerleft.count('D'))+'\n')
        print("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chairleft.count('h'))+'\n'+"Tables:"+str(tableleft.count('T'))+'\n'+"Computers:"+str(computerleft.count("D")))




        file=open("Solution_Final_Room.txt","w")
        file.write("Room with Furniture:"+"\n\n"+finalroom+"\n")
        file.write("Total number of furniture remaining:"+"\n"+str(chairleft.count('h')+tableleft.count('T')+computerleft.count('D'))+'\n')
        file.write("Number of each remaining furniture:"+"\n"+"Chairs:"+str(chairleft.count('h'))+'\n'+"Tables:"+str(tableleft.count('T'))+'\n'+"Computers:"+str(computerleft.count("D")))
        file.close()

furnitureplacement(room,chair,table,computer)

