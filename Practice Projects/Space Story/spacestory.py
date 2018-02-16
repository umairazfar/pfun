import random

#This function helps in drawing the required images
def writeImageCode(directory, var):
    name = "imageObj" + str(var)
    file.write("\n\t\t\tvar "+ name +" = new Image();")
    file.write("\n\t\t\t"+ name +".onload = function() {")
    file.write("\n\t\t\t\tcontext.drawImage("+ name +", 0, " + str(var * 125) +");\n\t\t\t};")
    file.write("\n\t\t\t"+ name +".src = 'Images/" + directory + "';\n")

#This function is used to write text, use True for Heading and False for normal text in the 'heading' argument
def writeTextCode(text, heading, var):
    if heading == True:
        file.write("\n\t\t\tcontext.font = 'bold 40pt Calibri';")
        file.write("\n\t\t\tcontext.fillText('" + text + "', 0, " + str((var * 125) + 50) +");")
    else:
        file.write("\n\t\t\tcontext.font = 'normal 16pt Calibri';")
        file.write("\n\t\t\tcontext.fillText('" + text + "', 0, " + str((var * 125) + 50) +");")
        
#This variable keeps the distance between lines in check
var = 0
#Keeps in check if the ship is alive
alive = True
loss = True

#opening file
file = open("spacestory.html", "w")

#writing the initial code to setup the HTML file

file.write("<!DOCTYPE HTML>\n<html>\n\t<head>\n\t\t<style>\n\t\t\tbody {")
file.write("\n\t\t\t\tmargin: 0px;\n\t\t\t\tpadding: 0px;\n\t\t\t}\n\t\t</style>")
file.write("\n\t</head>\n\t<body>")
file.write("\n\t\t<canvas id=\"myCanvas\" width=\"1000\" height=\"4000\"></canvas>\n\t\t<script>")
file.write("\n\t\t\tvar canvas = document.getElementById('myCanvas');")
file.write("\n\t\t\tvar context = canvas.getContext('2d');")
#Add the story specific code here

storyName = input('Enter the name of your story: ')
writeTextCode(storyName, True, var) 
var+=1
writeTextCode('You are the last hope for humanity, starting a journey from a desolated planet to your home ... EARTH!', False, var) 
var+=1
writeImageCode('ship1.jpg', var)
var+=1
writeTextCode('Your ship, although ill equiped is what you have to traverse this vast expanse of space', False, var) 
var+=1
writeImageCode('hyperspace.jpg', var)
var+=1
writeTextCode('You push the throttle and prepare for hyperspace jump into the unknown', False, var) 
var+=1

count = 0

while alive == True and loss == True:
    rand = random.randint(0,3)
    if rand == 0:
        writeImageCode('anomaly.jpg', var)
        var+=1
        writeTextCode('You came across a space anomaly', False, var)
        var+=1
        print("\nYou come across a space anomaly, it can give you some benefit or prove to be hazardous... what will you do?\n")
        print("1. Try to expore")
        print("2. Let it be... we cannot take any risks")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            rand = random.randint(0,3)
            if rand == 0:
                writeImageCode('destroyed.jpg', var)
                var+=1
                result = "You encountered a black hole whose intense gravity broke apart your ship"
                alive = False
                print("\n" + result)
                writeTextCode(result, False, var)
                break
            elif rand == 1:
                result = "The anomaly generated an energy pulse that made your ship stronger"
                print("\n" + result)
                writeTextCode(result, False, var)
            else:
                result = "Nothing turned up, it was a complete waste of time"
                print("\n" + result)
                writeTextCode(result, False, var)
            var+=1
        else:
            var+=1
    elif rand == 1:
        writeImageCode('planet.jpg', var)
        var+=1
        writeTextCode('You came across a planet', False, var)
        var+=1
        print("\nYou come across a planet which holds several resources... what will you do?\n")
        print("1. Try to expore")
        print("2. Let it be... we cannot take any risks")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            rand = random.randint(0,3)
            if rand == 0:
                writeImageCode('destroyed.jpg', var)
                var+=1
                result = "The planet's corrosive atmosphere destroyed your ship"
                alive = False
                print("\n" + result)
                writeTextCode(result, False, var)
                break
            elif rand == 1:
                result = "You were able to acquire a lot of resources for the journey"
                print("\n" + result)
                writeTextCode(result, False, var)
            else:
                result = "Nothing turned up, it was a complete waste of time"
                print("\n" + result)
                writeTextCode(result, False, var)
            var+=1
        else:
            var+=1
    else:
        writeImageCode('ship2.jpg', var)
        var+=1
        writeTextCode('You came across a spaceship', False, var)
        var+=1
        print("\nYou come across a spaceship which is trying to sell some wares?\n")
        print("1. Try to dock and trade")
        print("2. Let it be... we cannot take any risks")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            rand = random.randint(0,3)
            if rand == 0:
                writeImageCode('destroyed.jpg', var)
                var+=1
                result = "It was actually a slaver ship which took you hostage and so ended your journey"
                alive = False
                print("\n" + result)
                writeTextCode(result, False, var)
                break
            elif rand == 1:
                writeImageCode('enemykilled.jpg', var)
                var+=1
                result = "As you tried to dock, the ship attacked. You responded and destroyed the ship"
                print("\n" + result)
                writeTextCode(result, False, var)
            else:
                result = "Nothing turned up, it was a complete waste of time"
                print("\n" + result)
                writeTextCode(result, False, var)
            var+=1
        else:
            var+=1
    writeTextCode('You make a jump to the next quadrant', False, var) 
    var+=1
    writeImageCode('hyperspace.jpg', var)
    var+=2
    count+=1
    if count == 3:
        break
    
if count == 3:
    writeImageCode('victory.jpg', var)
    var+=1
    writeTextCode('You reached earth victorious and saved your people', False, var)

#writing the closing tags to finish the file
file.write("\n\t\t</script>\n\t</body>\n</html>")
           
file.close()


