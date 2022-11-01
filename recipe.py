
while True:
    print("\nSelect an option")
    print("1 add a recipe")
    print("2 view all recipes")
    print("3 search a recipe")
    print("4 update recipe")
    print("5 delete recipe")
    print("6 exit")
    
    ch=int(input("select an option  : \n"))
    if (ch==1):       
        print("selected add recipe")
    elif(ch==2):
         print("selected view all recipe")
    elif(ch==3):
        print("selected search recipe")
    elif(ch==4):
        print("selected update the recipe")
    elif(ch==5):
        print("selected delete recipe")
    elif(ch==6):
        break