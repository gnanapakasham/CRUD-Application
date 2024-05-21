import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host='localhost', user='root', password='root', database='testdb')


def create(name, age, city):
    res = con.cursor()
    sqlquery = "insert into studentdb(StudentName,age,CITY) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sqlquery, user)
    con.commit()
    print("Successfully added student entry in Database")


def update(name, age, city, id):
    res = con.cursor()
    sqlquery = "update studentdb set StudentName=%s,age=%s,CITY=%s where id=%s"
    user = (name, age, city, id)
    res.execute(sqlquery, user)
    con.commit()
    print("Successfully updated student entry in Database")


def delete(id):
    res = con.cursor()
    sqlquery = "delete from studentdb where id=%s"
    user = (id,)
    res.execute(sqlquery, user)
    con.commit()
    print("Successfully deleted student entry from Database")


def show():
    res = con.cursor()
    sqlquery = "select * from studentdb"
    res.execute(sqlquery)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))


input_banner = """
    Student Information
    
    1. Show Student Info
    2. Create New Entry
    3. Modify Student Details
    4. Delete Student Entry
    5. Exit
    """
while True:
    print(input_banner)
    choice = int(input("Enter you Choice : "))

    if choice == 1:
        show()
    elif choice == 2:
        name = input("Enter name of the Student : ")
        age = input("Enter Age of the Student : ")
        city = input("Enter City : ")
        create(name, age, city)
    elif choice == 3:
        id = input("Enter ID of the Student : ")
        name = input("Enter name of the Student : ")
        age = input("Enter Age of the Student : ")
        city = input("Enter City : ")
        update(name, age, city, id)
    elif choice == 4:
        id = input("Enter ID of the Student : ")
        delete(id)
    elif choice == 5:
        print("Thank You !!!")
    else:
        print("Invalid Input. Please enter right choice!!!")
