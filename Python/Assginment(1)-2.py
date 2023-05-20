# Prompt the user to enter a list of integers, separated by commas.

user_input=input("Enter your list :") # tacking input from user 

con=[int(a) for a in user_input.split()] #converting to integer


# square list

squared_list=list(map(lambda x:x **2 , con))

  # filtered squared list divisible by 3  " useing filter function "

filtered_list= list(filter(lambda a: a%3 == 0 ,con))

# reduceing the filtered list
from functools import reduce
red=reduce(lambda a,b : a*b , filtered_list)

# even elements

even_list=list(filter(lambda x: x % 2 == 0,con ))

# squareing even list
square_even_list = list(map(lambda x :x**2 , even_list))

#  squared even list that are greater than or equal to 16.
greater_than_16 = list(filter(lambda x : x >=16, square_even_list))

# reduceing all elements sum in  filtered list

reduce_sum=reduce(lambda x,y : x+y , filtered_list)
print("squared_list : " , squared_list)
print("filtered_element divisible by 3  : " , filtered_list)
print(red)
print("Even list :" , even_list)
print("squareing even list : " , square_even_list)
print("squared even list that are greater than or equal to 16 : " , greater_than_16)
print("sum in  filtered list : " , reduce_sum)
