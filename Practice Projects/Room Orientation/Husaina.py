#I have given priority to the tables for the setting of the room and used the random function to set them.
#Thus, the program will generate different outputs every time, also for the same size of the room.
#The program ensures space between furniture and would not necessarily fir all tge furniture in the room despite the space.
import random
file1=open('output.txt','w')
file=open('Project_2.txt','r')
lst2=[]
lst1=[]
lst3=[]
for e in file:
     if e.strip().startswith('D') and e.strip().endswith('D')or e.strip().startswith('T') and e.strip().endswith('T') or e.strip().startswith('h') and e.strip().endswith('h'):
        for i in e.strip():
           lst1.append(i)
     lst2.append(e.strip())
i=0
while i<2:
     for e in range(len(lst2)):
        if len(lst2[e])>1:
             c=lst2[e].count('w')
             if c==len(lst2[e])  and 'T' not in lst2[e+1] and 'D' not in lst2[e+1] and 'h' not in lst2[e+1]:
                  lst=[]  
                  for w in lst2[e]:
                     lst.append(w)
                  lst3.append(lst)   
                  lst2[e]='to be ignored'
                  i+=1
                  break
             elif i>0 and 'w' in lst2[e] and'_' in lst2[e] and'T' not in lst2[e] and 'D' not in lst2[e] and 'h' not in lst2[e]:
                  lst=[]  
                  for w in lst2[e]:  
                     lst.append(w)
                  lst3.append(lst)  
                  lst2[e]='to be ignored'
                  break
             else:
                  continue               

file.close()
def placingtables(lst1,lst3):
     if 'T' in lst1:
          c=lst1.count('T')
          if c<((len(lst3[0])-2)-2)*(len(lst3)-2-2):
               i=0
               while i<c:
                   a=random.randint(2,len(lst3)-3)
                   b=random.randint(2,len(lst3[a])-3)
                   if lst3[a][b]!='T' and lst3[a-1][b]!='T' and lst3[a+1][b]!='T' and 'D' not in lst1:
                        lst3[a][b]='T'
                        lst1.remove('T')
                        i+=1
                   elif lst3[a][b]!='T' and lst3[a-1][b]!='T' and lst3[a+1][b]!='T' and 'D' in lst1 and a%2!=0:
                        lst3[a][b]='T'
                        lst1.remove('T')
                        i+=1     
          elif c>((len(lst3[0])-2)-2)*(len(lst3)-2-2):
               i=0
               while i<(((len(lst3[0])-2)-2)*(len(lst3)-2-2)):
                   a=random.randint(2,len(lst3)-3)
                   b=random.randint(2,len(lst3[a])-3)
                   if lst3[a][b]!='T' and lst3[a-1][b]!='T' and lst3[a+1][b]!='T':
                        lst3[a][b]='T'
                        lst1.remove('T')
                        i+=1
                                      
   
def placingchairs(lst1,lst3):     
    characters=['_','D','T']
    for i in range(2,len(lst3)-2):
         for e in range(len(lst3[i])):
              if lst3[i][e]=='T' and 'h' in lst1:
                   if lst3[i][e+1]=='_' and lst3[i][e-1]=='_' and lst3[i][e+2] in characters and lst3[i][e-2] in characters:
                        if len(lst3[i])-e<e and lst3[i-1][e+1]!='h' and lst3[i+1][e+1]!='h':
                             lst3[i][e+1]='h'
                             lst1.remove('h')
                        elif len(lst3[i])-e>e and lst3[i-1][e-1]!='h' and lst3[i+1][e-1]!='h':
                             lst3[i][e-1]='h'
                             lst1.remove('h')
                        elif len(lst3[i])-e==e:
                             lst3[i][e+1]='h'
                             lst3[i][e-1]='h'
                             lst1.remove('h')
                             lst1.remove('h')
                   elif lst3[i][e+1]=='_' and lst3[i][e+2] in characters and lst3[i-1][e+1]!='h' and lst3[i+1][e+1]!='h':
                        lst3[i][e+1]='h'
                        lst1.remove('h')
                   elif lst3[i][e-1]=='_' and lst3[i][e-2] in characters and lst3[i-1][e-1]!='h' and lst3[i+1][e-1]!='h':
                        lst3[i][e-1]='h'
                        lst1.remove('h')
                        
def placingcomputers(lst1,lst3):   
     characters=['h','D']
     for i in range(3,len(lst3)-2):
          for n in range(len(lst3[i])):
               if lst3[i][n]=='T' and lst3[i-1][n]=='_' and 'D' in lst1 and lst3[i-1][n-1] not in characters:
                    lst3[i-1][n]='D'
                    lst1.remove('D')
     if len(lst1)==0:
          file1.write('All furniture has been placed inside the room'+'\n')
          
     else:
          file1.write('The remaining '+str(len(lst1))+' furniture piece/pieces is/are below:'+'\n')
          file1.write(' '.join(lst1)+'\n')
          
def finalroom(lst3):
     lst4=[]
     for e in lst3:
          line=''.join(e)
          lst4.append(line)
     file1.write('\n'.join(lst4))
    
placingtables(lst1,lst3)
placingchairs(lst1,lst3)
placingcomputers(lst1,lst3)
finalroom(lst3)
file1.close()         


     
                        
                        
                    
               

