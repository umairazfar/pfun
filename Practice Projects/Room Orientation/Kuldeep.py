file=open("project practice file.txt","r")
text = file.read()
file.close()


def furniture(text):
    furniture = []
    for i in text:
        if i=="h" or i== "T" or i== "D":
            furniture.append(i)
    return furniture
(furniture(text))

def room(text):
    room=""
    for i in text:
        if i=="h" or i== "T" or i== "D":
            continue
        else:
            room+=i
    return room.strip()
(room(text))

def area_to_place(room):
    room=room(text)
    area_to_place=""
    for i in range(len(room)-1):
        if room[i]=="w" and room[i+1]=="&":
            continue
        if room[i]=="w":
            continue
        else:
            area_to_place+=room[i]
    area_to_place=area_to_place.strip()
    area_to_place=area_to_place.split("\n")
    del area_to_place[0]
    del area_to_place[-1]
    left_area=""
    for x in range(len(area_to_place)):
        y=list(area_to_place[x])
        del y[0]
        del y[-1]
        y="".join(y)
        left_area+=y+"\n"
    return(left_area.strip())
(area_to_place(room))


def placement(area_to_place,furniture):
    area_left=area_to_place(room)
    furniture=furniture(text)
    if len(area_left)==0:
        return "can't be placed"
    else:
        area_left_lst=(area_left).split("\n")
        for element in range(len(furniture)):
                if furniture[element]=="h":
                        for place in range(0,len(area_left_lst),2):
                                    area_left_lst[place]=list(area_left_lst[place])
                                    area_left_lst[place][0]="h"
                                    area_left_lst[place][0],furniture[element]=furniture[element],area_left_lst[place][0]
                                    for spot in range(4,len(area_left_lst[place]),4):
                                            if area_left_lst[place][spot-1]!="h":
                                                    area_left_lst[place][spot],furniture[element]=furniture[element],area_left_lst[place][spot]
                area_left_lst[place]="".join(area_left_lst[place])
                if furniture[element]=="T":
                        for place in range(0,len(area_left_lst),2):
                                    area_left_lst[place]=list(area_left_lst[place])                                    
                                    if "T" not in furniture:
                                        continue
                                    area_left_lst[place][1]="T"
                                    for spot in range(3,len(area_left_lst[place])-1,):
                                            if area_left_lst[place][spot-1]=="h":
                                                    area_left_lst[place][spot],furniture[element]=furniture[element],area_left_lst[place][spot]
        area_left_lst[0]="".join(area_left_lst[0])
        for item in range(len(area_left_lst)):
                area_left_lst[item]=list(area_left_lst[item])
                for swap in range(5,len(area_left_lst[item]),8):
                                if area_left_lst[item][swap]=="T":
                                                area_left_lst[item][swap],area_left_lst[item][swap-1]=area_left_lst[item][swap-1],area_left_lst[item][swap]
        area_left_lst[place]="".join(area_left_lst[place])
        if furniture[element]=="D":
                                for place in range(1,len(area_left_lst)-1,2):
                                    area_left_lst[place]=list(area_left_lst[place])
                                    area_left_lst[place][1]="D"
                                    a=area_left_lst[place+1]
                                    for spot in range(4,len(area_left_lst[place])-1,5):
                                        for times in range(area_left_lst[place+1].count("T")):
                                            for search in range(len(a)):
                                                if a[search]=="T":
                                                    area_left_lst[place+1]="".join(area_left_lst[place+1])
                                                    index=area_left_lst[place+1].find(area_left_lst[place+1][search])
                                                    area_left_lst[place+1]=list(area_left_lst[place+1])
                                                    for i in furniture:
                                                        if i=="D":
                                                            area_left_lst[place][search],i=i,area_left_lst[place][search]
                                                            break
        area_left_lst[0]="".join(area_left_lst[0])
        area_left_lst[place]="".join(area_left_lst[place])
        area_left_updated="\n".join(["".join(x) for x in area_left_lst])
        return(area_left_updated)
((placement(area_to_place,furniture)))

def updated_room(placement):
    initial_room=room(text)
    updated_area=placement(area_to_place,furniture)
    updated_area_lst=updated_area.split("\n")
    initial_room_lst=initial_room.split("\n")
    updated_room=[]
    updated_room+=[initial_room_lst[0]]
    updated_room+=[initial_room_lst[1]]
    for x in range(2,len(initial_room_lst)-2):
        lines=list(initial_room_lst[x])
    x= len(updated_area_lst)
    for y in range(x):
        string="w__w"
        string = string[:2] + "".join(updated_area_lst[y])+ string[2:]
        updated_room.append(string)
        string = ""
    updated_room=("\n".join(updated_room))
    updated_room=updated_room+"\n"+"".join(initial_room_lst[-2])+"\n"+"".join(initial_room_lst[-1])
    return updated_room
print(updated_room(placement))

def remaining(placement,furniture):
        room=placement(area_to_place,furniture)
        furniture=(furniture(text))
        chair_count=room.count("h")
        table_count=room.count("T")
        desktop_count=room.count("D")
        for x in range(chair_count):
            if "h" not in furniture:
                continue
            (furniture).remove("h")
        for x in range(table_count):
            if "T" not in furniture:
                continue
            (furniture).remove("T")
        for x in range(desktop_count):
            if "D" not in furniture:
                continue
            (furniture).remove("D")
        return(",".join(furniture))
print(remaining(placement,furniture))

file=open("final_room.txt","w")
file.write("ROOM WITH FURNITURE:"+"\n"+updated_room(placement)+"\n")
file.write("REMAINING FURNITURE: "+str(remaining(placement,furniture))+"\n")
file.write("Number of furnitures:"+"\n"+"Chairs: "+str(remaining(placement,furniture).count("h"))+"\n"+"Table: "+str(remaining(placement,furniture).count("T"))+"\n"+"Desktop: "+str(remaining(placement,furniture).count("D")))
file.close()
