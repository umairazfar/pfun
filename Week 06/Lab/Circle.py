#bs03702@st.habib.edu.pk    #bakhtawar
#ms03975@st.habib.edu.pk    #Faizan

#Functions, parameters and return statement

#A function is a collection of code that is reusable and can work on different values
#normally, the idea is that, you want to get something done. You know how it can be done
#but the results vary on the type of input

#suppose, you want to calculate the weight of oranges
#you use a weighing machine
#The weighing machine is a function, whatever number of oranges we give it, it will calculate the weight and then return you a certain value
#if you do not give it anything, it just returns the default value of zero

#Example

def Cube(number):
    ans = number**3
    return ans

ans = Cube(3)
#print(ans)



#Write a program to input radius of circle from user and
#find diameter, circumference and area of the given circle using the following function.

#getDiameter(radius)
#getCircumference(radius)
#getArea(radius) 

#All the above three functions uses one parameter i.e.
#radius of circle to calculate output. and return output


#[Define functions here]




print('Enter radius of circle: ')
radius = float(input())

dia = getDiameter(radius)   #Call getDiameter function
                            




print('Diameter of the circle :' , dia)



#Lab Exercise:
#============
# Define the following functions above:
#   getDiameter(radius)     
#   getCircumference(radius)
#   getArea(radius)


#Call these functions to calculate diameter, circumference and area of the given circle.


