from .data import *
class gerant:
    def __init__(self, name,surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

    def Register_book(self):
        newBook = input(" ajouter un nouveau livre : ")

        if newBook not in listeLivre:
            listeLivre.append(newBook)
            books.update({newBook:1})
            print(books)
        else:
            books[newBook] +=1
            print("vous avez ajouter un nouvel exemplaire de ce livre")
    def Erase_book(self):
        book_erase = input("nom du livre à delete: ")

        if book_erase in listeLivre:
            if books[book_erase] == 0:

                listeLivre.remove(book_erase)
            books[book_erase]-=1
        else:
            print("ce livre n'exite pas dans la base")
