
#The user is prompted to type in a number using 'int(input)'

while True:
    user_input = int(input("Enter a number: "))
    
    # CONDITION: Must be an odd number AND must be between 1 and 20
    if user_input % 2!= 0 and 1 <= user_input <= 20:
        print("Yep, it's an odd one. Thanks!")
        break  

    #If the conditions aren't met, then the loop will continue. 
    else:
        print("That's not an odd number, choose something else.")
       
   