import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='recipedb')

mycursor=mydb.cursor()

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
        title=input("Enter the recipe name")
        des=input("Enter the description about the recipe")
        pb=input("name of the chef")
        incrt=input("Enter the incrediants")
        category=input("Enter the category of the recipe")
        sql='INSERT INTO `recipes`(`title`, `description`, `preparedby`, `incrediants`, `category`) VALUES (%s,%s,%s,%s,%s)'
        data=(title,des,pb,incrt,category)
        mycursor.execute(sql,data)
        mydb.commit()      
        print("insertion successful")
    elif(ch==2):
        sql='SELECT * FROM `recipes`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("\nselected view all recipe")
    elif(ch==3):
        print("selected search recipe")
    elif(ch==4):
        print("selected update the recipe")
    elif(ch==5):
        print("selected delete recipe")
    elif(ch==6):
        break