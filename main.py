# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Biblio.Abonne import *

def main():
    # Use a breakpoint in the code line below to debug your script.
   client = abonne("olivier", "geo", 1111)
   client1 = client
   client.Take_Book()
   print(client1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
