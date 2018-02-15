#Exercise 1:
#==========
#Write a function that confirms side1, side2, and side3 of a triangle are positive and non-zero.



#Exercise 2:
#==========
#A triangle is valid if sum of its two sides is greater than the third side.
#The triangle is valid , if all three conditions are satisfied.
# side1 + side2 > side3
# side1 + side3 > side2 and
# side2 + side3 > side1

#Write a function that checks to see if side1, side2, and side3 corresponds to a correctlyformed triangle.
#[Precondition : sides of triangle are positive and non-zero]


#Perimeter of an triangle.
#=========================
#The perimeter is the total distance around the outside, which can be found by adding together
#the length of each side.
def perimeter(side1 , side2 , side3):

    return (side1 + side2 + side3)



#Exercise 3:
#==========
#The area of an arbitrary triangle can be computed using the formula
#area = √(s(s - side1)(s - side2)(s - side3))
#where side1, side2, and side3 are the lengths of the sides, and s is the semiperimeter.
#s = (side1 + side2 + side3)/2


#Write a function to calculate the semiperimeter of a triangle.
#The semiperimeter of a triangle is half its perimeter.

# [Precondition : sides of triangle can correctly form a triangle]


#Exercise 4:
#==========
#Write a function to calculate the area of a triangle.




side1 = int(input('Enter side 1: '))
side2 = int(input('Enter side 2: '))
side3 = int(input('Enter side 3: '))
