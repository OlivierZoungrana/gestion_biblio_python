from .data import books
from .data import listeLivre
class abonne:
    def __init__(self, name, surname, identifiant):
        self.name =name
        self.surname = surname
        self.identifiant = identifiant

    def __str__(self):
        return self.name + " " + self.surname
    # if you want to take a book you can use this method
    def Take_Book(self):
        livre_Emprunte = []
        choix = input("vous pouvez choisir un livre: ")

        if choix in listeLivre:
            print("ce livre est disponible")

            quantite = int(input("quel quantité: "))
            if quantite > books[choix]:
                print("quantite indisponible")
            else:
                print("vous pouvez empruntez ce livre")
                livre_Emprunte.append(choix)
                print(livre_Emprunte)
        else:
            print("non disponible")

    # when the book is comming back this method is used
    def Rest_livre(self):
        pass
