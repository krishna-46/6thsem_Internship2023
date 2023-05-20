# class Adding : # creating class 
#     a = 5
#     b = 10
#     c=a+b

# add = Adding() # creating object of class
# print(add.c) 

#.........................................................................................................

#Create a class named Person, use the __init__() function to assign values for name and age:

# class Person : # Creating  class
    
#     def __init__(self,name ,age) :  
#             self.name=name
#             self.age=age

    
#     def fun(p): # printing by function
#         print("My name is :"+p.name)
#         print("My age is :",p.age) # using (+) it give error only it will accsept string

#     # def __str__(self) :
#     #     return  f"{self.name}{self.age}" 
    
# person1 = Person("Krishna" , 18) #class Object

# person1.age= 17 # modifying object age
# person1.name= "Jon" # modifying object name

# # del person1.age # Deleting value
# # del person1 # Deleting object

# # print(person1)

# # print("Name :",person1.name  )

# # print("Age : ", person1.age)

# person1.fun() # calling Function (line 19)

# ............................Python Inheritance..............................................................................


# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person : # Create a Parent Class

#     def __init__(self , fname ,lname):
#         self.fname=fname
#         self.lname=lname

#     def printname(self):
#         print(self.fname,self.lname)


# p1 = Person("Krishna","jadhav")
# p1.printname()

# # Create a class named Student, which will inherit the properties and methods from the Person class

# class Student(Person): # Create a Child Class
#     # pass 
#     def __init__ (self,fname , lname,age):
#         # Person.__init__(self,fname,lname)
#         super().__init__(fname,lname) # no need to use parent class name (if using super())
#         # self.fname=fname
#         # self.lname=lname
#         self.age=age

#     def print(self):
#         print("name :" ,self.fname , self.lname ,"age : " ,self.age)

# s1=Student("Sudarahan" , "Jadhav",18)




# # s1.printname()
# s1.print()

# ..................................................................................................


    
# class add:

#     def adding(self,a,b):
#         return a+b
#         # self.a=a
#         # self.b=b

# obj_add = add() 

    
# class sub :

#     def subb(self,a,b):
#         return a-b

# obj_sub = sub() 
    
# class mul :

#     def mul(self,a,b):
#         return a*b

# obj_mul = mul() 


# class sum(add , sub , mul):

#     def display (self):
#         print(obj_add)

#.......................................................................

# class A :
#   def add(self,a,b):
#     return a+b
    
# class B(A):
#   def sub(self,a,b):
#     return a-b,


# class C(B):
#   def mul(self,a,b):
#     return a*b

  
  
# # class D(A,B):
# #   def printsum(self,add1):
# #     print(add1)

# obj=C()
# print(obj.add(4,6))
# print(obj.sub(4,6))
# print(obj.mul(4,6))


class Student :
    def __init__(self,name,age) :
        self.name=name
        self.age=age


s1=Student("Krishna",18)

print(s1.name)
    



   

