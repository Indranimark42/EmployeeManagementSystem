import mysql.connector, re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
Pattern = r"[\+\d{2,3}]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
connect = mysql.connector.connect(
    host="127.0.0.1", user="root", password="Kaushik5@", database="employee"
)
mycursor = connect.cursor()


def insert_data():
    name = input("Enter name: ")
    email = input("Enter the email: ")
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")
        insert_data()
    phoneno = input("Enter the phoneno: ")
    if re.match(Pattern, phoneno):
        print("Valid Phoneno")
    else:
        print("Invalid Phoneno")
        insert_data()
    mycursor.execute(
        "INSERT INTO empdata(name,email,phoneno) VALUES(%s,%s,%s);",
        (name, email, phoneno),
    )


def check_data(name, id):
    a = (
        name,
        id,
    )
    sql = "select * from empdata where name=%s and emp_id=%s;"
    b = connect.cursor(buffered=True)
    b.execute(sql, a)
    if b.rowcount == 1:
        return True
    else:
        return False


def delete_data():
    id = input("Enter id:")
    name = input("Enter name:")
    data = (
        name,
        id,
    )
    cdata = check_data(name, id)
    sql = "delete from empdata where name=%s and emp_id=%s;"
    if cdata == True:
        condata = connect.cursor(buffered=True)
        condata.execute(sql, data)
        print(
            "Employee with username %s  with id %s" % (name, id) + " has been deleted"
        )
    else:
        print("doesn't exist")


def display_data():
    name = input("Enter name:")
    id = input("Enter id:")
    bdata = (
        name,
        id,
    )
    result = check_data(name, id)
    sql = "select * from empdata where name=%s and emp_id=%s;"
    if result == True:
        res = connect.cursor(buffered=True)
        res.execute(sql, bdata)
        dis = res.fetchall()
        for r in dis:
            print("Id:", r[0])
            print("Name", r[1])
            print("Email", r[2])
            print("Phoneno", r[3])
    else:
        print("Not found")


def menu():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        print("Add employee:")
        insert_data()
        connect.commit()
        menu()

    elif ch == 2:
        print("Display employee data")
        display_data()
        connect.commit()
        menu()

    elif ch == 3:
        print("Delete employee data")
        delete_data()
        connect.commit()
        menu()

    elif ch == 7:
        exit(1)

    else:
        print("Entered a wrong option")
        connect.commit()
        menu()


menu()
connect.commit()
