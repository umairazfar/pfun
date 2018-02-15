def setting():
    a = open('projectii.txt', 'r')
    b = a.read()
    b = b.rstrip()
    g = ''
    for i in b:
        if i == 'h' or i == 'T' or i == 'D':
            break
        else:
            g = g+ i
    c = g.rstrip()
    c = c.split('\n')
    if len(c)<5:
        return 'Invalid'
    d = c[2:len(c)-2]
    e = []
    for i in d:
        e.append(i)
    f = ''
    g = 0 
    for i in e:
        for j in range(2,len(i)-2):
            f = f + i[j]
        f = f+'\n'
    k = f.rstrip()      
    h = k.split('\n')
    l = ''
    s = []
    t = ''
    for i in h:
        for j in i:
            s.append(j)
    for i in b:
        if i == 'h' or i == 'T' or i == 'D':
            if len(l)>1 and i!=l[-1]:
                l = l+ '\n'
            l = l+i
        else:
            pass
    counth = 0
    countT = 0
    countD = 0
    for i in l:
        if i == 'h':
            counth = counth +1
        if i == 'D':
            countD = countD +1
        if i == 'T':
            countT = countT +1
    m = len(h)-1
    q = len(k)-m
    r = int(q/len(h))
    n = k[0]
    o = l[0]
    if counth>1:
        for i in range(1):
                s[0] = 'h'
                s[-1] = 'h'
                counth = counth-2
    if countT>0:
        s[-2] = 'T'
        countT = countT -1
    if len(h)>1 and s[-2] == 'T' and countD>0:
        s[(len(s)-2)-r] = 'D'
        countD = countD -1
        if countD>0 and countT>0:
            s[(q-r)+1] = 'T'
            s[((q-r)+1)-r] = 'D'
            countT = countT-1
            countD = countD-1
        if countD>0 and countT>0:
            for i in range((q-r)-1,r-1,-1):
                if s[i] == '_' and s[i-r] == '_' and s[i+1]!='D' and s[i-1]!='D':
                    s[i] = 'T'
                    s[i-r] = 'D'
                    countT =countT -1
                    countD = countD-1
                    
                    if countD == 0 or countT == 0:
                        break
                    else:
                        pass
                else:
                    pass
    v = 1
    x = 1
    w = 0
    counthii = counth
    if (len(h)-1)*2 >= counth:
        for i in range(counth//2):
            if counth%2!=0:
                for i in range(counth//2+1):
                    if s[(r+0)*v] == '_' and s[((r+0)*v)+1]!='D' and s[((r+0)*v)-1]!='D':
                        s[(r+0)*v] = 'h'
                        counthii = counthii-1
                        v = v+1
                for i in range(counth//2):
                    if s[(q-r)-w] == '_' and s[((q-r)-w)+1] != 'D' and s[((q-r)-w)-1] != 'D':
                        s[(q-r)-w] = 'h'
                        counthii = counthii-1
                        w = w+5
            else:
                for i in range(counth//2):
                    if s[((r-1)+0)*v] == '_' and s[(((r-1)+0)*v)+1]!= 'D' and s[(((r-1)+0)*v)-1]!= 'D':
                        s[((r-1)+0)*v] = 'h'
                        counthii = counthii-1
                        v = v+1
                for i in range(counth//2):
                    if s[(q-r)-w] == '_' and s[((q-r)-w)+1]!= 'D' and s[((q-r)-w)-1]!= 'D':
                        s[(q-r)-w] = 'h'
                        counthii = counthii-1
                        w = w+5
    y = 0
    bb = 0
    countTii = countT
    if countT> 1:
        for i in range(countT//2):
            for i in range(countT//2):
                if countTii == 0:
                    break
                else:
                    z = (1+(r*y))
                    y = y + 1
                    if s[z] == '_':
                        s[z] = 'T'
                        countTii =countTii -1
                    else:
                        pass
            for i in range(countT//2):
                if countTii == 0:
                    break
                else:
                    aa = ((q-2)-(bb*r))
                    bb  = bb +1
                    if aa>=0:
                        if s[aa] == '_':
                            s[aa] = 'T'
                            countTii =countTii -1
                        else:
                            pass
    cc = 0
    dd= 0
    if countTii == 1:
        for i in range(len(h)):
            if s[i+(r*dd)] == '_' and s[(i+(r*dd))-1] == 'h':
                s[i+(r*dd)] = 'T'
                countTii = countTii -1
                dd = dd+1
                cc = cc+1
        if cc == 0:
            for i in range(len(h)):
                if s[(q-2)-(i*r)] == '_' and s[((q-2)-(i*r))+1]== 'h':
                    s[(q-2)-(i*r)] = 'T'
                    countTii = countTii -1
    if counthii>0:
        for i in range(len(s)):
            if s[i]=='_' and s[i+1] != 'h' and s[i-1] != 'h' and s[i+1] != 'D' and s[i-1] != 'D':
                s[i] = 'h'
                counthii = counthii -1
                if counthii == 0:
                    break
                else:
                    pass
            else:
                pass
    ee = ''
    ff = 1
    gg = r*ff
    for i in range(q):
        if i == gg:
            ee = ee + '\n'
            ff = ff+1
            gg = r*ff
        ee = ee + s[i]
    hh = ''
    for i in range(len(ee)):
        if ee[i] == '\n':
            hh = hh+'_W'
        hh = hh + ee[i]
    hh = hh+'_W'
    hh = 'W_' + hh
    ii = ''
    for i in range(len(hh)):
        if hh[i-1] == '\n':
            ii = ii+'W_'
        ii = ii + hh[i]
    jj = 'W'*(r+4)+'\n'
    kk = 'W'+'_'*(r+2)+'W'+'\n'
    ii = jj + kk +ii+'\n' + kk + jj  
    ii = ii.rstrip()        
    if countD<0:
        countD = 0
    if countTii<0:
        countTii = 0
    if counthii<0:
        counthii = 0
    return 'Room with best placement of furniture:'+'\n'+ii+'\n'+'Numbers of Chairs left:'+str(counthii)+'\n'+'Numbers of Tables left:'+str(countTii)+'\n'+'Numbers of Computers left:'+str(countD)
print(setting())
file = open('P.Fun_Project.txt', 'w')
file.write(setting())
file.close()

