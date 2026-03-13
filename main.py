#this module contain main fucntion which will call all other functions
from library import LIBRARY

def menu():
    print("1. Add Paper\n"
    "2. View Papers\n"
    "3. Search Papers\n"
    "4. Find Similar Papers\n"
    "5. Exit\n")

#taking filename
filename=input("Enter filename: ")
lib=LIBRARY(filename)
lib.load_data()

while True:
    menu()
    print("\n")
    while True:
        try:
            opt=int(input("Enter option: "))
            if 1<=opt<=5:
                break
            print("Enter valid option")
        except ValueError:
            print("Enter integer options(1-5)")

    if opt==1:
        lib.add_paper()

    elif opt==2:
        lib.display_all()

    elif opt==3:
        query=input("Enter words to look(Seperated by comma): ")
        lst=lib.search(query)
        for idx,(paper,count) in enumerate(lst,1):
            print(f"{idx}. {paper.title} (occurence: {count})")
           
            

    elif opt==4:
        title=input("Enter title: ")
        lst=lib.find_similar(title)
        for idx,(paper,cos) in enumerate(lst,1):
            print(f"{idx}. {paper.title}")

    elif opt==5:
        print("Goodbyee👽")
        break
    
    print("\n")




    
