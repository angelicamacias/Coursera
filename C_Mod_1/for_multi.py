def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1 

    # Complete the while loop condition.
    while multiplier < 25:
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            return 0
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(2)