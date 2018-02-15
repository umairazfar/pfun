wall = 'w'
space= '_'
chair = 'h'
table = 'T'
computer = 'D'
##room dimensions will contain empty room
##where walls and empty spaces where the furniture will be placed
roomDimensions = []
##chairList will contain total number of chairs
chairList = []
totalChairs=0
##tableList will contain total number of chairs
tableList=[]
totalTables=0
##computerList will contain total number of computers
computerList=[]
totalComputers=0
##reading file and storing all the data in the list
fo= open("RoomConfig.txt",'r+')   #r and w
filedata= fo.readlines()
print("string is:",filedata[0][0])
print("Read string is:", filedata[1])
fo.close()

##extracting room information from file and storing in room data

row =0
while filedata[row][0]== wall:
    row =row+1
print(row)


col=0
while filedata[0][col]==wall:
    col=col+1
print(col)

##creating a list

for j in range(row):
    column = []
    for i in range(col):
        column.append(0)
        #print(column)
    roomDimensions.append(column)
        #print(roomDimensions)
##filling data in room dimensions
for i in range(row):
    for j in range(col):
        roomDimensions [i][j]= filedata[i][j]
print('roomDimensions the real ones: ', roomDimensions)
##now to extract furniture and computer info
#print(row)
i=0
for i in range(row):
    filedata.pop(0)
    #print(i)
#print(filedata)
##removing unwanted operators if there are any.
UnwantedChar1= "\xa0\n"

while filedata[0]==UnwantedChar1:
    filedata.pop(0)
print('1st',filedata)
#print('xyz',filedata)
##extracting Chair,Table and Computer info.
for i in range(len(filedata)):
    length =len(filedata[i])
    if (filedata[i][length-1]) == '\n':
        length = length-1
#print(length)

    j=0
    if filedata[i][0] == chair:
        for j in range(length):
            chairList.append(0)
            chairList[j] = filedata[i][j]


    if filedata[i][j]== table:
        for j in range(length):
            tableList.append(0)
            tableList[j] = filedata[i][j]


    if(filedata[i][0] == computer):
        for j in range(length):
            computerList.append(0)
            computerList[j] = filedata[i][j]
#print(chairList)
print(tableList)            
print(computerList)

totalChairs = len(chairList)
totalTables= len(tableList)
totalComputers = len(computerList)
print("Total Chairs :",totalChairs)
print("Total Tables:",totalTables)
print('total computers:',totalComputers)
print('room dimensions:, %d*%d'%(row,col))

##to calculate the room area that can be utilized for furniture

startRow= 2
startCol = 2
endRow = row -2
endCol = col -2

print('start point: %d*%d'%(startRow,startCol))
print('end point: %d*%d'%(endRow,endCol))



AvailableRows = endRow-startRow
AvailableCols = endCol- startCol
#print('AvailableRows=',AvailableRows)
#print("AvailableCol=", AvailableCols)
print("Available Room Dimensions for furniture: %d *%d"%(AvailableRows,AvailableCols))
## creating a tree for furniture placement in accordance with the following rules:
## nothing can be placed next to a wall, horizontally or vertically
## two chairs cannot be placed next to each other horizontally
## chairs can be placed next to tables
## two tables can be next to each other
## Computers can only be above a table
## You have to ensure that there is maximum space between furniture, meaning
## The furniture should be as close to the walls as possible
## Your code should work for any room size and any number of furniture.
##It should tell the user about the extra furniture it could not fit


treeIndex=0
if totalChairs<totalTables:
    treeIndex = totalChairs

if totalChairs>totalTables:
    treeIndex =totalTables

if totalChairs==totalTables:
    treeIndex = totalChairs

FurniturePlacingTree = []

for k in range(treeIndex):
    FurniturePlacingTree.append(chairList[k])
    #print(FurniturePlacingTree)
    FurniturePlacingTree.append(tableList[k])
    #print(FurniturePlacingTree)
    #FurniturePlacingTree.append(computerList[k])
    #print(FurniturePlacingTree)
print("FurniturePlacingTree =", FurniturePlacingTree)
totalSpaceForFurniture = AvailableRows*AvailableCols
print("total space:", totalSpaceForFurniture)

##placing furniture from top to bottom
colCounter= startCol
rowCounter= startRow

while(rowCounter<=endRow):
    #placing Chair
    if (len(FurniturePlacingTree)>0):
        roomDimensions[rowCounter][colCounter] = FurniturePlacingTree[0]
        FurniturePlacingTree.pop(0)
        #print("the tree is:",FurniturePlacingTree)
    #Placing table
    if (len(FurniturePlacingTree)>0):
        roomDimensions[rowCounter][colCounter+1] =FurniturePlacingTree[0]
        FurniturePlacingTree.pop(0)
        #print("tree       :",FurniturePlacingTree)

    rowCounter= rowCounter +2

rowCounter = startRow
colCounter= endCol-1# this will make it start from 0
#Direction of placing from right to left

while rowCounter<=endRow:
        ## placing chairs
        if len(FurniturePlacingTree)>0:
            roomDimensions[rowCounter][colCounter] = FurniturePlacingTree[0]
            FurniturePlacingTree.pop(0)
        ##placing tables
        if len(FurniturePlacingTree) >0:
            roomDimensions[rowCounter][colCounter-1] = FurniturePlacingTree[0]
            FurniturePlacingTree.pop(0)    
        rowCounter=rowCounter +1
#print("places:",FurniturePlacingTree)

print('Computers:',computerList)

print('roomDimensions testing',roomDimensions)

fi=open("DecoratedRoom.txt","w+")

#for i in range(row):
#    for j in range(col):
#            #roomDimensions=str(roomDimensions)
#        fi.write(roomDimensions [i][j])
#    fi.write("\n")
#fi.close()

##for i in roomDimensions:
##    for j in i :
##        print(j,end='')
##    print(j)
##

for i in range(len(roomDimensions)):
    for j in range(len(roomDimensions[i])) :
        if roomDimensions[i][j]=="T" and computerList and i<len(computerList):
            roomDimensions[i-1][j]=computerList.pop()


for i in range(len(roomDimensions)):
    for j in range(len(roomDimensions[i])) :
        print(roomDimensions[i][j],end='')
    print()
######Putting computers here !!!!!
###z=len(roomDimensions)
##for s in roomDimensions[i][j]:
##    for t in s:
##        #print(t)
##        if roomDimensions[j]=='T':
##            roomDimensions.replace([i-1],'D')
#print('Computer',roomDimensions)
    
#for m in range(roomDimensions):
#    for n in range(m):
#        print(n)
print("Number of chairs left:",len(FurniturePlacingTree))
print("Number of Tables left:",len(FurniturePlacingTree))
print("Number of computers left:",len(computerList)-len(roomDimensions[i-1][j]))























      











































    








