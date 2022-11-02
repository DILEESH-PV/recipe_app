import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='recipedb')

mycursor=mydb.cursor()

while True:
    print("\nSelect an option")
    print("1 add a recipe")
    print("2 view all recipes")
    print("3 display recipe details by name")
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
        name=input("Enter the recipe name for searching the recipe")
        sql="SELECT * FROM `recipes` WHERE `title`='"+name+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(ch==4):
        name=input("Enter the recipe name ")
        des=input("enter the recipe description to be updated")
        pb=input("name of the chef to be updated ")
        incre=input("enter the incrediants to be updated")
        cat=input("Enter the category to be updated")
        sql="UPDATE `recipes` SET `description`='"+des+"',`preparedby`='"+pb+"',`incrediants`='"+incre+"',`category`='"+cat+"' WHERE `title`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully")  
    elif(ch==5):
        name=input("Enter the recipe name for deletion ")
        sql="DELETE FROM `recipes` WHERE `title`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("deleted successfully")
    elif(ch==6):
        break