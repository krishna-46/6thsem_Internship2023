class Student :
    def __init__(self,name,id,gpa):
        self.name=name
        self.id=id
        self.gpa=gpa
    

    def get_name(self,name):
        return self.name
    
    def get_id(self,id):
        return self.id
    
    def get_id(self,gpa):
        return self.gpa


#student 1

First_student_name=input("Enter first student name :")
First_student_id=int(input("Enter first student id :"))
First_student_gpa=float(input("Enter first student gpa :"))

#Student 2

second_student_name=input("Enter second student name :")
second_student_id=int(input("Enter second student id :"))
second_student_gpa=float(input("Enter second student gpa :"))

# object of two student

s1=Student(First_student_name,First_student_id,First_student_gpa)
s2=Student(second_student_name,second_student_id,second_student_gpa)

# displaying 


print("student 1")
print("name :",First_student_name,"id :",First_student_id,"gpa :",First_student_gpa)

print("student 2")

print("name :" , second_student_name,"id :",second_student_id,"gpa :",second_student_gpa)

avrage_gpa=First_student_gpa+second_student_gpa/2

print("avrage gpa of two student is : ", avrage_gpa)


