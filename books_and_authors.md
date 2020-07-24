# Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby

Book.objects.create(title="C Sharp")  
Book.objects.create(title="Java")     
Book.objects.create(title="Python")  
Book.objects.create(title="PHP") 
Book.objects.create(title="Ruby")         

# Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu

Author.objects.create( first_name="Jane", last_name="Austen")
Author.objects.create( first_name="Emily", last_name="Dickinson") 
Author.objects.create( first_name="Fyodor", last_name="Dostoevsky")
Author.objects.create( first_name="William", last_name="Shakespeare")     
Author.objects.create( first_name="Lau", last_name="Tzu")

# Query: Change the name of the C Sharp book to C#

book_one = Book.objects.get(id=1) 
book_one.title = "C#"    
book_one.save()   

# Query: Change the first name of the 4th author to Bill

fourth_author = Author.objects.get(id=4)  
fourth_author.first_name = "Bill"  
fourth_author.save()

# Query: Assign the second author to the first 3 books

first_author = Author.objects.get(id=1)                                                                          

book_to_assign = Book.objects.get(id=1)                                                                          

first_author.books.add(book_to_assign)                                                                           

book_to_assign = Book.objects.get(id=2)                                                                          

first_author.books.add(book_to_assign)    

# Query: Assign the second author to the first 3 books

In [7]: author_to_assign = Author.objects.get(id=2)                                                                      

In [8]: book_to_assign = Book.objects.get(id=1)                                                                          

author_to_assign.books.add(book_to_assign)                                                                       

book_to_assign = Book.objects.get(id=2)                                                                         

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=3)                                                                         

author_to_assign.books.add(book_to_assign) 

# Query: Assign the third author to the first 4 books

author_to_assign = Author.objects.get(id=3)                                                                     

book_to_assign = Book.objects.get(id=1)                                                                         

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=2)                                                                         

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=3)                                                                         

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=4)                                                                         

author_to_assign.books.add(book_to_assign) 

# Query: Assign the fourth author to the first 5 books (or in other words, all the books)


author_to_assign = Author.objects.get(id=4)                                                                     

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=2)                                                                      
                                                                    
book_to_assign = Book.objects.get(id=3)                                                                         

author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=4)                                                                         

In [33]: author_to_assign.books.add(book_to_assign)                                                                      

book_to_assign = Book.objects.get(id=5)                                                                         

author_to_assign.books.add(book_to_assign)  

# Query: Retrieve all the authors for the 3rd book

book_to_assign = Book.objects.get(id=3)                                                                         

book_to_assign.books.all()   

# Query: Remove the first author of the 3rd book

author_to_assign = Author.objects.get(id=1)                                                                     

book_to_assign = Book.objects.get(id=3)                                                                         

book_to_assign.books.remove(author_to_assign)                                                                   

book_to_assign.books_authors.remove(author_to_assign)  

# Query: Add the 5th author as one of the authors of the 2nd book

author_to_assign = Author.objects.get(id=5)                                                                     

book_to_assign = Book.objects.get(id=2)                                                                         

author_to_assign.books.add(book_to_assign) 