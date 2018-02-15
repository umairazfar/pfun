l=int(input('length='))
w=int(input('width='))
chair=input('chair=')
table=input('table=')
computer=input('computer=')

def furniture(chair,table,computer):
        wall_one=('W'*w+'\n'+('W'+'_'*(w-2)+'W')) #Room
        print(wall_one)
        x=''
        for i in range(l-4):
               x=x+('W'+'_'*(w-2)+'W')+'\n'
               room=x.strip()
        wall_two=('W'+'_'*(w-2)+'W'+'\n'+'W'*w)    
        print(room)
        print(wall_two)
        empty_spaces1=wall_one.count('_')
        empty_spaces2=x.count('_')
        empty_spaces3=wall_two.count('_')
        total_empty_spaces=empty_spaces1+empty_spaces2+empty_spaces3#Empty spaces              
        print('number of empty spaces=',total_empty_spaces)
        
furniture(chair,table,computer)


