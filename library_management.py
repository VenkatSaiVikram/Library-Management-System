import csv
print("------------------------------------------------------\nSPS LIBRARY\n------------------------------------------------------\nENTER VIEW TO VIEW THE AVAILABLE BOOKS\nENTER ADD TO ADD A NEW BOOK\nENTER DELETE TO DELETE AN EXISTING BOOK\nENTER LEND TO LEND A BOOK\nENTER RETURN TO RETURN A BOOK\nENTER BORROWERS TO SEE THE BORROWERS LIST\nENTER EXIT TO EXIT THE PROGRAM\n------------------------------------------------------")
while True:
    def view_books():
        books_id=[]
        books_name=[]
        books={}
        file=open("books.csv","r")
        file=csv.reader(file)
        for i in file:
            books_id.append(i[0])
            books_name.append(i[1])
        for i in range(len(books_name)):
            books[books_id[i]]=books_name[i]
        
        print("\nBOOK ID|  BOOK NAME")
        
        for i in books.keys():
            print(i," | ",books[i])
            
        print("\n------------------------------------------------------")
    
    def add_book():
        books={}
        books_id=[]
        books_name=[]
        file=open("books.csv","r")
        file=csv.reader(file)
        for i in file:
            books_id.append(i[0])
            books_name.append(i[1])
        books_id=books_id[-1]
        books_id=int(books_id[1::])
        books_id="#000"+str(books_id+1)
        book_name=input("ENTER THE BOOK NAME : ")
        file=open("books.csv","a",newline="")
        add=csv.writer(file)
        add.writerow([books_id,book_name])
        file.close()
        file=open("books.csv","r")
        file=csv.reader(file)
        print("\nBOOK IS ADDED..!\n\n------------------------------------------------------\n")
        
    def delete_book():
        file=open("books.csv","r")
        file=csv.reader(file)
        book_name=input("BOOK NAME : ")
        for i in file:
            if i[0]=="#0001":
                file=open("books.csv","w",newline="")
                delete=csv.writer(file)
                if i[1].lower()==book_name.lower():
                    continue
                else:
                    delete.writerow(i)
                    file.close()
            else:
                file=open("books.csv","a",newline="")
                delete=csv.writer(file)
                if i[1].lower()==book_name.lower():
                    continue
                else:
                    delete.writerow(i)
                    file.close()
        print("\nBOOK IS DELETED..!\n\n------------------------------------------------------\n")
    def lend_book():
        file=open("lend.csv","a",newline="")
        lend=csv.writer(file)
        borrower_id=input("ADMISSION NUMBER : ")
        borrower_name=input("NAME : ")
        book_name=input("BOOK NAME : ")
        lend.writerow([borrower_id,borrower_name,book_name])
        file.close()
        print("\nBOOK IS LENDED..!\n\n------------------------------------------------------\n")

    def return_book():
        file=open("lend.csv","r")
        file=csv.reader(file)
        borrower_id=input("ADMISSION NUMBER : ")
        book_name=input("BOOK NAME : ")
        for i in file:
            if i[0]=="ID":
                file=open("lend.csv","w",newline="")
                Return=csv.writer(file)
                Return.writerow(i)
                file.close()
            else:
                file=open("lend.csv","a",newline="")
                Return=csv.writer(file)
                if i[0].lower()==borrower_id.lower() and i[2].lower()==book_name.lower():
                    pass
                else:
                    Return.writerow(i)
                    file.close()
        print("\nBOOK IS RETURNED..!\n\n------------------------------------------------------")
                    
    def borrowers_list():
        borrowers_id=[]
        borrowers_name=[]
        borrowed_book=[]
        borrowers={}
        file=open("lend.csv","r")
        file=csv.reader(file)
        for i in file:
            borrowers_id.append(i[0])
            borrowers_name.append(i[1])
            borrowed_book.append(i[2])
        for i in range(len(borrowers_id)):
           borrowers[borrowers_id[i]]=[borrowers_name[i],borrowed_book[i]]
        
        for i in borrowers.keys():
            print("\n",i," | ",borrowers[i][0]," | ",borrowers[i][1])
        print("\n------------------------------------------------------")
    
    choice=input("ENTER : ")
    print("\n------------------------------------------------------")
    
    if choice.lower()=="view":
        view_books()
        continue
        
    elif choice.lower()=="add":
        add_book()
        continue
        
    elif choice.lower()=="delete":
        delete_book()
        continue
        
    elif choice.lower()=="lend":
        lend_book()
        continue
        
    elif choice.lower()=="return":
        return_book()
        continue
        
    elif choice.lower()=="borrowers":
        borrowers_list()
        continue
        
    elif choice.lower()=="exit":
        break
    
    else:
        print("UNKNOWN OPTION!")
        continue