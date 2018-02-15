def inputList():
    file = open("ROOM.txt","r")
    content = file.read()
    file.close()
    sublist = []
    roomlist = []
    furniture = []
    for i in content:
        if i =='h' or i == 'T' or i == 'D':
            break
        if i != '\n':
            sublist.append(i)
        elif i == '\n':
            roomlist.append(sublist)
            sublist = []
    roomlist = roomlist[:-1]
    for i in content:
        if i == 'h' or i == 'T' or i == 'D':
            furniture.append(i)
    roomlist.append(furniture)
    return(roomlist)

def calculateSpaces():
    roomlist_plus_furniture = inputList()
    just_furniture = roomlist_plus_furniture[-1]
    just_roomlist = roomlist_plus_furniture[:-1]
    initial_count = 0
    for j in just_roomlist:
        for k in j:
            if k == '_':
                initial_count = initial_count + 1
    first_last = len(just_roomlist[0]) - 2
    mids = (len(just_roomlist) - 4) * 2
    total_spaces = initial_count - (first_last + mids + first_last)
    return(total_spaces)

def placeTables():
    ans = []
    roomlist = inputList()
    furniture = roomlist[-1]
    roomlist = roomlist[:-1]
    tables = 0
    for n in furniture:
        if n == 'T':
            tables = tables + 1
    replacements = 0    
    for l in range(len(roomlist)):
        if l == 0 or l == len(roomlist)-1 or l == len(roomlist)-2 :
            ans.append(roomlist[l])
        elif l%2 != 0:
            ans.append(roomlist[l])
        else:
            for m in range(3,len(roomlist[l])-2,2):
                if replacements == tables:
                    break
                roomlist[l][m] = 'T'
                replacements = replacements + 1
            ans.append(roomlist[l])
    remaining = tables - replacements
    ans.append(remaining)
    return(ans)

def placeMonitors():
    ans = []
    room = placeTables()
    remaining_tables = room[-1]
    room = room[:-1]
    original = inputList()
    furniture = original[-1]
    monitors = 0
    replacements = 0
    for s in furniture:
        if s == 'D':
            monitors = monitors + 1
    
    for p in range(len(room)):
        for q in range(len(room[p])):
            if replacements == monitors:
                break
            if room[p][q] == 'T':
                room[p-1][q] = 'D'
                replacements = replacements + 1
    for r in room:
        ans.append(r)
    remaining_monitors = monitors - replacements
    ans.append(remaining_tables)
    ans.append(remaining_monitors)
    return(ans)

def placeChairs():
    ans = []
    room = placeMonitors()
    remaining_tables = room[-2]
    remaining_monitors = room[-1]
    room = room[:-2]
    original = inputList()
    furniture = original[-1]
    chairs = 0
    for v in furniture:
        if v == 'h':
            chairs = chairs + 1
    replacements = 0
    for t in range(len(room)):
        for u in range(len(room[t])):
            if room[t][u] == 'T':
                if replacements == chairs:
                    break
                if room[t][u-1] == '_' and room[t][u-2] != 'h':
                    room[t][u-1] = 'h'
                    replacements = replacements + 1
                elif room[t][u+1] == '_' and room[t][u+2] != 'h':
                    room[t][u+1] = 'h'
                    replacements = replacements + 1
    for w in room:
        ans.append(w)
    remaining_chairs = chairs - replacements
    ans.append(remaining_tables)
    ans.append(remaining_monitors)
    ans.append(remaining_chairs)
    return(ans)

def extraTables():
    original_room = placeChairs()
    extra_tables = original_room[-3]
    room = original_room[:-3]
    ans = []
    replacements = 0
    if extra_tables == 0:
        return original_room
    else:
        for a in range(len(room)):
            if a == 0 or a == 1 or a == len(room)-1 or a == len(room)-2 :
                ans.append(room[a])
            elif a%2 == 0:
                ans.append(room[a])
            elif a%2 != 0:
                for b in range(2,len(room[a])-2,2):
                    if replacements == extra_tables:
                        break
                    if room[a][b] == '_':
                        room[a][b] = 'T'
                        replacements = replacements + 1
                ans.append(room[a])
    extra_tables = extra_tables - replacements
    if extra_tables == 0:
        ans.append(extra_tables)
        ans.append(original_room[-2])
        ans.append(original_room[-1])
        return(ans)
    else:
        anss = []
        rep = 0
        for n in range(len(ans)):
            if n == 0 or n == 1 or n == len(ans)-1 or n == len(ans)-2 :
                anss.append(room[n])
            else:
                for o in range(2,len(ans[n])-2):
                    if rep == extra_tables:
                        break
                    if room[n][o] == '_':
                        room[n][o] = 'T'
                        rep = rep + 1
                anss.append(room[n])
        extra = extra_tables - rep
        anss.append(extra)
        anss.append(original_room[-2])
        anss.append(original_room[-1])
        return(anss)

def extraMonitors():
    oroom = extraTables()
    etables = oroom[-3]
    emonitors = oroom[-2]
    echairs = oroom[-1]
    room = oroom[:-3]
    rep = 0
    if emonitors == 0:
        return(oroom)
    else:
        for q in range(len(room)):
            for r in range(2,len(room[q])-2):
                if room[q][r] == 'T':
                    if rep == emonitors:
                        break
                    if room[q-1][r] == '_':
                        room[q-1][r] = 'D'
                        rep = rep + 1
        extra_monitors = emonitors - rep
        room.append(etables)
        room.append(extra_monitors)
        room.append(echairs)
        return(room)
        

def extraChairs():
    oroom = extraMonitors()
    etables = oroom[-3]
    emonitors = oroom[-2]
    echairs = oroom[-1]
    room = oroom[:-3]
    rep = 0
    if echairs == 0:
        return(oroom)
    else:
        for a in range(2,len(room)-2):
            for b in range(2,len(room[a])-2):
                if rep == echairs:
                    break
                if room[a][b] == '_':
                    if room[a][b-1] != 'h' and room[a][b+1] != 'h':
                        room[a][b] = 'h'
                        rep = rep + 1
        extra = echairs - rep
        room.append(etables)
        room.append(emonitors)
        room.append(extra)                
        return(room)

def writeSolution():
    room = extraChairs()
    remaining_chairs = room[-1]
    remaining_monitors = room[-2]
    remaining_tables = room[-3]
    room = room[:-3]
    file = open("solution.txt","w")
    file.write("The room after placement of furniture will be:\n\n")
    for a in room:
        a = ''.join(a)
        a = a + '\n'
        file.write(a)
    tables = "\nThe number of remaining tables: " + str(remaining_tables)
    monitors = "\nThe number of remaining monitors: " + str(remaining_monitors)
    chairs = "\nThe number of remaining chairs: " + str(remaining_chairs)
    file.write(tables)
    file.write(monitors)
    file.write(chairs)
    file.close()
    
writeSolution()
    
    

