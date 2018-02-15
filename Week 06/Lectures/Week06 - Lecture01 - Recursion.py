#Do not forget to make your ren'py groups

#Recursion is the repetition of an occurence in plain English

#when working in loops, we go back in the code and run the same code again
#in recursion, you call a function again inside itself
#lets look at this example

def Continue():
    val = input("Do you want to continue?")

    if val == 'y':
        Continue()
    return

Continue()

#how is this executed? Lets look into the code
#below is a rough indication of what is going on

def Continue():
    val = input("Do you want to continue?")

    if val == 'y':
        val = input("Do you want to continue?")

        if val == 'y':
            val = input("Do you want to continue?")

            if val == 'y':
                val = input("Do you want to continue?")

                if val == 'y':
                    val = input("Do you want to continue?")
                    
    return

Continue()
#this can help us do things like printing lines

def Count(n):
    if n < 3:
        print(n, "sheeps jumped over the fence")
        n+=1
        Count(n)
    return

Count(0)

#We can further refine it

def Count(n):
    if n < 3:
        if n == 1:
            print(n, "sheep jumped over the fence")
        else:
            print(n, "sheeps jumped over the fence")
        n+=1
        Count(n)
    return

Count(0)

#Calculating Evens and Odds
def EvenOdd(n):
    if n < 10:
        print(n)
        n=n+2
        EvenOdd(n)
    return

EvenOdd(0)
EvenOdd(1)

#Almost the same function... What will be the outcome?
def EvenOdd(n):
    if n < 10:        
        n=n+2
        EvenOdd(n)
        print(n)
    return
