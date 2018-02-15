#Function
def convertCurrency( amount , country ):

    currency = 0
    print('Converted Currency')
    if country == 'USD':
        currency = 0 #calculate here
        
    # Convert the amount in pkr to usd.
    # 1 US Dollar  = 110.74 PKR
    # print the converted currency in words.
    # 5000 PKR = 45.15 USD  is 'Forty five dollars and 15 cents' in words


    
    #Euro and British pound conversion missing here.

choice = 'Yes'     #our choice is 'Yes' by default
while(choice == 'Yes' or choice == 'yes'):  #the user can enter these two ways

    pkrCurrency = float( input('Enter currency in Pakistani Rupee : '))

    print('In which currency you want to convert this amount? ')
    print("1.\tUS Dollar:")
    print("2.\tEuro:")
    print("3.\tBritish Pound:")
    
    choice = input('Your answer here : ')


    if choice == '1' or choice == 'US Dollar'  :
        choice = 'USD'
        convertCurrency( pkrCurrency , choice)
        
    print("Do you want to convert again?")
    choice = input("Ans:")  #The loop will end if the choice is not 'Yes'

#Exercise:
#========
    
# Complete the above code.
# You have to complete IF block to call the function convertCurrency() for other conversions
# as well.
# Code is also missing in convertCurrency() function for other conversions.Complete this.



    

    
