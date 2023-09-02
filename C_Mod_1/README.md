# Recursive 
----------------------- Example 1
``` python
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2: 
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)
```

output:
```
Factorial called with 4
Factorial called with 3
Factorial called with 2
Factorial called with 1
Returning 1
Returning 2 for factorial of 2
Returning 6 for factorial of 3
Returning 24 for factorial of 4
```

A **recursive** function called factorial that calculates the factorial of a given number n. It prints the intermediate steps of the calculation.

When factorial(4) is called, the following steps occur:

The function is called with the argument 4.
The function prints "Factorial called with 4".
Since n is not less than 2, the function calculates result as 4 * factorial(3).
At this point, a recursive call to factorial is made with the argument 3. The same steps as above are repeated for n = 3, n = 2, and n = 1. Eventually, factorial(1) is reached, and the base case is triggered.

The function is called with the argument 1.
The function prints "Factorial called with 1".
Since n is less than 2, the function returns 1.
The previous recursive call, factorial(2), receives the value 1 and calculates result = 2 * 1 = 2.
The function prints "Returning 2 for factorial of 2" and returns 2.
The previous recursive call, factorial(3), receives the value 2 and calculates result = 3 * 2 = 6.
The function prints "Returning 6 for factorial of 3" and returns 6.
The previous recursive call, factorial(4), receives the value 6 and calculates result = 4 * 6 = 24.
The function prints "Returning 24 for factorial of 4" and returns 24.
Finally, the value of factorial(4) is 24, and that is the result printed when you call factorial(4).

--------------------- Example 2

```python
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n == 1:
        return 1

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```

The function sum_positive_numbers takes an argument n and returns the sum of all positive numbers between n and 1.

Here's how the code works:

If n is equal to 1, it means we have reached the base case, and we simply return 1 (since 1 is the only positive number between 1 and 1).
Otherwise, we recursively call sum_positive_numbers with the argument n - 1 and add n to the result. This will continue until n reaches 1, and then the recursion will unwind, summing up the numbers along the way.


-------- Summary
 A recursive function must inclde a recursive case and base case. 
 The **rescurve case** cualls the function again, with a defferent value. 
 The **base case** retuns a value without calling the same fucntion. 

 A rescursive function will usually have this structure: 

 ```python
 def recusive_funciton(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```
# For loops Anidados 

```python 
def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row + 1

    for column in range(n1,n2):
        print(column)
        for row in range(n1, n2):
            print( column, end = ' ')
        print()
matrix(1, 4)
```

remember see the prints of columns, then try to think how fly the first column value to the second 

output:
````
1
1 1 1 1 
2
2 2 2 2
3
3 3 3 3
4
4 4 4 4
```

