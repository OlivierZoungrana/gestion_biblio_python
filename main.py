#
from Biblio.Abonne import *
from Biblio.Gerant import *

def main():
   client = abonne("olivier", "geo", 1111)
   gestionnaire = gerant("olivier", "Zoungrana")
   gerant1 = gestionnaire
   #gerant1.Register_book()
   gerant1.Erase_book()
   print(listeLivre)
   print(books)

if __name__ == '__main__':
    main()


