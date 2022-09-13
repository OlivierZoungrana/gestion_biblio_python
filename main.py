#
from Biblio.Abonne import *

def main():
   client = abonne("olivier", "geo", 1111)
   client1 = client
   client.Take_Book()
   print(client1)



if __name__ == '__main__':
    main()


