print("                LIBRARY MANAGEMENT SYSTEM           ")

from functools import reduce 
print("")
book_list=[]
class Library:
    def add_book(self):
        b=[]
        title=input("Enter book title name :")
        author=input("Enter book author name :")
        num_page=int(input("Enter number of pages in book :"))
        b.append(title)
        b.append(author)
        b.append(num_page)
        book_list.append(b)
        print("--------------------------------------------")
        print("--------------------------------------------")
    def get_books_by_author(self):
        author_name=input("Enter name of author :")
        p=0
        for i in book_list:
            if author_name in i:
                print(f"{i[0]} book is written by {author_name}")
                p=1
        if p==0:
                print("book with this author name is not present")
        print("-------------------------------------------")
        print("-------------------------------------------")
        
    def total_pages(self):
         num_list=[]
         for j in book_list:
             num_list.append(j[2])
         def addition(x,y):
                 return x+y
         total=reduce(addition,num_list)
         print("total number of pages in library : ", total)
         print("------------------------------------------")
         print("------------------------------------------")
         
    

def table(self):
     print("book_names     author_names    pages")
     print("____________")
     for i in book_list:
                 print(f"{i[0]}  |   {i[1]}   |  {i[2]}")
                 print("_________")
         


lib=Library()

while True:  
# Displaying the option menu 
  print("Enter 1 to add new book")
  
  if len(book_list) >= 1:                            
   print("Enter 2 to display the book name")
   
  if len(book_list)>= 1:
   print("Enter 3 to display the total number of pages in library")
   
  if len(book_list)>= 1:
   print("Enter 4 to display the table of books")
   
  inp = input("Enter your choice :- ")             
  
  if int(inp) == 1:
    lib.add_book()

  elif int(inp)==2 and len(book_list) >= 1:
    lib.get_books_by_author()
    
  elif int(inp)==3 and len(book_list)>= 1:
      lib.total_pages()
      
  elif int(inp)==4 and len(book_list)>= 1:
      lib.table()           
  
  else:
    print("Invalid Choice, Exiting from the program")
    break

